from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Status, Comments
from .forms import Status_Form, Comment_Form
from app_profile_page.active_profile import get_active_profile

# Create your views here.
response = {}

def index(request):
    profile = get_active_profile()
    status = Status.objects.order_by('-created_date')
    comments = Comments.objects.all()
    response['nama'] = profile.name
    response['picture'] = profile.picture_url
    response['status'] = status
    response['status_form'] = Status_Form
    response['comments'] = comments
    html = 'home_status.html'
    return render(request, html, response)

def add_status(request):
    response['status'] = request.POST['status']
    status = Status(status=response['status'])
    status.save()
    return HttpResponseRedirect('/home-status')

def comment(request,id):
    status = Status.objects.get(id=id)
    response['status'] = status
    response['comment_form'] = Comment_Form
    html = 'comment_status.html'
    return render(request, html, response)

def add_comment(request,id):
    response['adding_comment'] = request.POST['comment']
    response['nama'] = request.POST['nama']
    response['status'] = Status.objects.get(id=id)
    comment = Comments(comment = response['adding_comment'], nama = response['nama'],  post = response['status'])
    comment.save()
    return HttpResponseRedirect('/home-status')




