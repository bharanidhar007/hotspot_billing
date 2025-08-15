import secrets
from .models import Voucher, VoucherBatch
import io, csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def create_voucher_for_payment(hotspot, amount, created_by=None):
    prefix = 'PM'
    batch = VoucherBatch.objects.create(hotspot=hotspot, prefix=prefix, created_by=created_by, count=1)
    code = prefix + secrets.token_hex(3).upper()
    v = Voucher.objects.create(batch=batch, code=code, amount=amount)
    return v

def vouchers_to_csv(vouchers_qs):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["Voucher Code","Amount","Redeemed","Created At"])
    for v in vouchers_qs:
        writer.writerow([v.code, str(v.amount), v.is_redeemed, v.created_at.isoformat()])
    resp = HttpResponse(buffer.getvalue(), content_type="text/csv")
    resp['Content-Disposition'] = 'attachment; filename="vouchers.csv"'
    return resp

def vouchers_to_pdf(vouchers_qs):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    y = 800
    p.setFont("Helvetica", 12)
    p.drawString(50, y, "Vouchers")
    y -= 30
    for v in vouchers_qs:
        p.drawString(50, y, f"{v.code} — {v.amount} — Redeemed: {v.is_redeemed}")
        y -= 20
        if y < 100:
            p.showPage(); y = 800
    p.save()
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="vouchers.pdf"'
    return response
