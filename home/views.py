from django.shortcuts import render
from deals.models import FundingInfo
from start_ups.models import StartUp

def do_this(request):
    try:
        companies = StartUp.objects.all()
    except StartUp.DoesNotExist:
        companies = []
    context = {
        'companies': companies
    }
    return render(request, 'databases.html', context)

def company_profile(request, company_name):
    try:
        company = StartUp.objects.get(company_name=company_name)
        funding = FundingInfo.objects.all().filter(start_up__company_name=company.company_name)
    except StartUp.DoesNotExist:
        company = []
        funding = []
    
    context = {
        'company':company,
        'funding':funding
    }
    return render(request, 'company.html', context)