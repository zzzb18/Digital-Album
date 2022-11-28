from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name="home"),
    path('login/',views.LoginPage,name="login"),
    path('register/',views.RegisterPage,name="register")
]
