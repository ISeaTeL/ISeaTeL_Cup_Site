# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


from contest.models import *

from bs4 import BeautifulSoup

import random
import urllib2
import re
import sys

INCOMING_HTML = '<center><h1>Wait<br>The contest is yet to start.</h1></center>'
PAGE_NOT_FOUND = '<div style="height:50%"></div><center><h1>QAQ<br>What have you done...</h1></center>'

reload(sys)
sys.setdefaultencoding('utf-8')

def fetch_table(url):
    try:
        response = urllib2.urlopen(url, timeout=1)
        html = response.read()
        soup = BeautifulSoup(html)
        table = str(soup.find_all('table')[1])
        Dictionary.getDict('url2table')[url] = table
        return table
    except:
        m = Dictionary.getDict('url2table')
        if url in m.keys():
            return m[url]
        else:
            return 'ＯＪ 炸裂了'


def get_scoreboard(contest_data):
    if(contest_data.status=='incoming'):
        return INCOMING_HTML

    url = contest_data.scoreboard_url
    html = fetch_table(url)
    html = re.sub('AContestant', random.choice(['CKL', 'Chuck Lee', 'AContestant', '清大最強ＣＫＬ']), html)
    html = re.sub('<td>', '<td class="text-center">', html)
    html = re.sub('<th>', '<th class="text-center">', html)
    html = re.sub('0/[0-9]', '<div class="btn-danger text-center">0/1</div>', html)
    html = re.sub('1/1', '<div class="btn-success text-center">1/1</div>', html)
    html = re.sub('4/4', '<div class="btn-success text-center">4/4</div>', html)
    return html

def get_clarification(contest_data):
    clars = Clarification.objects.filter(cid=contest_data.cid).order_by('-time')
    response = str(render_to_response("clarification_table.html", {"clarifications": clars}))
    return response.replace('Content-Type: text/html; charset=utf-8', '')


def get_solution_html(idx, base_url):
    prob = 'p' + str(unichr(ord('a')+idx-1))
    return '<td><a class="href-popup-link" href="' + base_url + prob +'.html">' + prob.upper() + '</a></td>'

def get_problem(contest_data):
    if(contest_data.status=='incoming'):
        return INCOMING_HTML

    url = contest_data.problem_url
    html = fetch_table(url)
    soup = BeautifulSoup(html)
    for a in soup.find_all('a'):
        a['href'] = 'http://140.114.86.238/' + a['href']
        a['class'] = 'href-popup-link'
    if contest_data.status=='ended' and 'http' in contest_data.solution_url:
        trs = soup.find_all('tr')
        for idx, tr in enumerate(trs):
            if idx:
                tr.append(BeautifulSoup(get_solution_html(idx, contest_data.solution_url)))
            else:
                tr.append(BeautifulSoup('<th>Solution</th>'))
    return str(soup)

def get_status(contest_data):
    status = contest_data.status
    if status=='ended' or status=='running':
        return '<a class="btn btn-primary btn-lg" onclick="'+ "$('#p3').click()" + '" data-toggle="tab">'+status+'</a>'
    else:
        return '<a href="#signup-popup" class="open-popup-link btn btn-primary btn-lg">Sign Up!!</a>'
