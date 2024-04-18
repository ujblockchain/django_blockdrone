from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

from users.forms import CustomUserChangeForm
from .models import Profile, City

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


class UpdateUserForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "account-settings__form-input",
                "placeholder": "First Name",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "account-settings__form-input",
                "placeholder": "Last Name",
            }
        ),
    )
    email = forms.EmailField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "account-settings__form-input", "placeholder": "Email"}
        ),
    )

    tel_number = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "account-settings__form-input",
                "placeholder": "Phone number",
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "tel_number",
        ]


class ProfileForm(forms.ModelForm):

    profile = forms.CharField(
        max_length=10000,
        widget=forms.Textarea(
            attrs={
                "class": "account-settings__form-input",
                "placeholder": "About you",
            }
        ),
    )
    country = forms.CharField(
        max_length=150,
        widget=forms.Select(
            attrs={
                "class": "account-settings__form-input",
                "placeholder": "Select Country",
            }
        ),
    )
    city = forms.CharField(
        max_length=150,
        widget=forms.Select(
            attrs={
                "class": "account-settings__form-input",
                "placeholder": "Select City",
            }
        ),
    )

    class Meta:
        model = Profile
        fields = ["profile", "country", "city", "profile_image"]

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields["city"].queryset = City.objects.none()

            if "country" in self.data:
                try:
                    country_id = int(self.data.get("country"))
                    self.fields["city"].queryset = City.objects.filter(country_id=country_id).order_by("name")
                except (ValueError, TypeError):
                    pass 
            elif self.instance.pk:
                self.fields["city"].queryset = self.instance.country.city_set.order_by("name")
