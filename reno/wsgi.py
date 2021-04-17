"""
WSGI config for reno project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os,sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.join(settings.BASE_DIR, "apps"))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reno.settings.dev')

application = get_wsgi_application()
