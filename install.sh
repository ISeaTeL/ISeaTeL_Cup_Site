# install some needed python package
pip install beautifulsoup4
pip install django-grappelli
pip install django-pagedown
pip install django-markdown-deux
pip install django-crispy-forms

# gmail password
GMAIL_PWD=ISeaTeLContestSite/password.py

if [ -f $GMAIL_PWD ];
then
   echo "File $GMAIL_PWD exists."
else
   echo "File $GMAIL_PWD does not exist."
   read -p "Enter contest site gmail password: " PWD
   echo "GMAIL_PASSWORD = '$PWD'" >> $GMAIL_PWD
fi

python manage.py collectstatic --noinput
alias dj='python manage.py'
dj makemigrations
dj syncdb
dj runserver --insecure
