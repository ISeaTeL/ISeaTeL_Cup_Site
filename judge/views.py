from django.shortcuts import render
#from judge.models import *

from django import forms
import problem_judge
import random
# Create your models here.
CHOICES=(('select1','select 1'), ('select2','select 2'),)

class SubmitForm(forms.Form):
    LANG_CHOICES = (
        ('GCC', 'GCC'),
        ('G++', 'G++'),
    )
    language = forms.ChoiceField(widget=forms.RadioSelect, choices=LANG_CHOICES, label='Language')
    code = forms.CharField(label='Code', max_length=10000,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 11,
            'placeholder': 'your code',
            'id': 'code_editor'}))
    form_name = forms.CharField(label='', initial='Submit',
        widget=forms.HiddenInput())


# Create your views here.

def home(request):
	init_code = '''#include <cstdio>
#include <cstdlib>
// This is a god damn A+B problem
int main() {
    int x, y;
    while (scanf(\"%d%d\", &x, &y) > 0) {
        printf(\"%d\", x + y);
        putchar(10);
    }
    return 0;
}
'''
	if request.method == 'POST':
		submitform = SubmitForm(request.POST)
		if submitform.is_valid():
			code = submitform.cleaned_data['code']
			lang = submitform.cleaned_data['language']
			judge_result = 'fuck'
			try:
				judge_result = problem_judge.run(random.randint(1,10000),1,code,lang,1000,32000)
				print judge_result
			except Exception as e:
				print 'judge GG'
				print e
			return render(request, 'judge.html', {'form': submitform, 'message': str(judge_result)})
		else:
			return render(request, 'judge.html', {'form': submitform})
	return render(request, 'judge.html', {'form': SubmitForm(initial={'code': init_code, 'language': 'G++'})})
