from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  do_this, name="home"),
]
