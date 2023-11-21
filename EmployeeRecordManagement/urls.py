"""
URL configuration for EmployeeRecordManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name='index'),
    path ('registration/', registration, name='registration'),
    path('emp_login/', emp_login, name='emp_login'),
    path('emp_home/', emp_home, name='emp_home'),
    path('profile/',profile,name='profile'),
    path('logout/',Logout,name='logout'),
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_home/',admin_home, name='admin_home'),
    path('holidays/', holidays, name='holidays'),
    path('admin_holidays/', admin_holidays, name='admin_holidays'),
    path('emp_task', emp_task, name='emp_task'),
    path('admin_task', admin_task, name='admin_task'),
    path('change_password/',change_password,name='change_password'),
    path('change_passwordadmin/', change_passwordadmin, name='change_passwordadmin'),
    path('all_employee/',all_employee, name='all_employee'),


    # path('admin_home', admin_home, name='admin_home'),
    # path('admin1_login' , admin1_login, name='admin1_login'),
]

