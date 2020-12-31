from django import forms


class ItemForm(forms.Form):
    url = forms.URLField(label="URL to track", max_length=200)
    requested_price = forms.DecimalField(max_digits=8, decimal_places=2)