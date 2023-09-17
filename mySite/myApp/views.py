from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

import requests

# Create your views here.


def forDoctor(request):
    api_url = "http://127.0.0.1:3000/appointments"
    response = requests.get(api_url)
    data = response.json()
    
    forwarded = []
    pending = []
    for gn in data:
        if( gn['status']=='forwarded' ):
            forwarded.append(gn)
        if( gn['status']=='pending' ):
            pending.append(gn)

    context={
        'data':data,
        'forwarded':forwarded,
        'pending':pending,
    }
    return render(request,"doctorsLandingPage.html",context)


def forDoctor2(request,id):
    api_url = "http://127.0.0.1:3000/appointments"
    response = requests.get(api_url)
    data = response.json()

    api_url2 = f"http://127.0.0.1:3000/patients?number={id}"
    response2 = requests.get(api_url2)
    patient = response2.json()
    print(id)
    print(patient)
    forwarded = []
    pending = []
    for gn in data:
        if( gn['status']=='forwarded' ):
            forwarded.append(gn)
        if( gn['status']=='pending' ):
            pending.append(gn)

    context={
        'data':data,
        'forwarded':forwarded,
        'pending':pending,
        'patient':patient[0],
    }
    return render(request,"doctorsLandingPage2.html",context)


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



