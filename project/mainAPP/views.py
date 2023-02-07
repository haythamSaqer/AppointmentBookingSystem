from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import AppointmentForm, DoctorSignUpForm, PatientSignUpForm, PatientLoginForm, DoctorLoginForm
from .models import Appointment


@login_required
def logout_view(request):
    logout(request)
    return redirect('appointments:home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('appointments:home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect.'})
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('appointments:home')
        else:
            error = "The form contains errors. Please correct and submit again."
            return render(request, 'signup.html', {'form': form, 'error': error})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('appointments:home')
        else:
            error = "The form contains errors. Please correct and submit again."
            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = DoctorSignUpForm()
    return render(request, 'signup.html', {'form': form})


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('appointments:home')
        else:
            error = "The form contains errors. Please correct and submit again."
            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = PatientSignUpForm()
    return render(request, 'signup.html', {'form': form})


# @login_required
def home(request):
    # appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'home.html')


def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('appointments:home')
            else:
                error = "Invalid credentials. Please try again."
                return render(request, 'login.html', {'form': form, 'error': error})
        else:
            error = "The form contains errors. Please correct and submit again."
            print(form.errors)
            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = DoctorLoginForm()
    return render(request, 'login.html', {'form': form})


def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('appointments:view_appointments')
            else:
                error = "Invalid credentials. Please try again."
        else:
            error = "The form contains errors. Please correct and submit again."
            print(form.errors)
            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = PatientLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointments:confirm_appointment', pk=appointment.pk)
        else:
            error = "The form contains errors. Please correct and submit again."
            return render(request, 'appointments.html', {'form': form, 'error': error})
    else:
        form = AppointmentForm()
    return render(request, 'appointments.html', {'form': form})


@login_required
def confirm_appointment(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    return render(request, 'confirm_appointment.html', {'appointment': appointment})
