# -*- coding: utf-8 -*-

from django.shortcuts import render
from contest.models import Clarification, Contest, SignUp
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

import random
import urllib2
import re
from bs4 import BeautifulSoup

# Create your views here.
INCOMING_HTML = '<h3>Incoming.</h3>'

def fetch_table(url):
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        return str(soup.find_all('table')[1])
    except:
        return 'OJ 炸裂了'

def get_scoreboard(contest_data):
    if(contest_data.status=='incoming'):
        return INCOMING_HTML

    url = contest_data.scoreboard_url
    html = fetch_table(url)
    html = re.sub('AContestant', random.choice(['清大最強 CKL', 'Chunk Lee', '清大最強 Chuck Lee', 'AContestant']), html)
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
    
    reply_title = 'You have succeeded signing up ISeaTeL Cup on ' + contest_data.date 
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
                    #return HttpResponse('<html><head><meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"><style type="text/css"></style></head><body><h1>QAQ</h1><p>Please provide valid data.<br><a href="/contest/' + str(contest_id) + '">Go back</a></p></body></html>')
            
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
        return HttpResponse('<html><head><meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"><style type="text/css"></style></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>')

