'''
usage:
type "python manage.py shell"
paste the code in shell
'''
from contest.models import *
contest1 = Contest.objects.filter(cid=1)

if not contest1:
    Contest.objects.create(cid=1, 
        problem_url='http://140.114.86.238/contest.php?cid=654', 
        scoreboard_url='http://140.114.86.238/scoreboard.php?cid=654',
        date='11/29')
