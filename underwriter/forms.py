from django import forms
from .models import Underwriter, Client, ClassDef


class UnderwriterForm(forms.ModelForm):
    class Meta:
        model = Underwriter
        fields = ('company_name', 'email', 'phone_number', 'address', 'ceo_name', 'ceo_phone_number', 'ceo_email')
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'ceo_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ceo_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'ceo_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'email', 'phone_number', 'address')
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
         }


class ClassDefForm(forms.ModelForm):
    class Meta:
        model = ClassDef
        fields = ('class_of_Business', 'percentage_of_brokerage')
        widgets = {
            'class_of_Business': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter class'}),
            'percentage_of_brokerage': forms.NumberInput(attrs={'class': 'form-control'}),
        }
