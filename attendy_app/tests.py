from time import sleep
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from forms import TeacherForm, PeopleForm
from models import People
from views import check_in



class RegisterTest(TestCase):
    def test_clean_username_exception(self):
        People.objects.create_user(username='Bob')
        form = PeopleForm()
        form.cleaned_data = {'username': 'Bob'}

        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_clean_username_pass(self):
        People.objects.create_user(username='haha')
        form = PeopleForm()
        form.cleaned_data = {'username': 'unique'}
        form.clean_username()


class FormTest(TestCase):
    def test_teacher_form(self):
        form = TeacherForm(data= {'date': '2014-10-15'})
        self.assertTrue(form.is_valid())



        # resp = self.client.get('/teacher_home/')
        # self.assertEqual(resp.status_code, 200)
        # self.assertTrue('Students checked' in resp.context)

class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_admin_login(self):
        People.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_name('username').send_keys('superuser')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('mypassword')
        password_input.send_keys(Keys.RETURN)
        sleep(.5)

        # We check to see if 'Site administration' is now on the page, this means we logged in successfully
        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)


def admin_login(self):
    # Create a superuser
    People.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')

    # let's open the admin login page
    self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))

    # let's fill out the form with our superuser's username and password
    self.selenium.find_element_by_name('username').send_keys('superuser')
    password_input = self.selenium.find_element_by_name('password')
    password_input.send_keys('mypassword')

    # Submit the form
    password_input.send_keys(Keys.RETURN)

def test_admin_create_user(self):
    self.admin_login()
    self.selenium.find_elements_by_link_text('Users')[0].click()
    self.selenium.find_element_by_link_text('Add user').click()
    self.selenium.find_element_by_name('password').send_keys('password')
    self.selenium.find_element_by_name('username').send_keys('testuser')

    self.selenium.find_element_by_css_selector("input[value='Save']").click()

    sleep(.5)

def test_admin_edit_user(self):
         self.admin_login()
         self.selenium.find_elements_by_link_text('Users')[0].click()
         self.selenium.find_elements_by_link_text('Jo')[2].click()
         sleep(.5)


# class FormTest(TestCase):
#     def test_teacher_form(self):
#         form = TeacherForm(data= {'date': '2014-10-15'})
#         form.cleaned_data = {'date': '2014-10-15'}
#         resp = self.client.get('/teacher_home/')
#         self.assertEqual(resp.status_code, 200)
#         self.assertTrue('Students checked' in resp.context)

# class ViewsTest(TestCase):
#
#     def test_check_in(self):
#         user = People.objects.create_user(username='test-user', email='test@test.com', password='password')
#         check_in(user)
#         resp = self.client.get('/check_in/')
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(resp.context[0].fields.username, 'test-user')
#
#         pass
#
#     def test_get_mayor(self):
#         pass



