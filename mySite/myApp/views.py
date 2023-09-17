from django.shortcuts import render,HttpResponse

import requests

# Create your views here.


def forDoctor(request):
    api_url = "http://127.0.0.1:3000/appointments"
    response = requests.get(api_url)
    data = response.json()
    
    print(data[0])
    context={
        'data':data
    }
    return render(request,"doctorsLandingPage.html",context)


def forDesk(request):
    api_url = "http://127.0.0.1:3000/doctors"
    response = requests.get(api_url)
    data = response.json()

    print(data[0])
    context = {
        'data':data
    }
    return render(request,'deskLandingPage.html',context)

def home(request):



    return HttpResponse("<h1>Hello World</h1>")



