from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:

            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect( 'authen:registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken")
                return redirect('authen:registration')
            else:
                user = User.objects.create_user(username=username,last_name=last_name,first_name=first_name,email=email,password=password)
                user.save()


                return redirect('authen:login')
        else :
            messages.info(request, "Password not Matching")
            return redirect("authen:registration'")
    return render(request,"registration.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)

            return redirect('bankapp:details')
        else:
            messages.info (request,"Invalid Credential")
            return redirect('authen:login')

    return render(request, "Login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')