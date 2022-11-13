from django import forms

class OrderForms(forms.Form):
    # Вторым параметром указываем обязательность запорлнения
    # name = forms.CharField(max_length=280,required=False)
    name = forms.CharField(max_length=280)
    phone = forms.CharField(max_length=13)