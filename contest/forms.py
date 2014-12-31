# -*- coding: utf-8 -*-

from contest.models import *
from django.forms import ModelForm
from django import forms

class ClarificationForm(ModelForm):
    class Meta:
        model = Clarification
        fields = ['asker', 'question']

    asker = forms.CharField(label='Name', max_length=100, required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 
            'placeholder': 'Anonymous'}))
    
    question = forms.CharField(label='Message', max_length=1000,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3,
            'placeholder': '你的疑問'}))
    form_name = forms.CharField(label='', initial='ClarificationForm',
        widget=forms.HiddenInput())
    

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ['nthu_oj_id', 'name', 'email', 'message']
    nthu_oj_id = forms.CharField(label='NTHU OJ ID', max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 
            'placeholder': 'NTHU OJ ID'}))
    name = forms.CharField(label='Name', max_length=100, required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 
            'placeholder': '你的暱稱，也可以留空'}))
    email = forms.EmailField(label='E-mail', max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 
            'placeholder': '請留下常用的信箱，讓我們能聯絡到你！'}))
    message = forms.CharField(label='Message', max_length=100, required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3,
            'placeholder': '其他想說的東西\n一些雜七雜八的東西都可以說'}))
    form_name = forms.CharField(label='', initial='SignUpForm',
        widget=forms.HiddenInput())

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
    name = forms.CharField(label='Name', max_length=100, required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 
            'placeholder': '您的稱號（預設是匿名）'}))
    email = forms.EmailField(label='E-mail', max_length=100, required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 
            'placeholder': '如果您希望我們回信，請留下常用的信箱'}))
    message = forms.CharField(label='Message', max_length=500,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3,
            'placeholder': '請留下您對本場賽事的意見'}))
    form_name = forms.CharField(label='', initial='FeedbackForm',
        widget=forms.HiddenInput())
