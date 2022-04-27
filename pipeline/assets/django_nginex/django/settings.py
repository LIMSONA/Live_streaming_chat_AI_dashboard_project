# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    '****************'  # 본인 settings.py에 있는 키를 입력
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', 1))

if os.environ.get('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = []