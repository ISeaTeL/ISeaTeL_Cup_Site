# -*- coding: utf-8 -*-

from django import forms

from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

from users.models import *
 
class UserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the same password as above, for verification."))


    email = forms.EmailField(label='電子信箱', max_length=100, help_text=_("Required."),
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
 
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
