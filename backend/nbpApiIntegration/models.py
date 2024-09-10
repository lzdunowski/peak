import datetime

from django.db import models
from django.utils import timezone

class Currency(models.Model):
    name_text = models.CharField(max_length=200)
    def __str__(self):
        return self.name_text

class ExchangeRateOnDay(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)
    date = models.DateTimeField("date")
    def __str__(self):
        return str(self.rate)
    def was_checked_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
    