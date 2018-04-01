"""ProjekTugas1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
import app_home_status.urls as app_home_status
import app_profile_page.urls as app_profile_page
import app_add_friend.urls as app_add_friend
import app_statistic_page.urls as app_statistic_page
from .views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home-status/', include(app_home_status, namespace='home-status')),
    url(r'^profile-page/', include(app_profile_page,namespace='profile-page')),
    url(r'^add-friend/', include(app_add_friend, namespace='add-friend')),
    url(r'^my-stats/', include(app_statistic_page,namespace='my-stats')),
    url(r'^$', RedirectView.as_view(url='home-status/', permanent='true'), name='index'),
]
