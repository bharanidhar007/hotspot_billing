from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hotspot, Payment, Withdrawal
from django.db.models import Sum
from vouchers.models import Voucher
from django.http import JsonResponse
import datetime

@login_required
def dashboard(request):
    profile = request.user.profile
    hotspots = Hotspot.objects.filter(owner=profile)
    currency = request.currency
    total_revenue = Payment.objects.filter(hotspot__owner=profile).aggregate(total=Sum('amount'))['total'] or 0
    total_vouchers = Voucher.objects.filter(batch__hotspot__owner=profile).count()
    return render(request, 'billing/dashboard.html', {
        'hotspots': hotspots, 'currency': currency,
        'total_revenue': total_revenue, 'total_vouchers': total_vouchers
    })

@login_required
def dashboard_stats(request):
    profile = request.user.profile
    today = datetime.date.today()
    labels, revenue = [], []
    for i in range(6, -1, -1):
        month = (today.replace(day=1) - datetime.timedelta(days=30*i)).replace(day=1)
        labels.append(month.strftime('%b %Y'))
        start = month
        end = (month + datetime.timedelta(days=32)).replace(day=1)
        total = Payment.objects.filter(hotspot__owner=profile, created__gte=start, created__lt=end).aggregate(total=Sum('amount'))['total'] or 0
        revenue.append(float(total))
    return JsonResponse({'labels': labels, 'revenue': revenue, 'active_users': [0]*len(labels)})

@login_required
def request_withdrawal(request, hotspot_id):
    hotspot = get_object_or_404(Hotspot, id=hotspot_id, owner=request.user.profile)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        dest = request.POST.get('destination')
        Withdrawal.objects.create(hotspot=hotspot, amount=amount, currency=request.user.profile.currency, destination=dest)
        return redirect('billing-dashboard')
    return render(request, 'billing/request_withdrawal.html', {'hotspot': hotspot})

@login_required
def approve_withdrawal(request, wid):
    w = get_object_or_404(Withdrawal, id=wid)
    w.processed = True
    from django.utils import timezone
    w.processed_at = timezone.now()
    w.processed_by = request.user
    w.save()
    return redirect('/admin/')
