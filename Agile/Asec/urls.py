from django.urls import path
from . import views

# our site url patterns
urlpatterns=[
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("Committee", views.decription, name="Committee"),
    path("main", views.committe_main, name="main"),
    path("HR_form", views.create_form, name="HR_form"),
    path("submit_form", views.Show_form, name="submit_form"),
    path("announcements", views.show_announcements, name="show_announcements"),
    path("Members", views.add_member, name="Members"),
    path("list",views.list_members,name="list"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
]