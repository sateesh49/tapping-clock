from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import Holiday

# Create your views here.

def index(request) :
    return render(request,'index.html')

def registration(request) :
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user = user, empcode=ec)
            Holiday.objects.create(user=user)

            error='no'
        except:
            error='yes'

    return render(request,'registration.html', locals())


def emp_login(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error='no'
        else:
            error='yes'
    return render(request,'emp_login.html', locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')




def profile(request) :
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)

    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender
        #employee.user.first_name = fn

        if jdate:
            employee.joiningdate = jdate


        try:
            employee.save()
            employee.user.save()

            error='no'
        except:
            error='yes'

    return render(request,'profile.html', locals())

def admin_login(request):
    return render(request,'admin_login.html')

def admin_login(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error="yes"
    return render(request,'admin_login.html', locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')



def holidays(request):
    return render(request,'holidays.html')


def holidays(request) :
    error = ""
    if request.method == "POST":
        date = request.POST['date']
        hn = request.POST['holiday_name']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user = user, empcode=ec)
            Holiday.objects.create(user=user)

            error='no'
        except:
            error='yes'

    return render(request,'registration.html', locals())







def admin_holidays(request):
    return render(request,'admin_holidays.html')



from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def emp_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        assigned_to = request.POST['assigned_to']

        task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            assigned_to=assigned_to
        )

        # Do additional processing as needed

    return render(request, 'emp_task.html')


def admin_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        assigned_to = request.POST['assigned_to']

        task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            assigned_to=assigned_to
        )

        # Do additional processing as needed

    return render(request, 'admin_task.html')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user

    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error='no'
            else:
                error ="not"
        except:
            error = "yes"
    return render(request,'change_password.html', locals())



def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user

    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error='no'
            else:
                error ="not"
        except:
            error = "yes"
    return render(request,'change_passwordadmin.html', locals())


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request,'all_employee.html',locals())























'''
def holidays(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    holidays = Holiday.objects.get(user = user)

    return render(request, 'holidays.html', locals())


def admin_holidays(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    holiday = Holiday.objects.get(user=user)

    return render(request, 'admin_holidays.html', locals())

'''



