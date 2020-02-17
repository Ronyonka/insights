from django.shortcuts import render
from .models import StartUp
from deals.models import FundingInfo
from django.views.generic import TemplateView


# def latest_funding(request):
#     start_up = StartUp.objects.all()