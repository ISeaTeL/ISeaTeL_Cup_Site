from django.shortcuts import *
from django.http import *
from django import forms
import random
from judge import judge
from problem.models import *
from contest.crawler import *

# Create your models here.
CHOICES=(('select1','select 1'), ('select2','select 2'),)

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

def problem(request, problem_id):
    problem_data = Problem.objects.filter(pid=problem_id).first()
    render_data = {}



    if problem_data:
        render_data['problem'] = problem_data

        if request.method == 'POST':
            submitform = SubmitForm(request.POST)
            render_data['form'] = submitform
            if submitform.is_valid():
                code = submitform.cleaned_data['code']
                lang = submitform.cleaned_data['language']
                judge_result = 'GG'
                try:
                    judge_result = judge.run(random.randint(1,10000),1,code,lang,1000,32000)
                    print judge_result
                except:
                    print 'judge GG'
                render_data['message'] = str(judge_result)
                return render(request, 'show_problem.html', render_data)
            else:
                return render(request, 'show_problem.html', render_data)

        render_data['form'] = SubmitForm(initial={'code': init_code, 'language': 'G++'})
        return render(request, 'show_problem.html', render_data)
    else:
        return HttpResponseNotFound(PAGE_NOT_FOUND)
