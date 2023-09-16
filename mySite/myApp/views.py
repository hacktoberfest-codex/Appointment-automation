from django.shortcuts import render,HttpResponse

import requests

# Create your views here.


def forDoctor(request):
    api_url = "http://127.0.0.1:3000/appointments"
    response = requests.get(api_url)
    data = response.json()

    storage = {}
    
    for n in data:
        storage[n['_id']]=n['patient']

    print(storage)

    return render(request,"doctorsLandingPage.html")


def forDesk(request):
    api_url = "http://127.0.0.1:3000/appointments"
    response = requests.get(api_url)
    data = response.json()

    return render(request,'deskLandingPage.html')

def home(request):



    return HttpResponse("<h1>Hello World</h1>")



