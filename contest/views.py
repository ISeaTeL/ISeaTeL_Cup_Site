from django.shortcuts import render
from contest.models import Clarification, Contest
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

import random
import urllib2
import re
from bs4 import BeautifulSoup

# Create your views here.
def get_solution(url):
    return '<iframe id="solution_frame" src="'+url+'pa.html" width="100%" height="200%">'

def fetch_table(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    return soup.find_all('table')[1]

def get_scoreboard(url):
    rawData = str(fetch_table(url))
    rawData = re.sub('<td>', '<td class="text-center">', rawData)
    rawData = re.sub('<th>', '<th class="text-center">', rawData)
    rawData = re.sub('0/[0-9]', '<div class="btn-danger text-center">0/1</div>', rawData)
    rawData = re.sub('1/1', '<div class="btn-success text-center">1/1</div>', rawData)
    rawData = re.sub('4/4', '<div class="btn-success text-center">4/4</div>', rawData)
    return rawData


def get_problem(url):
    rawData = str(fetch_table(url))
    rawData = rawData.replace('problem', 'http://140.114.86.238/problem')
    return rawData


def contest(request, contest_id):
    magic_num = 7777
    magic_mod = 2345678

    contest_data = Contest.objects.filter(cid=contest_id).first()
    render_data = {}

    if contest_data:
        if request.method == 'POST':
            if all(x in request.POST for x in ['token', 'asker', 'question']):
                if request.POST['asker'] != '' and int(request.POST['token']) % magic_mod == magic_num:
                    Clarification.objects.create(question=request.POST['question'], asker=request.POST['asker'], cid=contest_id)
                else:
                    Clarification.objects.create(question=request.POST['question'], cid=contest_id)
            return HttpResponseRedirect(reverse("contest.views.contest", args=(contest_id,)))

        render_data["clarification_table"] = Clarification.objects.filter(cid=contest_id).order_by('-time')
        render_data["scoreboard_table"] = get_scoreboard(contest_data.scoreboard_url)
        render_data["solution_table"] = get_solution(contest_data.solution_url)
        render_data["problem_table"] = get_problem(contest_data.problem_url)
        render_data["token"] = random.getrandbits(128)*magic_mod + magic_num
        render_data["head_title"] = contest_data.title
        render_data["head_content"] = contest_data.content
        render_data["head_status"] = contest_data.status

        return render(request, "contest.html", render_data)
    else:
        return HttpResponse('<html><head><meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"><style type="text/css"></style></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>')

