from django.shortcuts import render
from deals.models import FundingInfo
from start_ups.models import StartUp

def do_this(request):
    companies = StartUp.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'index.html', context)

def company_profile(request, company_name):
    company = StartUp.objects.get(company_name=company_name)
    funding = FundingInfo.objects.all().filter(start_up__company_name=company.company_name)
    context = {
        'company':company,
        'funding':funding
    }
    return render(request, 'company.html', context)
