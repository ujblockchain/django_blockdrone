from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
#custom user
User = get_user_model()


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "user_type",
            "tel_number",
        ]
