from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, ProfileForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        pform = ProfileForm(request.POST)
        if form.is_valid() and pform.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = user.profile
            for f in pform.cleaned_data:
                setattr(profile, f, pform.cleaned_data[f])
            profile.save()
            login(request, user)
            return redirect('billing-dashboard')
    else:
        form = RegistrationForm()
        pform = ProfileForm()
    return render(request, 'accounts/register.html', {'form': form, 'pform': pform})
