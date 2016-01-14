from django.shortcuts import HttpResponse
from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    ip = request.environ.get('REMOTE_ADDR', None)

    web_user_list = WebUser.objects.filter(ip=ip)
    if not web_user_list:
        WebUser.objects.create(ip=ip)
    else:
        web_user = web_user_list.get()
        web_user.pv += 1
        web_user.save()

    return render(request, '2.html', {'data': web_user_list[0]})
