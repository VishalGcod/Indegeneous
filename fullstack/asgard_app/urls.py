from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^asgard/$', views.show_data, name="show_data"),
]