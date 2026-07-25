"""
WSGI config for zibano_intro project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zibano_intro.settings')

application = get_wsgi_application()