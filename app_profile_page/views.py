from django.shortcuts import render
from datetime import datetime, date
from .active_profile import get_active_profile


# Create your views here.
exp = ['Marketing', 'Collector', 'Programmer']
def index(request):

    profile = get_active_profile()
    response = {'name': profile.name,'description': profile.description, 'gender': profile.gender,
                'email': profile.email, 'birth': profile.birth_date, 'expertise': exp,
                'picture': profile.picture_url}
    return render(request, 'profile_page.html', response)
