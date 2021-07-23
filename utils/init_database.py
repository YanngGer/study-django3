import os
import sys
import django

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
django.setup()

from user.models import User

def create_user():
    User.objects.create_superuser(username='admin', password='admin123456',name='admin',user_id=1,email='admin@qq.com')

if __name__ == '__main__':
    create_user()
    print('ok')