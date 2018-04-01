from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .models import Profile
from .views import index
# Create your tests here.

class ProfileUnitTest(TestCase):
    def test_profile_url_is_exist(self):
        response = Client().get('/profile-page/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_using_index_func(self):
        found = resolve('/profile-page/')
        self.assertEqual(found.func, index)
