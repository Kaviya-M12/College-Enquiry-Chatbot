# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
#from .models import Users
# Create your views here.

def index(request):
    return render(request,'index.html')
def guest(request):
    return redirect('guestchatbot')
@index_required(index_url="/studentlogin")
def authchat(request):
    return redirect('studentchatbot')
    
def logout(request):
    if  'profile' in request.session:
        request.session.flush()
    return render(request,'index.html')

def studentlogin(request):
    if request.method== 'POST':
        email= request.POST['MailId']
        password = request.POST['password']
        status=request.POST['cap']
        user = Student.objects.filter(email=email ,password=password).first()
        if status=="valid" and Student.objects.filter(email=email,password=password).exists():
            request.session['profile']={'username':user.Name,'Department':user.Department,'year':user.YearofPassing,'MailId':user.email,'Password':user.password}
            userses=request.session['profile']
            request.session.modified=True
            return render(request,'studentchatbot.html',{"userses":userses})
        else:
            messages.info(request,'invalid credentials')
            return render(request,'signinforstudent.html')    

    else:
        return render(request,'signinforstudent.html')    
def studentprofile(request):
    user=request.session['profile']
    return render(request,'studentprofile.html',{'user':user})    

         


def studentregister(request):
    if request.method == 'POST':
        password=request.POST['createpassword']
        secpassword=request.POST['confirmpassword']
        if password==secpassword:
            for studentitr in Student.objects.all():
                if studentitr.Name==request.POST['username']:
                    messages.info(request,'username taken')
                    return render(request,'studentregister.html')
                if studentitr.email==request.POST['MailId']:
                    messages.info(request,'email taken')
                    return render(request,'studentregister.html')
            student=Student()
            student.Name=request.POST['username']
            student.Department=request.POST['Department']
            student.YearofPassing=request.POST['year']
            student.email=request.POST['MailId']
            student.password=password
            student.save()
            return redirect('studentlogin')
        else:
            return render(request,'studentregister.html')
    else:
        return render(request,'studentregister.html')

    

'''
        email = request.POST['MailId']
        password= request.POST['createpassword']
        secpassword = request.POST['confirmpassword']
        username = request.POST['username']
        department=request.POST['Department']
        yearofpassing=request.POST['yearofpassing']
        if  password==secpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'MailId Taken')
                return redirect('studentregister')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('studentregister')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                    #dummyusers=Users()
                    # #dummyusers.name=username
                    # print('user created')
                return redirect('studentlogin')
        else:
            messages.info(request,'password not matching..')    
            return redirect('studentregister')
#return redirect('/')
'''
    


def studentlogout(request):
    auth.logout(request)
    return redirect('/')    

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
#from .models import Users
# Create your views here.


def parentlogin(request):
    if request.method== 'POST':
        email= request.POST['MailId']
        password = request.POST['password']
        status= request.POST['cap']
        #user = Parent.objects.get(email=email,password=password)
        user = Parent.objects.filter(email=email ,password=password).first()
        if status=="valid" and  Parent.objects.filter(email=email,password=password).exists():
            request.session['profile']={'studentname':user.Studentname,'parentname':user.Parentname,'MailId':user.email,'Password':user.password}
            userses=request.session['profile']
            request.session.modified=True
            return render(request,'parentchatbot.html',{"userses":userses})
        else:
            messages.info(request,'invalid credentials')
            return render(request,'signinforparent.html')    

    else:
        return render(request,'signinforparent.html')    
def parentprofile(request):
    user=request.session['profile']
    return render(request,'parentprofile.html',{'user':user})    

         





def parentregister(request):
    if request.method == 'POST':
        password=request.POST.get('createpassword')
        secpassword=request.POST['confirmpassword']
        if password==secpassword:
            for parentitr in Parent.objects.all():
                if parentitr.Parentname==request.POST['username2']:
                    messages.info(request,'username taken')
                    return render(request,'parentregister.html')
                if parentitr.email==request.POST['MailId']:
                    messages.info(request,'email taken')
                    return render(request,'parentregister.html')
            parent=Parent()
            parent.Studentname=request.POST['username1']
            parent.Parentname=request.POST['username2']
            parent.email=request.POST['MailId']
            parent.password=password
            parent.save()
            return redirect('parentlogin')
        else:
             return render(request,'parentregister.html')
    else:
        return render(request,'parentregister.html')
    
'''     email = request.POST['MailId']
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
'''
   


def  parentlogout(request):
    auth.logout(request)
    return redirect('/')    
    

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .models import Users
# Create your views here.


def stafflogin(request):
    if request.method== 'POST':
        email= request.POST['MailId']
        password = request.POST['password']
        status=request.POST['cap']
        user = Staff.objects.filter(email=email ,password=password).first()     
        if status== "valid" and Staff.objects.filter(email=email,password=password).exists():
            request.session['profile']={'username':user.Name,'Department':user.Department,'MailId':user.email,'Password':user.password}
            userses=request.session['profile']
            request.session.modified=True
            return render(request,'staffchatbot.html',{"userses":userses})
        else:
            messages.info(request,'invalid credentials')
            return render(request,'signinforstaff.html')
    else:
        return render(request,'signinforstaff.html')
        
def staffprofile(request):
    user=request.session['profile']
    return render(request,'staffprofile.html',{'user':user})    





def staffregister(request):
    if request.method == 'POST':
        password=request.POST.get('createpassword')
        secpassword=request.POST.get('confirmpassword')
        if password==secpassword:
            for staffitr in Staff.objects.all():
                if staffitr.Name==request.POST.get('username'):
                    messages.info(request,'username taken')
                    return render(request,'staffregister.html')
                if staffitr.email==request.POST.get('MailId'):
                    messages.info(request,'email taken')
                    return render(request,'staffregister.html')
            staff=Staff()
            staff.Name=request.POST['username']
            staff.Department=request.POST['Department']
            staff.email=request.POST['MailId']
            staff.password=password
            staff.save()
            return redirect('stafflogin')
        else:
            return render(request,'staffregister.html')
    else:
        return render(request,'staffregister.html')

'''
        email = request.POST['MailId']
        password= request.POST['createpassword']
        secpassword = request.POST['confirmpassword']
        username = request.POST['username']
        department=request.POST['department']
        if  password==secpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'MailId Taken')
                return redirect('staffregister')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('staffregister')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                #dummyusers=Users()
                # #dummyusers.name=username
                # print('user created')
                return redirect('stafflogin')
        else:
            messages.info(request,'password not matching..')    
            return redirect('staffregister')
#return redirect('/')
'''
   


def stafflogout(request):
    auth.logout(request)
    return redirect('/')    



from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .models import Users
# Create your views here.


def Adminlogin(request):
    if request.method == 'POST':
        email= request.POST['MailId']
        password = request.POST['password']
        user = Admin.objects.filter(email=email,password=password)
        if Admin.objects.filter(email=email,password=password).exists():
            return redirect('')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'signinforadmin.html')
    else:
        return render(request,'signinforadmin.html')    

def Adminregister(request):
    if request.method == 'POST':
        fir_pass=request.POST['createpassword']
        sec_pass=request.POST['confirmpassword']
        if fir_pass==sec_pass:
            for adminitr in Admin.objects.all():
                if adminitr.Name==request.POST['username']:
                    messages.info(request,'username taken')
                    return render(request,'Adminregister.html')
                if adminitr.email==request.POST['MailId']:
                    messages.info(request,'email taken')
                    return render(request,'Adminregister.html')
            admin=Admin()
            admin.Name=request.POST['username']
            admin.email=request.POST['MailId']
            admin.password=request.POST['createpassword']
            admin.save()
            return render(request,'signinforadmin.html')
        else:
            return render(request,'Adminregister.html')
    else:
        return render(request,'Adminregister.html')

         
'''
        email = request.POST['MailId']
        password= request.POST['createpassword']
        secpassword = request.POST['confirmpassword']
        username = request.POST['username']
        if  password==secpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'MailId Taken')
                return redirect('Adminregister')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('Adminregister')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                #dummyusers=Users()
                # #dummyusers.name=username
                # print('user created')
                return redirect('Adminlogin')
        else:
            messages.info(request,'password not matching..')    
            return redirect('Adminregister')
#return redirect('/')
'''

def Adminlogout(request):
    auth.Adminlogout(request)
    return redirect('/')    


