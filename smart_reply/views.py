from django.shortcuts import render
from django.http import HttpResponse

def smart_reply_home(req):
    return render(req, 'smart_reply/base.html')

def smart_reply_view(req):
    return render(req, 'smart_reply/base.html')
# Create your views here.
