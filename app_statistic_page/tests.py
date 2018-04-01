from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import index
from app_home_status.models import Status
from app_home_status.forms import Status_Form
# Create your tests here.

class Lab4UnitTest(TestCase):
    def test_statistic_page_url_is_exist(self):
        response = Client().get('/my-stats/')
        self.assertEqual(response.status_code, 200)

    def test_statistic_page_using_index_func(self):
        found = resolve('/my-stats/')
        self.assertEqual(found.func, index)