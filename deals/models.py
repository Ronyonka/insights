from django.db import models
from start_ups.models import StartUp

class FundingInfo(models.Model):
    start_up = models.ForeignKey(StartUp, on_delete=models.CASCADE, related_name="start_up")
    round_number = models.IntegerField()
    funded_date = models.DateField()
    round_type = models.CharField(max_length=80, null=False, blank=True)
    investor_name = models.CharField(max_length=80, null=False, blank=True)
    lead_investor = models.BooleanField()
    total_funding_round = models.FloatField()

    
