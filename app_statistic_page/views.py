from django.shortcuts import render
from app_home_status.models import Status
from app_home_status.forms import Status_Form
from app_add_friend.models import Message
# Create your views here.

response = {}
def index(request):
    status = Status.objects.order_by('-created_date')
    if len(status) != 0:
        statusAkhir = Status.objects.order_by('-created_date')[0]
        response['statusAkhir'] = statusAkhir
    else:
        response['statusAkhir'] = 'Tidak ada status'

    response['number_of_feed'] = Status.objects.all().count()
    response['number_of_friend'] = Message.objects.all().count()
    html = 'statistic_page.html'
    return render(request, html, response)
