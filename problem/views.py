from django.shortcuts import *
from django.http import *
from django import forms
import random
from oj_judge import problem_judge
from oj_judge.models import *
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
                sid = JudgeResult.objects.count()+1
                try:
                    judge_result = problem_judge.run(sid,
                        problem_data.pid,
                        code,lang,
                        problem_data.time_limit,
                        problem_data.mem_limit)
                    print judge_result
                except:
                    judge_result={
                        'result': 'Judge Error',
                        'status': 0,
                        'time': 0,
                        'memory': 0,
                        'message': ''}
                    print 'judge GG'
                judge_result['username'] = str(request.user.username)
                render_data['message'] = str(judge_result)

                JudgeResult.objects.create(pid=problem_id, sid=sid, username=judge_result['username'],
                    result=judge_result['result'], time=judge_result['time'], 
                    memory=judge_result['memory'], status=judge_result['status'], 
                    message=judge_result['message'], language=lang)
                
                return redirect('/problem/status')
                #return render(request, 'show_problem.html', render_data)
            else:
                return render(request, 'show_problem.html', render_data)

        render_data['form'] = SubmitForm(initial={'code': init_code, 'language': 'G++'})
        return render(request, 'show_problem.html', render_data)
    else:
        return HttpResponseNotFound(PAGE_NOT_FOUND)

def status(request):
    results = JudgeResult.objects.order_by('-submit_time')
    return render(request, 'status.html', {'results': results})
