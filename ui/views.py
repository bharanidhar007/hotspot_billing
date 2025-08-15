from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def home_redirect(request):
    return redirect('billing-dashboard')

@login_required
def simple_page(request, title):
    return render(request, 'ui/simple_page.html', {'title': title})
