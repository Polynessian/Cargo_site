import os 
from pathlib import Path
import psycopg2 

BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR, 'Secret_files/prod_secret_key.txt')) as f:
   SECRET_KEY = f.read().strip()
   
   

DEBUG = False


ALLOWED_HOSTS = [ '127.0.0.1' ] 

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cargo',
        'USER': 'viktor',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
        }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
