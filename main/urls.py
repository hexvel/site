from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('about', views.about_us, name="about"),
    path('authorization', views.authorize, name="login"),
]