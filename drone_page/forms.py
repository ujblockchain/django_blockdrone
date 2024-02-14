from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


from .models import DroneUser


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = DroneUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ] + ("user_type", "tel_number")
