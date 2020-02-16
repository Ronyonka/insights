from django.db import models


class StartUp(models.Model):
    unique_code = models.CharField(max_length=25, unique=True, blank=False, null=False)
    company_name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    linkedin = models.URLField(blank=True, null=True)
    company_website = models.URLField(unique=True, null=False, blank=False)
    hq_city = models.CharField(max_length=80, null=False, blank=False)
    hq_country = models.CharField(max_length=80, null=False, blank=False)
    founded_date = models.DateField()
    sector = models.CharField(max_length=80, null=False, blank=True)
    last_funding_amount = models.FloatField()
    total_funding_amount = models.FloatField()

    def __str__(self):
        return self.company_name


