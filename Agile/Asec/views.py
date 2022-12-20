from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django import forms
from .models import User
from .models import Committee_des
# Create your views here.
class NewTaskForm(forms.Form):
    name = forms.CharField(label="full name")
    
    Id =forms.IntegerField(label="Id ")
    task = forms.CharField(label="Assigned Task ")
    Attendance = forms.CharField(label="Attendence ")
    Committee = forms.CharField(label="Committee ")
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:

            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def decription(request):
    return render(request, "Committee/Service.html",{
        "Committee":Committee_des.objects.all()
    })
def committe_main(request):
    return render(request, "Committee/main.html")
def create_form(request):
    if request.method == "POST":

        form = NewTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            id = form.cleaned_data["Id"]
            task = form.cleaned_data["task"]
            Attendance=form.cleaned_data["Attendance"]
            tasks.append("Name"+":"+name+","+"Task" +":"+task+","+"attendance"+":"+Attendance)
            print("\n")
            return HttpResponseRedirect(reverse("submit_form"))
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "Committee/HRForm.html", {
                "form": form
            })
    return render(request,"Committee/HRForm.html" ,
   
               { "form" :NewTaskForm()})
def show_announcements(request):
    if request.method == 'GET':
        return render(request, "Announcements/announcements.html")


tasks=[ ]
def Show_form(request):
   
    return render(request, "Committee/Show_submission.html", {
        "tasks": tasks
    })
    