from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response, redirect, HttpResponse
from attendy_app.form import PeopleForm

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
