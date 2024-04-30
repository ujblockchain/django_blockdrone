from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


from users.forms import CustomUserChangeForm
from .models import JobType, Profile, City, JobRequestModel, JobReviewModel

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
    request_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form__field",
                "placeholder": "Organisation Name",
            }
        ),
    )
    request_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form__field",
                "placeholder": "Organisation Email",
            }
        ),
    )
    request_tel = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form__field",
                "placeholder": "Organisation Phone Number",
            }
        ),
    )
    request_pilot = forms.CharField(
        required=True, widget=forms.Select(attrs={"class": "form__field"})
    )
    request_job_type = forms.ModelChoiceField(
        queryset=JobType.objects.all(),
        initial="pp",
        widget=forms.Select(
            attrs={
                "class": "form__field",
            },
        ),
    )
    # request_country = forms.CharField(
    #     required=True,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form__field",
    #         }
    #     ),
    # )
    request_city = forms.CharField(
        required=True,
        empty_value="Organisation City",
        widget=forms.Select(
            attrs={
                "class": "form__field",
            }
        ),
    )
    request_extra_information = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form__field"}),
    )

    class Meta:
        model = JobRequestModel
        exclude = (
            "request_id",
            "request_job_type",
            "request_create_date",
            "request_update_date",
        )

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields["city"].queryset = City.objects.none()
            self.fields["request_pilot"].initial = "Select a pilot"

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

        widgets = {
            "request_country": forms.Select(
                attrs={
                    "class": "form__field",
                }
            )
        }

    def clean_request_pilot(self):
        get_pilot = self.cleaned_data.get("request_pilot", "")
        if get_pilot != "":
            print(f"something is wring {get_pilot}")
            pilot_instance = Profile.objects.get(user__id=get_pilot)
            print(f"{type(pilot_instance)}")
        else:
            raise ValidationError(
                f"This field got an invalid choice - {get_pilot}",
                code="request_pilot",
            )
        return pilot_instance

    def clean_request_city(self):
        # init
        city_instance = ""
        get_user_city_id = self.cleaned_data.get("request_city", "")

        if get_user_city_id != "" and get_user_city_id != "Organisation City":
            # print(get_user_city_id)
            city_instance = City.objects.get(id=get_user_city_id)
        else:
            raise ValidationError("This field is required", code="request_city")
        return city_instance


class JobReviewForm(forms.ModelForm):

    class Meta:
        model = JobReviewModel
        exclude = (
            "review_id",
            "review_create_date",
            "review_pilot",
        )
        RATING_CHOICES = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
        widgets = {
            "review_job": forms.TextInput(
                attrs={
                    "class": "form__field",
                    "placeholder": "Job ID",
                    "required": True,
                }
            ),
            # "review_pilot": forms.Select(
            #     attrs={
            #         "class": "form__field",
            #         "required": True,
            #     }
            # ),
            "review_rating": forms.Select(
                choices=RATING_CHOICES,
                attrs={
                    "class": "form__field form__field--range",
                    "default": RATING_CHOICES[1],
                },
            ),
            "review_comment": forms.Textarea(
                attrs={
                    "class": "form__field form__field--textarea",
                    "placeholder": "Leave a review...",
                }
            ),
        }

        def __init__(self, *args, **kwargs) -> None:

            super().__init__(*args, **kwargs)

            self.fields["review_pilot"].queryset = Profile.user.objects.filter(
                user_type="Pilot"
            )
