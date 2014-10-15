from django.contrib.auth import authenticate, login
from django.core import serializers
from django.shortcuts import render, render_to_response, redirect, HttpResponse
from .models import People
from .forms import PeopleForm
from .forms import TeacherForm
from django.template import RequestContext
from attendy_app.forms import PeopleForm
from django.db.models import Max
from attendy_app.forms import StudentForm
from attendy_app.models import People
from django.core import serializers

def home(request):
    return render_to_response("home.html", {}, context_instance = RequestContext(request))

def get_mayor(request):
    highest = People.objects.all().aggregate(Max('check_in_counter')).get('check_in_counter__max')
    print highest
    mayor = People.objects.filter(check_in_counter=highest)
    data = serializers.serialize('json', mayor)
    return HttpResponse(data, content_type='application/json')


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
                    return redirect("home")
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

def check_in(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, "check_in.html", {
        'form': form,
    })
