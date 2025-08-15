Hotspot Billing (SQLite, non-Docker)
====================================
Features:
- Currency auto-detection via middleware (Cloudflare header, custom header, or user profile)
- Mobile Money webhook placeholders: Safaricom M-Pesa, Vodacom M-Pesa, MTN, Airtel, Tigo Pesa
- 5% commission logic on each Payment
- Withdrawals to bank/mobile money (request + admin approval flow)
- Dashboard with revenue stats
- Voucher generation & export (CSV/PDF)
- User registration capturing business/contact fields
- MikroTik / CoovaChilli config preview

Quickstart:
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
Open http://127.0.0.1:8000/accounts/login/  (or /accounts/register/)

Notes:
- Replace SMS sending and real provider integrations in payments/ with actual gateways.
- Add GeoIP if you want IP-based country detection instead of headers.
- Secure secrets via .env in production (copy .env.example to .env).
