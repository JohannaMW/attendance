from django.contrib.auth import authenticate, login
from django.core import serializers
from django.shortcuts import render, render_to_response, redirect, HttpResponse
from .models import People
from .form import PeopleForm
from .form import TeacherForm


def register(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("data")
    else:
        form = PeopleForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def teacher_view(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            check_in_date = request.POST['check_in_date']
            students = People.objects.filter(checked_in=True, check_in_date=check_in_date)
            return render(request, "teacher_home.html", {'students': students})
    else:
        form = TeacherForm()

    return render(request, "teacher_view.html", {'form': form})