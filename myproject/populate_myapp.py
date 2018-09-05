import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from myapp.models import Musician, Album, User
from faker import Faker

fakegen = Faker()

def populate(N=5):
	for entry in range(N):

		fake_first_name = fakegen.first_name()
		fake_last_name = fakegen.last_name()
		fake_email =fakegen.email()

		fake_name = fakegen.name()
		fake_date = fakegen.date()
		fake_num = fakegen.random_digit()

		m = Musician.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,instrument=fake_name)[0]

		a = Album.objects.get_or_create(artist=m, name=fake_name, release_date=fake_date, num_stars=fake_num)[0]

		u = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__=='__main__':
	print("populating script!!")
	populate(10)
	print("Completed!")

