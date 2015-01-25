# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.http import *

from contest.forms import *
from contest.models import *
from contest.crawler import *
from contest.email_reply import *

import json


def feedback(request, contest_id):
    feedbackform = FeedbackForm(
        request.POST,
        instance=Feedback(cid=contest_id))
    if feedbackform.is_valid():
        feedbackform.save()
        return render(
            request,
            'form.html',
            {'form': FeedbackForm(), 'message': '您已成功傳送訊息'})
    else:
        return render(request, 'form.html', {'form': feedbackform})


def signup(request, contest_id):
    contest_data = Contest.objects.filter(cid=contest_id).first()
    signupform = SignUpForm(request.POST, instance=SignUp(cid=contest_id))
    if signupform.is_valid():
        signupform.save()
        signup_reply(contest_data, request)
        return render(
            request,
            'form.html',
            {'form': SignUpForm(), 'message': '您已成功傳送訊息'})
    else:
        return render(request, 'form.html', {'form': signupform})


def clarification(request, contest_id):
    contest_data = Contest.objects.filter(cid=contest_id).first()
    clarificationform = ClarificationForm(
        request.POST,
        instance=Clarification(
            asker='',
            cid=contest_id,
            reply='No reply yet.'))
    if clarificationform.is_valid() and contest_data:
        clar = clarificationform.save(commit=False)
        clar.asker = 'Anonymous' if clar.asker == '' else clar.asker
        clar.save()
        clarification_reply(contest_data, request)
        return render(
            request,
            'form.html',
            {'form': ClarificationForm(), 'message': '您已成功傳送訊息'})
    else:
        return render(request, 'form.html', {'form': clarificationform})


def contest(request, contest_id):
    contest_data = get_object_or_404(Contest, cid=contest_id)
    render_data = {}

    if contest_data:
        if request.is_ajax():
            data = {
                'scoreboard_table': str(get_scoreboard(contest_data)),
                'clarification_table': str(get_clarification(contest_data))
            }
            return HttpResponse(json.dumps(data))

        render_data['signup_form'] = SignUpForm()
        render_data['feedback_form'] = FeedbackForm()
        render_data['clarification_form'] = ClarificationForm()

        render_data['problem_table'] = get_problem(contest_data)
        render_data['contest_data'] = contest_data

    return render(request, 'contest.html', render_data)


def rank(request, contest_id):
    contest_data = get_object_or_404(Contest, cid=contest_id)
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
                prizes += [{'place': place,
                            'ojid': user.nthu_oj_id,
                            'email': user.email,
                            'name': user.name}]
                place += 1

        render_data['prizes'] = prizes
        render_data['scoreboard_table'] = table
    return render(request, 'rank.html', render_data)


def competitor(request, contest_id):
    contest_data = get_object_or_404(Contest, cid=contest_id)
    render_data = {}

    return render(request, 'competitor.html', render_data)
