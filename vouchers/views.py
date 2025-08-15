from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Voucher, VoucherBatch
from .utils import vouchers_to_csv, vouchers_to_pdf
from billing.models import Hotspot

@login_required
def voucher_list(request, hotspot_id):
    hotspot = get_object_or_404(Hotspot, id=hotspot_id, owner=request.user.profile)
    vouchers = Voucher.objects.filter(batch__hotspot=hotspot).order_by('-created_at')
    return render(request, 'vouchers/list.html', {'vouchers': vouchers, 'hotspot': hotspot})

@login_required
def export_vouchers_csv(request, hotspot_id):
    hotspot = get_object_or_404(Hotspot, id=hotspot_id, owner=request.user.profile)
    vouchers = Voucher.objects.filter(batch__hotspot=hotspot).order_by('-created_at')
    return vouchers_to_csv(vouchers)

@login_required
def export_vouchers_pdf(request, hotspot_id):
    hotspot = get_object_or_404(Hotspot, id=hotspot_id, owner=request.user.profile)
    vouchers = Voucher.objects.filter(batch__hotspot=hotspot).order_by('-created_at')
    return vouchers_to_pdf(vouchers)
