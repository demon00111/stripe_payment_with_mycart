from django import forms
from .models import Products

class Productform(forms.ModelForm):
    name = forms.CharField(max_length=100)
    quantity = forms.CharField(max_length=100)
    currency = forms.CharField(max_length=100)
    amount = forms.CharField(max_length=100)
    img = forms.FileField()



    class Meta:
        model = Products
        fields = '__all__'  

