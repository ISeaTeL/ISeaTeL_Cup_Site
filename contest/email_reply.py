# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.conf import settings

from threading import Thread
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def signup_reply(contest_data, request):
    render_data = {}
    render_data["register_name"] = request.POST['nthu_oj_id']
    render_data["contest_name"] = contest_data.title
    render_data["contest_date"] = contest_data.date
    render_data["contest_cid"] = contest_data.cid
    try:
        reply_title = '您已成功註冊 ' + contest_data.date 
        reply_content = str(render(request, "reply_signup.html", render_data)).replace('Content-Type: text/html; charset=utf-8', '')
        
        from_email, to_email = settings.EMAIL_HOST_USER, request.POST['email']
        msg = EmailMultiAlternatives(reply_title, reply_content, from_email, [to_email])
        msg.attach_alternative(reply_content, "text/html")
        Thread(target=msg.send, args=()).start()
    except:
        print 'sned_email error'

def clarification_reply(contest_data, request):
    try:
        Thread(target=send_mail, 
            args=('Clarification @ contest ' + str(contest_data.cid), 
                'asker: %s:\nquestion : %s\n' % (request.POST['asker'], request.POST['question']), 
                settings.EMAIL_HOST_USER, 
                [email[1] for email in settings.ADMINS])).start()
    except:
        print 'send_email error'

