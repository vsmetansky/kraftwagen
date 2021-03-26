from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from showroom.utils import CHAR_FIELD_DEFAULT_SIZE_M


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, required=True)
    second_name = forms.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, required=False, help_text='Optional')
    surname = forms.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, required=True)

    address = forms.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, required=False, help_text='Optional')
    phone = forms.IntegerField(required=True, help_text='Cellular phone number')
    passport = forms.IntegerField(required=True, help_text='Passport number')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'surname', 'address', 'phone', 'passport')
