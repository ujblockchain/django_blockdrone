from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

from users.forms import CustomUserChangeForm

# custom user
User = get_user_model()


# Register User
class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form__field", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "form__field",
                "placeholder": "Password Confirmation",
            }
        ),
    )

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
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "Username"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "Last Name"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "Email"}
            ),
            "user_type": forms.Select(
                attrs={"class": "form__field", "placeholder": "Which One Are You?"}
            ),
            "tel_number": forms.TextInput(
                attrs={"class": "form__field", "placeholder": "Phone number"}
            ),
        }


# Authenticate a User (model form)
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form__field", "placeholder": "Username"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form__field", "placeholder": "Password"}
        )
    )



# "password1": forms.PasswordInput(
#                 attrs={"class": "form__field", "placeholder": "Password"}
#             ),
#             "password2": forms.PasswordInput(
#                 attrs={
#                     "id": "confirmPassword",
#                     "class": "form__field",
#                     "placeholder": "Password Confirmation",
#                 }
#             )
