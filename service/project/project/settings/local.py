from django.conf import settings

import os
print "--------"
print "ON LOCAL"
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}