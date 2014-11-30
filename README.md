##Needed plugin:
- beautifulsoup4

##Usage:
```sh
cd ISeaTeL_Cup_Site
#assume you have install pip and django.
pip install beautifulsoup4
alias dj='python manage.py'
dj makemigrations
dj syncdb
dj runserver --insecure
```