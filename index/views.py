from django.shortcuts import render
from index.models import Bulletin, Visited

# Create your views here.

def home(request):
    bulletin_content = Bulletin.objects.all().order_by('-time')

    return render(request, "base.html", {'bulletin': bulletin_content})

