from django.db import models
from billing.models import Hotspot

class VoucherBatch(models.Model):
    hotspot = models.ForeignKey(Hotspot, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=6, default="VT")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('accounts.Profile', null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=0)

class Voucher(models.Model):
    batch = models.ForeignKey(VoucherBatch, on_delete=models.CASCADE, related_name='vouchers')
    code = models.CharField(max_length=64, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_redeemed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
