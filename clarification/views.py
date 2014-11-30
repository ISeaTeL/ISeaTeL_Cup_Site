from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from clarification.models import Bulletin, Clarification, Visited
import random
# Create your views here.

def home(request):
    magic_num = 7777
    magic_mod = 2345678

    if request.method == 'POST':
        if not all(x in request.POST for x in ['token', 'asker', 'question']):
            return HttpResponseRedirect(reverse("clarification.views.home"))
        
        q = request.POST['question']
        if request.POST['asker'] != '' and int(request.POST['token']) % magic_mod == magic_num:
            Clarification.objects.create(question=q, asker=request.POST['asker'])
        else:
            Clarification.objects.create(question=q)
        return HttpResponseRedirect(reverse("clarification.views.home"))

    bulletin_content = Bulletin.objects.all().order_by('-time')
    clarification_content = Clarification.objects.all().order_by('-time')
    
    if Visited.objects.count() == 0:
        v = Visited.objects.create(hits=0)
        v.save()

    hits = Visited.objects.first()
    hits.hits += 1
    hits.save()

    return render(request, "base.html", {'bulletin': bulletin_content, 'clarification': clarification_content,
    'token': random.getrandbits(128)*magic_mod + magic_num, 'hits': hits.hits})

