import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'second_project.settings')

import django
django.setup()

from second_app.models import User
from faker import Faker

fake = Faker()

def populate(N=10):
    for entry in range(N):
        fake_name = fake.name().split(' ')
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake.email()

        usr = User.objects.get_or_create(first_name=fake_first_name, last_name = fake_last_name, email = fake_email)[0]
        print(usr)

if __name__ == '__main__':
    print("POPULATING Start")
    populate(20)
    print("POPULATING End")
