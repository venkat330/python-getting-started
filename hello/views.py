from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import json
import uuid

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def getUUID(request):
    requestInfo = json.loads(request.body)
    respnseData = {}
    if "atmId" in requestInfo and len(requestInfo['atmId']):
        respnseData['atmId']=requestInfo['atmId']
        requestInfo['uniqueId']=uuid.uuid4()
    else:
        return HttpResponseBadRequest()
    #greeting.save()

    #greetings = Greeting.objects.all()

    return HttpResponse(json.dumps(respnseData), content_type="application/json")

def serverAuthentication(request):
    requestInfo = json.loads(request.body)
    respnseData = {}
    if "atmId" in requestInfo and len(requestInfo['atmId']):
        if "uniqueId" in requestInfo and len(requestInfo['uniqueId']):
            respnseData['atmId']=requestInfo['atmId']
            respnseData['uniqueId']=requestInfo['uniqueId']
            respnseData['track2']=" ;1234567890123445=99011200XXXX00000000?"
            return HttpResponse(json.dumps(respnseData), content_type="application/json")
    return HttpResponseBadRequest()
    #greeting.save()

    #greetings = Greeting.objects.all()

    return HttpResponse(json.dumps(respnseData), content_type="application/json")
