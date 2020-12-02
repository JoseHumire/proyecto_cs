from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from .forms import *


def welcome(request):
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")
    return redirect('login')


def register(request):
    user_form = UserForm()
    professional_form = ProfessionalForm()
    user_form.fields['username'].help_text = None
    user_form.fields['password1'].help_text = None
    user_form.fields['password2'].help_text = None
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        professional_form = ProfessionalForm(data=request.POST)
        if user_form.is_valid() and professional_form.is_valid():
            user = user_form.save()
            professional = professional_form.save(commit=False)
            professional.user = user
            professional.save()
            Curriculum.objects.create(owner=professional)
            return redirect('login')

    return render(
        request,
        "users/register.html",
        {
            'user_form': user_form,
            'professional_form': professional_form
        }
    )


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(
        request, "users/login.html", {'form': form}
    )


def logout(request):
    do_logout(request)
    return redirect('/')


# Pantalla principal
def home(request):
    return render(request, "home.html")


# Mensajes
def messages(request):
    return render(request, "messages.html")


def add_job(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            professional = Professional.objects.get(user=request.user)
            cv = Curriculum.objects.get(owner=professional)
            job = form.save(commit=False)
            job.cv = cv
            job.save()
            return redirect('home')

    return render(
        request, "add_job.html", {'form': form}
    )


def add_study(request, pk=None):
    if pk:
        study = get_object_or_404(Study, pk=pk)
        if study.cv.owner.user != request.user:
            return HttpResponseForbidden()
    else:
        cv = Curriculum.objects.get(owner=request.user.professional)
        study = Study(cv=cv)
    form = StudyForm(data=request.POST or None, instance=study)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(
        request, "add_study.html", {'form': form}
    )


def employments(request):
    return render(request, "employments.html")
