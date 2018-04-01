from django.conf.urls import url
from .views import index, add_status, comment, add_comment

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_status', add_status, name='add_status'),
    url(r'^comment/(?P<id>\w{0,50})/$', comment, name='comment'),
    url(r'^add_comment/(?P<id>\w{0,50})/$', add_comment, name='add_comment'),
]