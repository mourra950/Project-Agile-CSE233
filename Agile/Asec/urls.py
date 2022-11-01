from django.urls import path
import views


# our site url patterns
urlpatterns=[
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
]