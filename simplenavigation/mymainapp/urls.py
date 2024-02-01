from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'mymainapp'

urlpatterns = [
        path("home/", TemplateView.as_view(template_name="mymainapp/home.html"), name="home"),
        path("wherenext/", views.wherenext, name="wherenext")
]