# Generated by Django 3.0.3 on 2020-02-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_ups', '0002_auto_20200217_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='last_funding_amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='total_funding_amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]