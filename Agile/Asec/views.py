from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django import forms
from .models import User
from .models import Committee
from django import forms
from .models import User
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
class NewTaskForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Full Name'}),label="Full name")
    Id =forms.IntegerField(label="ID",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'ID'}))
    task = forms.CharField(label="Assigned Task ",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Assigned Task'}))
    Attendance = forms.CharField(label="Attendence ",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Attendance'}))
    Committee = forms.CharField(label="Committee ",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Committee'}))

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
        return render(request, "General/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]


        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Authentication/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email=email, password= password,first_name=first_name,last_name= last_name)
            user.save()
        except IntegrityError:
            return render(request, "Authentication/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("announcements"))
    else:
        return render(request, "Authentication/register.html")

def show_committee(request, committeeId):
    committee = Committee.objects.get(id=committeeId)
    return render(request, "Committee/show_committee.html",{
        "name":committee.name,
        "description": committee.description,
        "photo": committee.photo
    })


def LoginView(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:

            login(request, user)
            return HttpResponseRedirect(reverse("announcements"))
        else:
            return render(request, "Authentication/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Authentication/login.html")
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

def index(request):
  mymembers = User.objects.all().values()
  template = loader.get_template('Committee/List_of_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context,request))

def add(request):
    committees = Committee.objects.all()

    return render(request, "Committee/Add_member.html", {
        "committees": committees
    })


def addrecord(request):
  x = request.POST['username']
  y = request.POST['email']
  member = User(username=x,email=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = User.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('list'))

def update(request,id):
  mymember = User.objects.get(id=id)
  template = loader.get_template('Committee/Updated_list.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  x = request.POST['username']
  y = request.POST['email']
  member = User.objects.get(id=id)
  member.username = x
  member.email = y
  member.save()
  return HttpResponseRedirect(reverse('index'))

def list_members(request):
    members = User.objects.all().values()
    return render(request,"Committee/List_of_members.html",{"members": members})


def add_member(request):
  mymembers = User.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["username"]
    output += x["email"]
  return HttpResponse(output)

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder':('Username')
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'first_name',
            'placeholder':('First Name')
        }
    )) 
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'last_name',
            'placeholder':('Last Name')
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type':'email',
            'placeholder':('Email')
        }
    ))
    password1 = forms.CharField(max_length=16,widget=forms.PasswordInput(
        attrs={
            # 'class':'form-control',
            'placeholder':'Password'
        }
    ))
    password2 = forms.CharField(max_length=16,widget=forms.PasswordInput(
        attrs={
            # 'class':'form-control',
            'placeholder':'Repeat Password'
        }
    ))
    group_choices = (
        ('M','Manager'),
        ('U','User'),
        ('C','Customer'),   
    )
    groups = forms.ChoiceField(choices=group_choices)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2','groups']
        
def create_register_form(request):
    if request.method == "POST":
        print(request.POST['username'])
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email= form.cleaned_data["email"]
            first_name= form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            password1=form.cleaned_data["password1"]
            password2=form.cleaned_data["password2"]
            groups=form.cleaned_data["groups"]
            return HttpResponseRedirect(reverse("login"))
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "Authentication/register.html", {
                "form": form
            })
    return render(request,"Authentication/register.html" ,
   
               { "form" :UserForm()})