from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from clarification.models import Bulletin, Clarification
import random
# Create your views here.

def home(request):
    magic_num = 7777
    magic_mod = 2345678
    if request.method == 'POST':
        if 'question' in request.POST:
            q = request.POST['question']
        else:
            q = ''
        if request.POST['asker'] != '' and int(request.POST['token']) % 2345678 == 7777:
            Clarification.objects.create(question=q, asker=request.POST['asker'])
        else:
            Clarification.objects.create(question=q)
        return HttpResponseRedirect(reverse("clarification.views.home"))

    bulletin_content = Bulletin.objects.all().order_by('-time')
    clarification_content = Clarification.objects.all().order_by('-time')


    return render(request, "base.html", {'bulletin': bulletin_content, 'clarification': clarification_content, 'token': random.getrandbits(128)*2345678 + 7777})

