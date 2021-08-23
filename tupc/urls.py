"""acso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('SignUp/', views.signup, name='signup'),

    #Organization
    path('org/', views.organization, name='org'),
    #Form Officers
    path('FormOfficers/', views.form, name='Form'),
    #CRUD Form Officers
    path('CRUD/', views.crud, name='crud'),
    path('update_profile/<str:pk>/', views.update, name="update_profile"),
    path('nextpage', views.nextpage, name='nextpage'),
    #View Activities
    path('Data/', views.data, name='Data'),
    path('view_data/<str:pk>/', views.view_data, name="view_data"),
    #Form Report
    path('Activities/', views.activity, name='Activities'),
    #View Report
    path('View/', views.view, name='View'),
    #About US
    path('Reports/', views.report, name='Report'),


    #ADMIN ACCESS
    path('History/', views.history, name='History'),
    path('Editable/', views.editable, name='Editable'),
    path('Table/', views.table, name='Table'),
]
