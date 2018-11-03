from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django_registration import validators
from django_registration.forms import RegistrationForm


class CustomRegistrationForm(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` that enforces case-insensitive unique usernames
    and unique email addresses.
    """
    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.fields[User.USERNAME_FIELD].validators.append(MinLengthValidator(3))
        self.fields[User.USERNAME_FIELD].validators.append(MaxLengthValidator(20))

        self.fields[User.USERNAME_FIELD].validators.append(
            validators.CaseInsensitiveUnique(
                User, User.USERNAME_FIELD,
                validators.DUPLICATE_USERNAME
            )
        )

        email_field = User.get_email_field_name()
        self.fields[email_field].validators.append(
            validators.CaseInsensitiveUnique(
                User, email_field,
                validators.DUPLICATE_EMAIL
            )
        )

        self.fields['username'].help_text = "Required. 3-20 characters. Letters, digits and @/./+/-/_ only."
        self.fields['password1'].help_text = "Your password must contain at least 8 characters, cannot be entirely numeric, and cannot be too similar to your other personal information or a commonly used password."


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].help_text = "Your password must contain at least 8 characters and can't be too similar to your other personal information, a commonly used password, or entirely numeric."
