from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Message_Form
from .models import Message

response = {'author': "Reza Akbar Shahputra"}
def index(request):
	html = 'add_friend/add_friend.html'
	response['message_form'] = Message_Form
	data = Message.objects.all()
	response['data'] = data
	return render(request, html, response)

def add_friend(request):
	form = Message_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['name'] = request.POST['name']
		response['url'] = request.POST['url']
		data = Message(name=response['name'], url=response['url'])
		data.save()
		return HttpResponseRedirect('/add-friend/')
	else:
		return HttpResponseRedirect('/add-friend/')