MOST BASIC
mkdir example.com
cd example.com
virtualenv .
source bin/activate
pip install django
pip freeze > requirements.txt
django-admin.py startproject project