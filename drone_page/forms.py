from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

from users.forms import CustomUserChangeForm
from .models import Profile, City, JobRequestModel

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

    # profile = forms.CharField()
    # country = forms.ChoiceField()
    # city = forms.CharField(
    #     max_length=150,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "account-settings__form-input",
    #             "placeholder": "Select City",
    #         }
    #     ),
    # )

    class Meta:
        model = Profile
        fields = ["profile", "country", "city", "hourly_rate", "profile_image"]

        widgets = {
            "profile": forms.Textarea(
                attrs={
                    "class": "account-settings__form-input",
                    "placeholder": "Tell us about yourself...",
                    "required": True,
                }
            ),
            "country": forms.Select(
                attrs={
                    "class": "account-settings__form-input",
                    "placeholder": "Country",
                    "required": True,
                }
            ),
            "city": forms.Select(
                attrs={
                    "class": "account-settings__form-input",
                    "placeholder": "Username",
                    "required": True,
                }
            ),
            "hourly_rate": forms.NumberInput(
                attrs={
                    "class": "account-settings__form-input",
                    "placeholder": "Enter Hourly Rate",
                }
            ),
            "profile_image": forms.FileInput(
                attrs={
                    "class": "account-setting__avatar",
                    "placeholder": "Username",
                    "accept": "image/png, image/jpeg",
                }
            ),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["city"].queryset = City.objects.none()

            for key in ["profile", "country", "city"]:
                self.fields[key].required = True

            if "country" in self.data:
                try:
                    country_id = int(self.data.get("country"))
                    self.fields["city"].queryset = City.objects.filter(
                        country_id=country_id
                    ).order_by("name")
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields["city"].queryset = self.instance.country.city_set.order_by(
                    "name"
                )


class JobRequestsForm(forms.ModelForm):

    class Meta:
        model = JobRequestModel
        exclude = ("request_id","request_create_date","request_update_date",)

        widgets = {
            "request_name": forms.TextInput(
                attrs={
                    "class": "form__field",
                    "placeholder": "Organisation Name",
                    "required": True,
                }
            ),
            "request_email": forms.EmailInput(
                attrs={
                    "class": "form__field",
                    "placeholder": "Organisation Email",
                    "required": True,
                }
            ),
            "request_tel": forms.TextInput(
                attrs={
                    "class": "form__field",
                    "placeholder": "Organisation Phone Number",
                    "required": True,
                }
            ),
            "request_pilot": forms.Select(
                attrs={
                    "class": "form__field",
                    "placeholder": "Select Pilot",
                    "required": True,
                }
            ),
            "request_job_type": forms.Select(
                attrs={
                    "class": "form__field",
                    "empty_label": "Select Job Type",
                    "required": True,
                }
            ),
            "request_country": forms.Select(
                attrs={
                    "class": "form__field",
                    "placeholder": "Organisation Country",
                    "required": True,
                }
            ),
            "request_city": forms.Select(
                attrs={
                    "class": "form__field",
                    "placeholder": "Organisation City",
                    "required": True,
                }
            ),
            "request_extra_information": forms.Textarea(
                attrs={
                    "class": "form__field",
                    "placeholder": "Any extra information you need to tell us?",
                    "required": True,
                }
            ),
        }

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields["city"].queryset = City.objects.none()

            if "country" in self.data:
                try:
                    country_id = int(self.data.get("country"))
                    self.fields["city"].queryset = City.objects.filter(
                        country_id=country_id
                    ).order_by("name")
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields["city"].queryset = self.instance.country.city_set.order_by(
                    "name"
                )
            # filter the request_pilot dropdown to only show pilots
            self.fields["request_pilot"].queryset = Profile.user.objects.filter(
                user_type="Pilot"
            )
