from conduit.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '13q$v6_po-j^dxlt2b!w(!5j0mf**w8g$&%z0205o7ephoph(p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
