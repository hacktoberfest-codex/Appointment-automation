from django.shortcuts import render,HttpResponse

# Create your views here.


def landingPage(request):


    return render(request,"doctorsLandingPage.html")


def home(request):



    return HttpResponse("<h1>Hello World</h1>")



