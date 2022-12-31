import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django import forms
from .models import User, announcements
from .models import Committee
from django import forms
from .models import User,Role,Urls,announcements,Tracker
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
# Create your views here.
class NewTaskForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Full Name','list':'names'}),label="Full name")
    Id =forms.IntegerField(label="ID",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'ID'}))
    task = forms.CharField(label="Assigned Task ",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Assigned Task'}))
    Attendance = forms.CharField(label="Attendence ",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Attendance'}))
    Committee = forms.CharField(label="Committee ",widget=forms.TextInput(attrs={'class': 'form-control form-floating mb-3','placeholder':'Committee'}))


    
def is_allowed(request, urlName):
    if request.user.is_anonymous:
        return False
    else:
        roleId = Role.objects.get(id= request.user.roleId.pk)
        url = Urls.objects.get(name= urlName)  

        return url.role_set.filter(pk=roleId.pk).exists()


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        committeeId = request.POST["committeeId"]
        try:
            committee = Committee.objects.get(id=committeeId)
        except ValueError:
            return render(request, "Authentication/register.html", {
                "message": "Please select a Committee",
                'committees': Committee.objects.all()
            })

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Authentication/register.html", {
                "message": "Passwords must match.",
                'committees': Committee.objects.all()
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email=email, password= password,first_name=first_name,last_name= last_name,roleId=Role.objects.get(id=3),committeeId=committee )
            user.save()
        except IntegrityError:
            return render(request, "Authentication/register.html", {
                "message": "Username already taken.",
                'committees': Committee.objects.all()
            })
        login(request, user)
        return HttpResponseRedirect(reverse("announcements"),{
            "announcements":announcements
        })
    else:
        return render(request, "Authentication/register.html",{
            'committees': Committee.objects.all()
        })

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
            return HttpResponseRedirect(reverse("announcements"),{
                "announcements":announcements.objects.all()
            })
        else:
            return render(request, "Authentication/login.html", {
                "message": "Invalid username and/or password.",
                "announcements":announcements.objects.all()
            })
    else:
        return render(request, "Authentication/login.html",{
            "announcements":announcements.objects.all()
        })
def committe_main(request):
    return render(request, "Committee/main.html",{
        'committees':Committee.objects.all()
    })

def create_form(request):
    if is_allowed(request,'HR_form'):
        if request.method == "POST":
            id = request.user.id
            task = request.POST["task"]
            description =request.POST["description"]
            attendance = request.POST.get('attendance', False)
            
            try:
                user = User.objects.get(id=id)
            except ValueError:
                return render(request, "Committee/HRForm.html")
            tracker = Tracker(user= user, task=task,attendance=attendance,description=description)
            tracker.save()
            return HttpResponseRedirect(reverse("HR_form"))

            
            
        else:
            return render(request,"Committee/HRForm.html")
    else:
        return HttpResponse("<h2>Page requires admin previliges</h2>")




def show_announcements(request):
    if request.method == 'GET':
        return render(request, "Announcements/announcements.html")

def about_us_view(request):
    if request.method == 'GET':
        return render(request, "General/about_us.html")

def tracker(request):
    if is_allowed(request,'tracker'):

        return render(request, "Committee/show_tracker.html", {
            "trackers": Tracker.objects.all()
        })
    else:
        return HttpResponse("<h2>Page requires admin previliges</h2>")
    

def index(request):
  members = User.objects.all().values()
  template = loader.get_template('Admin/List_of_members.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context,request))

def add(request):
    
    if request.method == 'POST':
        if is_allowed(request,'add'):
            username = request.POST["username"]
            email = request.POST["email"]
            first_name = request.POST["firstName"]
            last_name = request.POST["lastName"]
            committeeId = request.POST["committeeId"]
            roleId = request.POST["roleId"]

            try:
                committee = Committee.objects.get(id=committeeId)
                role = Role.objects.get(id= roleId)
            except ValueError:
                return render(request, "Admin/Add_member.html", {
                    "message": "Please select a Committee/Role",
                    "committees": Committee.objects.all(),
                    "roles": Role.objects.all()
                })

            # Ensure password matches confirmation
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "Admin/Add_member.html", {
                    "message": "Passwords must match.",
                    "committees": Committee.objects.all(),
                    "roles": Role.objects.all()
                })

            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email=email, password= password,first_name=first_name,last_name= last_name,roleId=role,committeeId=committee )
                user.save()
            except IntegrityError:
                return render(request, "Admin/Add_member.html", {
                    "message": "Username already taken.",
                    "committees": Committee.objects.all(),
                    "roles": Role.objects.all()
                })
            return HttpResponseRedirect(reverse("announcements"))
        else:
            return HttpResponse("<h2>Page requires admin previliges</h2>")

    else:
        if is_allowed(request,'add'):
            committees = Committee.objects.all()

            return render(request, "Admin/Add_member.html", {
                "committees": committees,
                "roles": Role.objects.all()
            })
        else:
            return HttpResponse("<h2>Page requires admin previliges</h2>")




def delete(request, id):
    if is_allowed(request,'delete'):
        member = User.objects.get(id=id)
        member.delete()
        return HttpResponseRedirect(reverse('list'))
    else:
        return HttpResponse("<h2>Page requires admin previliges</h2>")

def update(request,id):
    if is_allowed(request,'update'):
        if request.method == 'GET':
            member = User.objects.get(id=id)
            
            return render(request, "Admin/update_member.html", {
                    "member": member,
                    "roles":Role.objects.all(),
                    "committees": Committee.objects.all()
                })
        elif request.method == 'POST':
            first_name = request.POST['firstName']
            last_name = request.POST['lastName']
            username = request.POST['username']
            email = request.POST['email']
            roleId = request.POST['roleId']
            commiteeId = request.POST['committeeId']
            
            role = Role.objects.get(id = roleId)
            committee = Committee.objects.get(id = commiteeId)
            member = User.objects.get(id=id)

            member.first_name = first_name
            member.last_name = last_name
            member.username = username
            member.email = email
            member.roleId = role
            member.committeeId = committee
            member.save()
            return HttpResponseRedirect(reverse('announcements'))
    else:
        return HttpResponse("<h2>Page requires admin previliges</h2>")


def list_members(request):
    if is_allowed(request,'list'):
        members = User.objects.all()
        return render(request,"Admin/List_of_members.html",{"members": members})
    else: 
        return HttpResponse("<h2>Page requires admin previliges</h2>")


def admin(request):
    if request.method == 'POST' :
        name= request.POST['name']
        description= request.POST['description']
        link= request.POST['Fblink']
        ann = announcements(name=name,description=description,facebookLink=link)
        ann.save()
        return HttpResponseRedirect(reverse('announcements'),{
            'announcements':announcements.objects.all()
        })
    else: 
        return render(request,"Announcements/admin_page.html")
def events(request):
    if request.method == 'GET':
        return render(request,"Announcements/announcements.html",{"announcements": announcements.objects.all()})


        



    
