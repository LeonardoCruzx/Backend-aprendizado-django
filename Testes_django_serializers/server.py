import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leonardo281$teste',
        'USER': 'leonardo281',
        'PASSWORD': 'teste001',
        'HOST': 'leonardo281.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}