from unittest import SkipTest

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory, Form
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from django.template.context_processors import request

from .models import *
from .forms import CreateStudentForm
from .forms import CreateLecturerForm
from .forms import CreateAdminForm
from .forms import ProfileForm
from .models import Class
from .models import Consultation
from .models import Lecturer
from .models import Department
from .models import Student
from . models import UserProfile
from .forms import ProfileForm,StudentDetForm,ConsultationBooking,LecturerDetForm,ClassForm


def registerLecturer_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateLecturerForm()
        if request.method == 'POST':
            form = CreateLecturerForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for ' + user)

                return redirect('loginLec')

        context = {'form': form}
        return render(request, 'accounts/registerLecturer.html', context)


def registerStudent_page(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = CreateStudentForm()
            if request.method == 'POST':
                form = CreateStudentForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account successfully created for ' + user)

                    return redirect('loginStud')

            context = {'form': form}
            return render(request, 'accounts/registerStudent.html', context)


def registerAdmin_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateAdminForm()
        if request.method == 'POST':
            form = CreateAdminForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for ' + user)

                return redirect('loginLec')

        context = {'form': form}
        return render(request, 'accounts/registerAdmin.html', context)


def loginLecturer_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect!')

        context = {}
        return render(request, 'accounts/loginLecturer.html', context)

def loginStudent_page(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username OR password is incorrect!')

            context = {}
            return render(request, 'accounts/loginStudent.html', context)


def loginAdmin_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect!')

        context = {}
        return render(request, 'accounts/loginAdmin.html', context)


def logout_user(request):
    logout(request)
    return redirect('welcome_page')


@login_required(login_url='login')
def home(request):
    displayclass = Class.objects.all()
    return render(request, 'accounts/home.html',
                  {'Class':displayclass})


@login_required(login_url='login')
def view_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def consultation_booking(request):
    displaybookings = Consultation.objects.all()
    return render(request, 'accounts/bookings.html',
                  {'Consultation':displaybookings})


@login_required(login_url='login')
def insert_booking(request):
    form = ConsultationBooking()

    if request.method == 'POST':
        form = ConsultationBooking(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been made sucessfully..!')
    context = {'form': form}

    return render(request,'accounts/consultation_booking.html', context)




@login_required(login_url='login')
def lecturer_details(request):
    form = LecturerDetForm()

    if request.method == 'POST':
        form = LecturerDetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your lecturer details have been stored sucessfully..!')
    context = {'form': form}
    return render(request, 'accounts/lecturer_details.html',context)


@login_required(login_url='login')
def student_details(request):

    form = StudentDetForm()

    if request.method == 'POST':
        form=StudentDetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your student details have been stored sucessfully..!')
    context = {'form': form}

    return render(request, 'accounts/student_details.html',context)


@login_required(login_url='login')
def showdept(request):
    deptdisplay = Department.objects.all()
    return render (request,"accounts/lecturer_details.html",{'Department':deptdisplay})


def welcome_page(request):
    return render(request,'accounts/welcome_page.html')

def T_and_C(request):
    return render(request,'accounts/Terms_and_Conditions.html')


@login_required(login_url='login')
def ClassInsert(request):
    form = ClassForm()

    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your class details have been stored sucessfully..!')

    context = {'form': form}

    return render(request,"accounts/class.html",context)


@login_required(login_url='login')
def Profile(request):

    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile details have been stored sucessfully..!')

    context = {'form':form}
    return render(request,'accounts/profile.html',context)




