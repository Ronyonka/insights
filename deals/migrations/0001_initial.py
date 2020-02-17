# Generated by Django 3.0.3 on 2020-02-16 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('start_ups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('funded_date', models.DateField()),
                ('round_type', models.CharField(blank=True, max_length=80)),
                ('investor_name', models.CharField(blank=True, max_length=80)),
                ('lead_investor', models.BooleanField()),
                ('total_funding_round', models.FloatField()),
                ('start_up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_up', to='start_ups.StartUp')),
            ],
        ),
    ]
