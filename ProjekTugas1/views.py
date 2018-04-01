from django.shortcuts import render, HttpResponsePermanentRedirect

#TODO Implement
#Create a content paragraph for your landing page:

def index(request):
    return HttpResponsePermanentRedirect('/home-status')