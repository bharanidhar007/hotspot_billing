from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class CountryDetectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        cc = None
        # Cloudflare header or custom header can set country code
        if 'CF-IPCountry' in request.META:
            cc = request.META.get('CF-IPCountry')
        if not cc:
            cc = request.META.get('HTTP_X_COUNTRY_CODE')
        # Fallback to user profile
        if not cc and getattr(request, 'user', None) and request.user.is_authenticated:
            profile = getattr(request.user, 'profile', None)
            if profile and profile.country:
                cc = profile.country.code.upper()
        # Default to KE
        if not cc:
            cc = 'KE'
        request.country_code = cc
        request.currency = settings.CURRENCY_MAP.get(cc, 'USD')
