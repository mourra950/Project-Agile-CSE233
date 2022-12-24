from django.urls import path
from . import views

# our site url patterns
urlpatterns=[
    path("login", views.LoginView, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("HR_form", views.create_form, name="HR_form"),
    path("main", views.committe_main, name="main"),
    path("announcements", views.show_announcements, name="announcements"),
    path("show_committee/<int:committeeId>", views.show_committee, name="HR_committee"),
    path("add/", views.add, name="add"),
    path("list",views.list_members,name="list"), 
    path('delete/<int:id>', views.delete, name='delete'),

    path("submit_form", views.Show_form, name="submit_form"), # Msh fahemha
    path("Members", views.add_member, name="Members"), # Msh m7tagenha
    path('add/addrecord/', views.addrecord, name='addrecord'), # error

    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

]