from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"InvalidCredentials")
            return redirect("login")

        else:
            auth.login(request,user)
            return redirect("/")



    else:
        return render(request,'login.html')

    
   
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['Last_name']
        username=request.POST['User_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,"User Taken")
               return redirect('rejogister')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"EmailId already exists")
                return redirect('register')
              
            else:
                user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"User created")
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')

        return redirect('/')
    else:
       return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')