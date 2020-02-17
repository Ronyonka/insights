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

    def __str__(self):
        return self.start_up.company_name + ", Round " + str(self.round_number)+ " funding."

    def save(self, *args, **kwargs):
        company = self.start_up.company_name
        funding = FundingInfo.objects.filter(start_up__company_name=company).order_by('funded_date')
        if len(funding)>0:
            self.start_up.last_funding_amount = self.total_funding_round
            self.start_up.total_funding_amount += self.total_funding_round
        else:
            self.start_up.last_funding_amount = self.total_funding_round
            self.start_up.total_funding_amount = self.total_funding_round
        self.start_up.save()
        super(FundingInfo, self).save(*args, **kwargs)

    def get_start_up(self):
        company = self.start_up.company_name
        funding = FundingInfo.objects.filter(start_up__company_name=company).order_by('funded_date')
        return funding

    def delete(self):
        company = self.start_up.company_name
        funding = FundingInfo.objects.filter(start_up__company_name=company).order_by('funded_date')
        if funding:
            funding_amounts = [i.total_funding_round for i in funding]
            if len(funding_amounts >1):
                self.start_up.last_funding_amount = funding_amounts[len(funding_amounts)-2]
            else:
                self.start_up.last_funding_amount = 0.00
            self.start_up.total_funding_amount = self.start_up.total_funding_amount- self.total_funding_round
        self.start_up.save()
        super(FundingInfo, self).delete()

    # def last_funding_round(self):
        
    #     return self.save()

    
