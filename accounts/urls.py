from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index', views.index,name="index"),
    path('guest', views.guest,name="guest"),
    path('studentlogin', views.studentlogin,name="studentlogin"),
    path('studentregister', views.studentregister,name="studentregister"),
    path('studentprofile', views.studentprofile,name="studentprofile"),
    path('logout',views.logout,name="logout"),
    path('parentlogin',views.parentlogin,name="parentlogin"),
    path('parentregister',views.parentregister,name="parentregister"),
    path('parentprofile', views.parentprofile,name="parentprofile"),
    path('stafflogin',views.stafflogin,name="stafflogin"),
    path('staffregister',views.staffregister,name="staffregister"),
    path('staffprofile', views.staffprofile,name="staffprofile"),
    path('Adminlogin',views.Adminlogin,name="Adminlogin"),
    path('Adminregister',views.Adminregister,name="Adminregister"),
    path('authchat',views.authchat,name="authchat"),
    path('password_reset/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
     
     
     ]
