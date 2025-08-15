from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    whatsapp = forms.CharField(required=False)
    business_name = forms.CharField(required=False)
    customer_care_number = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    country = CountryField().formfield(widget=CountrySelectWidget())

    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','whatsapp','business_name','customer_care_number','address','country']
