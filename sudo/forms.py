# -*- coding: utf-8 -*-

from sudo.models import *
from django.forms import ModelForm
from django import forms

class SudoForm(ModelForm):
    class Meta:
        model = Sudo
        fields = ['name', 'email', 'schedule']

    name = forms.CharField(label='Name', max_length=200,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    
    email = forms.CharField(label='E-Mail', max_length=200,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    schedule = forms.CharField(label='', initial='0'*91,
        widget=forms.HiddenInput(
            attrs={'id': 'schedule'}))
