pip install beautifulsoup4
pip install django-grappelli
pip install django-pagedown
pip install django-markdown-deux

python manage.py collectstatic --noinput
alias dj='python manage.py'
dj makemigrations
dj syncdb
dj runserver --insecure
