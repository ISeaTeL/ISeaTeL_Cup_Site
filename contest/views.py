# -*- coding: utf-8 -*-

from django.shortcuts import render
from contest.models import Clarification, Contest, SignUp, Dictionary
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.mail import send_mail
from django.conf import settings

import random
import urllib2
import re
from bs4 import BeautifulSoup

# Create your views here.
INCOMING_HTML = '<h3>Incoming.</h3>'
PAGE_NOT_FOUND = '<div style="height:50%"></div><center><h1>QAQ<br>What have you done...</h1></center>'

def fetch_table(url):
    try:
        response = urllib2.urlopen(url, timeout=1)
        html = response.read()
        soup = BeautifulSoup(html)
        table = str(soup.find_all('table')[1])
        Dictionary.getDict('url2table')[url] = table
        return table
    except:
        m = Dictionary.getDict('url2table')
        if url in m.keys():
            return m[url]
        else:
            return 'ＯＪ 炸裂了'


def get_scoreboard(contest_data):
    if(contest_data.status=='incoming'):
        return INCOMING_HTML

    url = contest_data.scoreboard_url
    html = fetch_table(url)
    html = re.sub('AContestant', random.choice(['CKL', 'Chuck Lee', 'AContestant']), html)
    html = re.sub('<td>', '<td class="text-center">', html)
    html = re.sub('<th>', '<th class="text-center">', html)
    html = re.sub('0/[0-9]', '<div class="btn-danger text-center">0/1</div>', html)
    html = re.sub('1/1', '<div class="btn-success text-center">1/1</div>', html)
    html = re.sub('4/4', '<div class="btn-success text-center">4/4</div>', html)
    return html

def get_solution_html(idx, base_url):
    prob = 'p' + str(unichr(ord('a')+idx-1))
    return '<td><a class="href-popup-link" href="' + base_url + prob +'.html">' + prob.upper() + '</a></td>'

def get_problem(contest_data):
    if(contest_data.status=='incoming'):
        return INCOMING_HTML

    url = contest_data.problem_url
    html = fetch_table(url)
    soup = BeautifulSoup(html)
    for a in soup.find_all('a'):
        a['href'] = 'http://140.114.86.238/' + a['href']
        a['class'] = 'href-popup-link'
    if contest_data.status=='ended' and 'http' in contest_data.solution_url:
        trs = soup.find_all('tr')
        for idx, tr in enumerate(trs):
            if idx:
                tr.append(BeautifulSoup(get_solution_html(idx, contest_data.solution_url)))
            else:
                tr.append(BeautifulSoup('<th>Solution</th>'))
    return str(soup)

from django.core.mail import EmailMultiAlternatives

def sign_up_reply(contest_data, request):
    render_data = {}
    render_data["register_name"] = request.POST['nthu_oj_id']
    render_data["contest_name"] = contest_data.title
    render_data["contest_date"] = contest_data.date
    render_data["contest_cid"] = contest_data.cid
    
    reply_title = '您已成功註冊 ' + contest_data.date 
    reply_content = str(render(request, "reply_signup.html", render_data)).replace('Content-Type: text/html; charset=utf-8', '')
    
    from_email, to_email = settings.EMAIL_HOST_USER, request.POST['email']
    msg = EmailMultiAlternatives(reply_title, reply_content, from_email, [to_email])
    msg.attach_alternative(reply_content, "text/html")
    msg.send()
    
def get_status(contest_data):
    status = contest_data.status
    if status=='ended' or status=='running':
        return '<a class="btn btn-primary btn-lg" onclick="'+ "$('#p3').click()" + '" data-toggle="tab">'+status+'</a>'
    else:
        return '<a href="#signup-popup" class="open-popup-link btn btn-primary btn-lg">Sign Up!!</a>'

def contest(request, contest_id):    
    magic_num = 7777
    magic_mod = 2345678

    contest_data = Contest.objects.filter(cid=contest_id).first()
    render_data = {}

    if contest_data:
        if request.method == 'POST':
            if all(x in request.POST for x in ['signup', 'nthu_oj_id', 'name', 'email', 'message']):
                try:
                    SignUp.objects.create(nthu_oj_id=request.POST['nthu_oj_id'], name=request.POST['name'], email=request.POST['email'], message=request.POST['message'], cid=contest_id)
                    sign_up_reply(contest_data, request)
                except:
                    pass
            
            if all(x in request.POST for x in ['token', 'asker', 'question']):
                if request.POST['asker'] != '' and int(request.POST['token']) % magic_mod == magic_num:
                    Clarification.objects.create(question=request.POST['question'], asker=request.POST['asker'], cid=contest_id)
                else:
                    Clarification.objects.create(question=request.POST['question'], cid=contest_id)
                # when clarification is sent, notify admins
                try:
                    send_mail('Clarification @ contest ' + str(contest_id), 
                        'asker: %s:\nquestion : %s\n' % (request.POST['asker'], request.POST['question']), 
                        settings.EMAIL_HOST_USER, 
                        [email[1] for email in settings.ADMINS])
                except:
                    print 'send_email error'

            return HttpResponseRedirect(reverse("contest.views.contest", args=(contest_id,)))

        render_data["clarification_table"] = Clarification.objects.filter(cid=contest_id).order_by('-time')
        render_data["scoreboard_table"] = get_scoreboard(contest_data)
        render_data["problem_table"] = get_problem(contest_data)
        render_data["token"] = random.getrandbits(128)*magic_mod + magic_num
        render_data["head_title"] = contest_data.title
        render_data["head_content"] = contest_data.content
        render_data["head_status"] = get_status(contest_data)
        return render(request, "contest.html", render_data)
    else:
        return HttpResponseNotFound(PAGE_NOT_FOUND)


def rank(request, contest_id):    
    contest_data = Contest.objects.filter(cid=contest_id).first()
    render_data = {}

    if contest_data:
        signups = SignUp.objects.filter(cid=contest_id)
        table = get_scoreboard(contest_data)
        soup = BeautifulSoup(table)

        oj_ids = [str(x.nthu_oj_id) for x in signups]
        rank_list = []

        for tr in soup.find_all('tr'):
            tds = tr.find_all('td')
            if tds:
                oj_id = tds[0].string
                rank_list += [str(oj_id)]

        prizes = []
        place = 1
        for x in rank_list:
            if x in oj_ids:
                user = signups.filter(nthu_oj_id__iexact=x).first()
                prizes += [{ 'place': place,
                            'ojid': user.nthu_oj_id,
                            'email': user.email,
                            'name': user.name}]
                place += 1        

        render_data['prizes'] = prizes
        render_data["scoreboard_table"] = table
        return render(request, "rank.html", render_data)
    else:
        return HttpResponseNotFound(PAGE_NOT_FOUND)

