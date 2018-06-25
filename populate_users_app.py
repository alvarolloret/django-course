
#Lecture 128
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()


#FAKE POP JavaScript
import random
from users_app.models import User, UserAge
from faker import Faker

fakegen =Faker()
topics=['Search', 'Social', 'Marketplace', 'News', 'Games']
def add_name():
    fake_name = fakegen.name()
    fake_email = fakegen.email()
    fake_age = fakegen.random_int(min=18, max=99)
    t=User.objects.get_or_create(name=fake_name, email=fake_email, age=fake_age)[0]
    t.save()
    return t

def populate(N=5):
    for entry in range (N):
        #get the topic for the entry
        top = add_name()

        #create the fake data for that entry
        #Create the new webpage entry
        #usr=UserAge.objects.get_or_create(user_age=top.age,user_name=top.name)[0]
        #user_age=top.age,
        # #Create fqke acces AccesRecord
        # acc_rec =AccesRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__== '__main__':
    print ("populating script!")
    populate(20)
    print ("populating complete")
