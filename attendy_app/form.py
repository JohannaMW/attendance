from django import forms
from django.contrib.auth.forms import UserCreationForm
from attendy_app.models import People

class PeopleForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = People
        fields = ("username", "email", "password1", "password2", "user_type", "class_number")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            People.objects.get(username=username)
        except People.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
