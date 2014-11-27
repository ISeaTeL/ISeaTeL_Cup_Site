from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
from clarification.models import Bulletin, Clarification

# Create your views here.

def home(request):
    if request.method == 'POST':
        if 'question' in request.POST:
            q = request.POST['question']
        else:
            q = ''
        Clarification.objects.create(question=q, asker=request.POST['asker'])

    bulletin_content = Bulletin.objects.all()
    clarification_content = Clarification.objects.all()


    return render(request, "base.html", {'bulletin': bulletin_content, 'clarification': clarification_content})

