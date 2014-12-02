pip install beautifulsoup4
alias dj='python manage.py'
dj makemigrations
dj syncdb
dj shell < initdb.py
dj runserver --insecure
