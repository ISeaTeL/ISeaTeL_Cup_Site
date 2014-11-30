from django.shortcuts import render
import urllib2
from bs4 import BeautifulSoup
# Create your views here.

def fetch_scoreboard(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup.find_all('table')[1]

def scoreboard(request):
	 return render(request, 'scoreboard.html', {"scoreboard_table": str(fetch_scoreboard('http://140.114.86.238/scoreboard.php?cid=654'))})