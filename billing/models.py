from django.db import models
from accounts.models import Profile
from decimal import Decimal
from django.conf import settings

class Hotspot(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    mikrotik_identity = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.identity})"

class Package(models.Model):
    hotspot = models.ForeignKey(Hotspot, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    duration_days = models.IntegerField()
    upload_kbps = models.IntegerField()
    download_kbps = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return f"{self.name} - {self.price}"

class Payment(models.Model):
    hotspot = models.ForeignKey(Hotspot, on_delete=models.SET_NULL, null=True, blank=True)
    payer_name = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10)
    provider = models.CharField(max_length=50)
    provider_tx = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    commission_amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    def save(self, *args, **kwargs):
        if not self.commission_amount:
            pct = Decimal(settings.SYSTEM_COMMISSION_PERCENT) / Decimal(100)
            self.commission_amount = (self.amount * pct).quantize(Decimal('0.01'))
        super().save(*args, **kwargs)

class Withdrawal(models.Model):
    hotspot = models.ForeignKey(Hotspot, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10)
    destination = models.CharField(max_length=255)  # "MTN:+256..." or "Bank:IBAN..."
    requested_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True, blank=True)
    processed_by = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"Withdrawal {self.amount} {self.currency} to {self.destination}"
