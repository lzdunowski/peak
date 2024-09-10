# Generated by Django 4.2.10 on 2024-09-09 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRateOnDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nbpApiIntegration.currency')),
            ],
        ),
    ]