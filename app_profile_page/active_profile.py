from datetime import date
from .models import Profile

#Default user
NAME = 'Hepzibah Smith'
EMAIL = 'hello@smith.com'
PICTURE_URL = 'https://orig00.deviantart.net/08ce/f/2008/235/9/2/hepzibah_smith_by_jlestrange.jpg'
GENDER = 'Female'
DESCRIPTION = 'Antique expert. Experience as marketer for 10 years'
BIRTH = date(1998, 6, 28)
EXPERTISE = 'Marketing', 'Collector', 'Programmer'

def get_active_profile():
    #Will return most recently created profile, create a new one if none exists
    if not Profile.objects.all():
        create_new_profile()
    return Profile.objects.all()[len(Profile.objects.all()) - 1]

def create_new_profile():
    #Will create new profile based on the variables defined as the default user on active_profile
    Profile.objects.create(name=NAME, email=EMAIL, picture_url=PICTURE_URL, gender=GENDER,
                           description=DESCRIPTION, birth_date=BIRTH, expertise=EXPERTISE)
