# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .chatbot import parentbot,studentbot,staffbot,guestbot
# Create your views here.

def parentchat(request):
    if request.method=="POST":
        text=request.POST["text"]
        a=str(parentbot.get_response(text))
        print(a)
        return HttpResponse(a)
    return render(request,'parentchatbot.html')
def studentchat(request):
    if request.method=="POST":
        text=request.POST["text"]
        a=str(studentbot.get_response(text))
        print(a)
        return HttpResponse(a)
    return render(request,'studentchatbot.html')
def staffchat(request):
    if request.method=="POST":
        text=request.POST["text"]
        print(str(staffbot.get_response(text)))
        return HttpResponse(str(staffbot.get_response(text)))
    return render(request,'staffchatbot.html')
def guestchat(request):
    if request.method=="POST":
        text=request.POST["text"]
        print(str(guestbot.get_response(text)))
        return HttpResponse(str(guestbot.get_response(text)))
    return render(request,'guestchatbot.html')

