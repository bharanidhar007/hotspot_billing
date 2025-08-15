from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    whatsapp = models.CharField(max_length=32, blank=True)
    business_name = models.CharField(max_length=200, blank=True)
    customer_care_number = models.CharField(max_length=32, blank=True)
    address = models.TextField(blank=True)
    country = CountryField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        from django.conf import settings
        if self.country:
            self.currency = settings.CURRENCY_MAP.get(self.country.code, self.currency or "USD")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} profile"
