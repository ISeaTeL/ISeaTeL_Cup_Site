from django.shortcuts import *
from django.http import *

# Create your views here.
def home(request):
	return HttpResponse('gg')