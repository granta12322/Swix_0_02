"""
WSGI config for Rest_Test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os

configuration = os.getenv('ENVIRONMENT', 'development').title()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rest_Test.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', configuration)

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
 