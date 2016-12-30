from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2
from .faceroc import preptraining

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
    
def detect(request):
    data = {'success':False}
    content = request.GET['content']    
    if request.FILES.get('image', None) is not None:
        image = _grab_image(stream=request.FILES["image"])
        if content == "register":
            accountin = request.GET['account']
            facial = face(account =accountin )
            facial.save()
            picture = piclist(Picture = request.FILES["image"])
            picture.save()
            facial.pictures.add(picture)
            did = facial.id
            ret = train(did)
            if ret:
                data['success'] = True
            return JsonResponse(data)         
        else:
            accountin = request.GET['account']
            faced.objects.get(account = accountin)
            obj = detect(image, accountin)
            obj['account'] = accountin
            return jsonResponse()
                
    else:
        data = {'success':False}
        return JsonResponse(data) 


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

