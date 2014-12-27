# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import *

from contest.models import *
from contest.crawler import *
from contest.email_reply import *

import json

def contest(request, contest_id):    
    contest_data = Contest.objects.filter(cid=contest_id).first()
    render_data = {}

    if contest_data:
        if request.is_ajax() and 'email' not in request.POST and 'asker' not in request.POST:
            data = {
                'scoreboard_table': str(get_scoreboard(contest_data)),
                'clarification_table': str(get_clarification(contest_data))
            }
            return HttpResponse(json.dumps(data))

        if request.method == 'POST' and 'form_name' in request.POST:
            if request.POST['form_name'] == 'SignUpForm':
                # create a form instance and populate it with data from the request:
                signupform = SignUpForm(request.POST, instance=SignUp(cid=contest_id))
                # check whether it's valid:
                if signupform.is_valid():
                    signupform.save()
                    signup_reply(contest_data, request)

                    return render(request, 'form.html', {'form': SignUpForm(), 'message': '您已成功傳送訊息'})
                else:
                    return render(request, 'form.html', {'form': signupform})
            if request.POST['form_name'] == 'FeedbackForm':
                # create a form instance and populate it with data from the request:
                feedbackform = FeedbackForm(request.POST, instance=Feedback(cid=contest_id))
                # check whether it's valid:
                if feedbackform.is_valid():
                    feedbackform.save()
                    return render(request, 'form.html', {'form': FeedbackForm(), 'message': '您已成功傳送訊息'})
                else:
                    return render(request, 'form.html', {'form': feedbackform})
            if request.POST['form_name'] == 'ClarificationForm':
                clarificationform = ClarificationForm(request.POST, instance=Clarification(asker='', cid=contest_id, reply='No reply yet.'))
                if clarificationform.is_valid():
                    clar = clarificationform.save(commit=False)
                    clar.asker = 'Anonymous' if clar.asker == '' else clar.asker
                    clar.save()
                    clarification_reply(contest_data, request)
                    return render(request, 'form.html', {'form': ClarificationForm(), 'message': '您已成功傳送訊息'})
                else:
                    return render(request, 'form.html', {'form': clarificationform})

        render_data['signup_form'] = SignUpForm()
        render_data['feedback_form'] = FeedbackForm()
        render_data['clarification_form'] = ClarificationForm()

        render_data['problem_table'] = get_problem(contest_data)
        render_data['head_title'] = contest_data.title
        render_data['head_content'] = contest_data.content
        render_data['head_status'] = get_status(contest_data)
        return render(request, 'contest.html', render_data)

    else:
        return HttpResponseNotFound(PAGE_NOT_FOUND)


def rank(request, contest_id):    
    contest_data = Contest.objects.filter(cid=contest_id).first()
    render_data = {}

    if contest_data:
        signups = SignUp.objects.filter(cid=contest_id)
        table = get_scoreboard(contest_data)
        soup = BeautifulSoup(table)

        oj_ids = [str(x.nthu_oj_id.lower()) for x in signups]
        rank_list = []

        for tr in soup.find_all('tr'):
            tds = tr.find_all('td')
            if tds:
                oj_id = tds[0].string
                rank_list += [str(oj_id)]

        prizes = []
        place = 1
        for x in rank_list:
            if x.lower() in oj_ids:
                user = signups.filter(nthu_oj_id__iexact=x).first()
                prizes += [{ 'place': place,
                            'ojid': user.nthu_oj_id,
                            'email': user.email,
                            'name': user.name}]
                place += 1        

        render_data['prizes'] = prizes
        render_data['scoreboard_table'] = table
        return render(request, 'rank.html', render_data)
    else:
        return HttpResponseNotFound(PAGE_NOT_FOUND)

def competitor(request, contest_id):    
    contest_data = SignUp.objects.filter(cid=contest_id)
    render_data = {}

    if contest_data:
        render_data['competitor'] = contest_data
        return render(request, 'competitor.html', render_data)
    else:
        return HttpResponseNotFound(PAGE_NOT_FOUND)
