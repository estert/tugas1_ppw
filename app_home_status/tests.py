from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .models import Status, Comments
from .forms import Status_Form, Comment_Form
from .views import comment

# Create your tests here.
class StatusPageUnitTest(TestCase):

    def test_status_page_is_exist(self):
        response = Client().get('/home-status/')
        self.assertEqual(response.status_code, 200)
    
    def test_comment_status_page_is_exist(self):
        status1 = Status(status ='test aja ya',pk=1)
        response = Client().get('/home-status/comment/1')
        self.assertEqual(response.status_code, 301,200)

    def test_comment_link_using_comment_function(self):
        status1 = Status(status ='test aja ya',pk=1)
        found = resolve('/home-status/comment/1/')
        self.assertEqual(found.func, comment)

    def test_root_url_now_is_using_index_page_from_app_home_status(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 301)
        self.assertRedirects(response,'/home-status/',301,200)

    def test_model_can_create_new_status(self):
        #Creating a new activity
        new_activity = Status.objects.create(status ='test aja ya')

        #Retrieving all available activity
        counting_all_available_Status= Status.objects.all().count()
        self.assertEqual(counting_all_available_Status,1)

    def test_model_creating_status_wrongly_and_render_the_result(self):
        response = Client().post('/home-status/add_status', {'status' : ''})
        self.assertEqual(response.status_code, 302)

    def test_status_showing_all_status(self):

        status = 'coba coba coba'
        new_status = {'status' : status}
        post_new_status = Client().post('/home-status/add_status', new_status)

        response = Client().get('/home-status/')
        html_response = response.content.decode('utf8')

        self.assertIn(status, html_response)
    
    def test_comment_is_doable(self):
        status2 = Status(status ='test aja ya',pk=1)
        comment1 = Comments(comment='test melulu', nama = 'afkar', post=status2)
        comment1.save()
        counting_all_available_comment= Comments.objects.all().count()
        self.assertEqual(counting_all_available_comment, 1)

    def test_comment_is_shown_at_home(self):
        statusbaru1 = 'bisabisa'
        postbaru = Client().post('/home-status/add_status', {'status':statusbaru1,id:1})
        response = Client().get('/home-status/')
        html_response = response.content.decode('utf8')
        self.assertIn(statusbaru1,html_response)

        post_terkait = Status.objects.get(id=1)
        comment10 = 'insyaAllah'
        new_comment = Client().post('/home-status/add_comment/1/', {'comment':comment10, 'nama' : 'anas', 'post':post_terkait})

        response2 = Client().get('/home-status/')
        html_response2 = response2.content.decode('utf8')
        self.assertIn(comment10, html_response2)

    def test_form_comment_form_has_placeholder_and_css_classes(self):
        form = Comment_Form()
        self.assertIn('class="form-control', form.as_p())
        self.assertIn('id="id_nama"', form.as_p())
        self.assertIn('class="form-control', form.as_p())
        self.assertIn('id="id_comment', form.as_p())
        

