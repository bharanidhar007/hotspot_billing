from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def mikrotik(request):
    # Placeholder Mikrotik/CoovaChilli config script preview
    script = """
/ip hotspot profile add name=hsprof1 hotspot-address=10.0.0.1 html-directory=hotspot
/ip pool add name=hs-pool ranges=10.0.0.2-10.0.0.254
/ip hotspot add name=hotspot1 interface=wlan1 address-pool=hs-pool profile=hsprof1
"""
    return render(request, 'devices/mikrotik.html', {'script': script})

@login_required
def equipment(request):
    return render(request, 'devices/equipment.html')
