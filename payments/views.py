from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from billing.models import Payment, Hotspot
from decimal import Decimal
from django.shortcuts import get_object_or_404
import json
from vouchers.utils import create_voucher_for_payment
from . import providers

def send_sms_or_log(number, message):
    # TODO: integrate real SMS gateway
    print(f"SMS to {number}: {message}")
    return True

PROVIDER_DISPATCH = {
    'safaricom_mpesa': providers.handle_mpesa_ke,
    'vodacom_mpesa': providers.handle_mpesa_tz,
    'mtn': providers.handle_mtn,
    'airtel': providers.handle_airtel,
    'tigo_pesa': providers.handle_tigo_pesa,
}

@csrf_exempt
def mobile_money_webhook(request, provider):
    body = json.loads(request.body.decode('utf-8') or "{}")
    handler = PROVIDER_DISPATCH.get(provider)
    if not handler:
        return JsonResponse({'ok': False, 'error': 'Unknown provider'}, status=400)
    data = handler(body)
    hotspot = get_object_or_404(Hotspot, id=data['hotspot_id'])
    amount = Decimal(str(data['amount']))
    currency = data.get('currency', hotspot.owner.currency or 'USD')
    p = Payment.objects.create(
        hotspot=hotspot,
        payer_name=body.get('payer_name',''),
        amount=amount,
        currency=currency,
        provider=data['provider'],
        provider_tx=data.get('transaction_id','')
    )
    voucher = create_voucher_for_payment(hotspot, amount, created_by=hotspot.owner)
    send_sms_or_log(data.get('phone'), f"Your voucher: {voucher.code}")
    return JsonResponse({'ok': True, 'payment_id': p.id, 'voucher': voucher.code})
