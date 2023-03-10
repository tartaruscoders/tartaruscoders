from django.db import models
from django.contrib.auth.models import User


class Elderly(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    idn_or_ssn = models.IntegerField(max_length=1000, help_text='ID card number', default=None)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    time_credits = models.PositiveIntegerField(default=0)
