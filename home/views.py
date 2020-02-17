from django.shortcuts import render
from deals.models import FundingInfo
from start_ups.models import StartUp

def do_this(request):
    companies = StartUp.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'index.html', context)
