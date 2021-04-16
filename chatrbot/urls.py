from django.urls import path
from . import views

urlpatterns = [
    path('studentchatbot',views.studentchat,name="studentchatbot"),
    path('parentchatbot',views.parentchat,name="parentchatbot"),
    path('staffchatbot',views.staffchat,name="staffchatbot"),
    path('guestchatbot',views.guestchat,name="guestchatbot"),

]