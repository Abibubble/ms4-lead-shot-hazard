"""
WSGI config for lead_shot_hazard project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lead_shot_hazard.settings')

application = get_wsgi_application()
