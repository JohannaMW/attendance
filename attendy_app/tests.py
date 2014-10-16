from django.core.exceptions import ValidationError
from django.test import TestCase
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



