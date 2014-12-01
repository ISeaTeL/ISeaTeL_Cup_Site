from django.shortcuts import render
import urllib2
import re
from bs4 import BeautifulSoup
# Create your views here.

def fetch_scoreboard(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup.find_all('table')[1]

def scoreboard(request):
	rawData = str(fetch_scoreboard('http://140.114.86.238/scoreboard.php?cid=654'))
	rawData = re.sub('<td>', '<td class="text-center">', rawData)
	rawData = re.sub('<th>', '<th class="text-center">', rawData)
	rawData = re.sub('0/[0-9]', '<div class="btn-danger text-center">0/1</div>', rawData)
	rawData = re.sub('1/1', '<div class="btn-success text-center">1/1</div>', rawData)
	rawData = re.sub('4/4', '<div class="btn-success text-center">4/4</div>', rawData)
	return render(request, 'scoreboard.html', {"scoreboard_table": rawData})
