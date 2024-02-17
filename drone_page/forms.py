from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from users.forms import CustomUserChangeForm

# custom user
User = get_user_model()


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "user_type",
            "tel_number",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "Last Name"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "Email"}
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form__field", "placeholder": "Password"}
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "id": "confirmPassword",
                    "class": "form__field",
                    "placeholder": "Password Confirmation",
                }
            ),
            "user_type": forms.Select(
                attrs={"class": "form__field", "placeholder": "Which One Are You?"}
            ),
            "tel_number": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "Phone number"}
            ),
        }
