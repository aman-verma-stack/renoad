from .settings import *

#ALLOWED_HOSTS = ['http://renoad.com/', 'http://renoad.com', 'www.renoad.com/', 'www.renoad.com', 'renoad.com/','renoad.com', 'http://139.59.14.43:8000']

ALLOWED_HOSTS =['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'renoad',
        'USER': 'root',
        'PASSWORD': 'renoad@jiten',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
