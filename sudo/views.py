# -*- coding: utf-8 -*-

from django.shortcuts import *
from django.http import *

from sudo.forms import *
from sudo.models import *

import hashlib
import json

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from threading import Thread
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def signup_reply(sudo, request):
    render_data = {}
    render_data["name"] = sudo.name
    render_data["url"] = 'http://iseatel.org/sudo/change/%s' % sudo.url_hash

    try:
        reply_title = '您已成功填寫 Web 讀書會時段調查表'
        reply_content = str(render(request, "web_reply_signup.html", render_data)).replace('Content-Type: text/html; charset=utf-8', '')

        from_email, to_email = settings.EMAIL_HOST_USER, sudo.email
        msg = EmailMultiAlternatives(reply_title, reply_content, from_email, [to_email])
        msg.attach_alternative(reply_content, "text/html")
        Thread(target=msg.send, args=()).start()
    except:
        print 'sned_email error'

def change(request, url_hash, g):
    sudo = get_object_or_404(Sudo, url_hash=url_hash)
    msg = ''
    F = SudoForm if g == '' else SpecialSudoForm
    if sudo:
        if request.method == 'POST':
            sudoform = F(request.POST, instance=sudo)
            if sudoform.is_valid():
                sudo = sudoform.save()
                sudo.save()
                msg = '修改成功'
            else:
                return render(request, 'sudo.html', {'sudoform': sudoform})
        if sudo.count == 0:
            msg = '<script>alert("您已成功傳送表單，欲修改資料者可用此url修改。確認信已寄至%s")</script>' % sudo.email
        sudo.count += 1
        sudo.save()
    return render(request, 'sudo.html', {'sudoform': F(instance=sudo), 'msg': msg})

def create(request, g):
    F = SudoForm if g == '' else SpecialSudoForm
    if request.method == 'POST':
        sudoform = F(request.POST)
        if sudoform.is_valid():
            sudo = sudoform.save()
            sudo.url_hash = hashlib.md5(sudo.email).hexdigest()
            sudo.save()
            signup_reply(sudo, request)
            return HttpResponseRedirect('/sudo/change/%s' % sudo.url_hash)
        else:
            return render(request, 'sudo.html', {'sudoform': sudoform})
    msg = ''
    return render(request, 'sudo.html', {'sudoform': F(), 'msg': msg})

def query_schedule(request):
    sudos = Sudo.objects.all()
    print sudos
    sums = [0]*91
    sums_total = 0
    if sudos:
        for schedule in [sudo.schedule for sudo in sudos]:
            sums_total += 1
            for i in range(0, 91):
                sums[i] += int(schedule[i])
    return render(request, 'sums.html', {'sums': json.dumps(sums), 'sums_total': sums_total})
