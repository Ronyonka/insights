from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  do_this, name="home"),
    path('<company_name>', company_profile, name="company"),
]