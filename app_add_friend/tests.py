from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import index
from .models import Message
from .forms import Message_Form

class AddFriendUnitTest(TestCase):
	def test_add_friend_url_is_exist (self):
		response = Client().get('/add-friend/')
		self.assertEqual(response.status_code, 200)
		
	def test_addFriend_using_index_func(self):
		found = resolve('/add-friend/')
		self.assertEqual(found.func, index)
		
	def test_form_message_input_has_placeholder_and_css_classes(self):
		form = Message_Form()
		self.assertIn('class="form-control"', form.as_p())
		self.assertIn('<label for="id_name">Nama:</label>', form.as_p())
		self.assertIn('<label for="id_url">Heroku URL:</label>', form.as_p())
		
	def test_form_validation_for_blank_items(self):
		form = Message_Form(data={'name':'','url:':''})
		self.assertFalse(form.is_valid())
	
	def test_tugas1_post_success_and_render_the_result(self):
		anonymous = 'Anonkjhkhymousymous'
		url = 'http://aloha.herokuapp.com'
		response = Client().post('/add-friend/add_friend', {'name':anonymous,'url':url})
		self.assertEqual(response.status_code, 302)
		
		response = Client().get('/add-friend/')
		html_response = response.content.decode('utf8')
		self.assertIn(anonymous,html_response)
		self.assertIn(url,html_response)
		
	def test_tugas1_post_fail(self):
		response = Client().post('/add-friend/add_friend', {'name': '', 'url': ''})
		self.assertEqual(response.status_code, 302)