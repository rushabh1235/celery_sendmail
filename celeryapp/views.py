from django.shortcuts import render,HttpResponse
from .tasks import mail_information
# Create your views here.

def intro(request):
    mail_information.delay()
    return HttpResponse("done")