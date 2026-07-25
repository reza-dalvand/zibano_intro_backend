"""
ASGI config for zibano_intro project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zibano_intro.settings')

application = get_asgi_application()