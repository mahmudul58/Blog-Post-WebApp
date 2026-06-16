import os
import django
from django.conf import settings
from django.contrib.staticfiles import finders

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

print("STATIC_URL:", settings.STATIC_URL)
print("STATICFILES_DIRS:", settings.STATICFILES_DIRS)
print("Finding css/style.css:", finders.find('css/style.css'))

