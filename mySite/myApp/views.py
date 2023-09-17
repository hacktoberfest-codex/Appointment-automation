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

    

    print(f'Forwarded = {forwarded}')
    print(data[0])
    context={
        'data':data,
        'forwarded':forwarded,
        'pending':pending,
    }
    return render(request,"doctorsLandingPage.html",context)

def get_user(request):
    api_url = "http://127.0.0.1:3000/patients"
    response = requests.get(api_url)
    data = response.json()



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



