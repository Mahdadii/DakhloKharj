from django.contrib.auth.models import User
from django.db import models

from django.db import models


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255, default=None)
    date = models.DateTimeField(default=None)
    amount = models.BigIntegerField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return '{}-{}'.format(self.date, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255, default=None)
    date = models.DateTimeField(default=None)
    amount = models.BigIntegerField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return '{}-{}'.format(self.date,self.amount)
