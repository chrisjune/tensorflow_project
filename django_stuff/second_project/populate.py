import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoLevelTwo.settings')

import django
django.setup()

## Fake pop script
from faker import Faker
from user.models import User
fake = Faker()
def populate(N=5):
    for entry in range(N):
        fake_name = fake.name().split(' ')
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake.email()
        u = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]
        print(u)

if __name__ == "__main__":
    print("Populate User Start")
    populate(20)
    print("Populate User Complete")