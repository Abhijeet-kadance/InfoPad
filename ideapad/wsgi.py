"""
WSGI config for ideapad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

<<<<<<< HEAD
dotenv.read_dotenv(str(ENV_FILE_PATH))
=======
dotenv.load_dotenv(str(ENV_FILE_PATH))

>>>>>>> efdeb17f103fc7796aef297a12cf4ed19b56d652
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideapad.settings')

application = get_wsgi_application()
