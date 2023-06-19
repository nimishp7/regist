from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.pOST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 !=pass2:
            return HttpResponse('passwords does not match')
        my_user = User.objects.create_user()
    return render (request, 'signup.html')

def LoginPage(request):
    return render(request, 'login.html')

def HomePage(request):
    return render(request, 'home.html')