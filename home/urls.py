from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home",views.home, name="home"),
    path("reg",views.reg),
    path("log",views.log),
]
