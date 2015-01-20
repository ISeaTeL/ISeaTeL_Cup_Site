# -*- coding: utf-8 -*-

from django.shortcuts import *
from django.http import *

from sudo.forms import *
from sudo.models import *

import hashlib
# Create your views here.
def change(request, url_hash):
    sudo = get_object_or_404(Sudo, url_hash=url_hash)
    msg = '欲修改資料者可用此url修改'
    if sudo:
        if request.method == 'POST':
            sudoform = SudoForm(request.POST, instance=sudo)
            if sudoform.is_valid():
                sudo = sudoform.save()
                sudo.save()
                msg = '修改成功'
            else:
                return render(request, 'sudo.html', {'sudoform': sudoform})
    
    return render(request, 'sudo.html', {'sudoform': SudoForm(instance=sudo), 'msg': msg})

def create(request):
    if request.method == 'POST':
        sudoform = SudoForm(request.POST)
        if sudoform.is_valid():
            sudo = sudoform.save()
            sudo.url_hash = hashlib.md5(sudo.email).hexdigest()
            sudo.save()
            return HttpResponseRedirect('/sudo/change/%s' % sudo.url_hash)
        else:
            return render(request, 'sudo.html', {'sudoform': sudoform})

    return render(request, 'sudo.html', {'sudoform': SudoForm()})

def special_change(request, url_hash):
    sudo = get_object_or_404(Sudo, url_hash=url_hash)
    msg = '欲修改資料者可用此url修改'
    if sudo:
        if request.method == 'POST':
            sudoform = SpecialSudoForm(request.POST, instance=sudo)
            if sudoform.is_valid():
                sudo = sudoform.save()
                sudo.save()
                msg = '修改成功'
            else:
                return render(request, 'sudo.html', {'sudoform': sudoform})
    
    return render(request, 'sudo.html', {'sudoform': SpecialSudoForm(instance=sudo), 'msg': msg})

def special_create(request):
    if request.method == 'POST':
        sudoform = SpecialSudoForm(request.POST)
        if sudoform.is_valid():
            sudo = sudoform.save()
            sudo.url_hash = hashlib.md5(sudo.email).hexdigest()
            sudo.save()
            return HttpResponseRedirect('/sudo/special_change/%s' % sudo.url_hash)
        else:
            return render(request, 'sudo.html', {'sudoform': sudoform})

    return render(request, 'sudo.html', {'sudoform': SpecialSudoForm()})