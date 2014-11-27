from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from clarification.models import Bulletin, Clarification

# Create your views here.

def home(request):
    if request.method == 'POST':
        if 'question' in request.POST:
            q = request.POST['question']
        else:
            q = ''
        if request.POST['asker'] != '':
            Clarification.objects.create(question=q, asker=request.POST['asker'])
        else:
            Clarification.objects.create(question=q)
        return HttpResponseRedirect(reverse("clarification.views.home"))

    bulletin_content = Bulletin.objects.all()
    clarification_content = Clarification.objects.all()


    return render(request, "base.html", {'bulletin': bulletin_content, 'clarification': clarification_content})

