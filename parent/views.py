from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .models import Users
# Create your views here.


def parentlogin(request):
    if request.method== 'POST':
        MailId = request.POST['MailId']
        password = request.POST['password']
        user = auth.authenticate(email=MailId,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('parentlogin')
    else:
        return render(request,'parentlogin.html')    

def parentregister(request):
    if request.method == 'POST':
        email = request.POST['MailId']
        password= request.POST['createpassword']
        secpassword = request.POST['confirmpassword']
        username = request.POST['username']
        if  password==secpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'MailId Taken')
                return redirect('parentregister')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('parentregister')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                #dummyusers=Users()
                # #dummyusers.name=username
                # print('user created')
                return redirect('parentlogin')
        else:
            messages.info(request,'password not matching..')    
            return redirect('parentregister')
#return redirect('/')

    else:
        return render(request,'parentregister.html')



def  parentlogout(request):
    auth.logout(request)
    return redirect('/')    

