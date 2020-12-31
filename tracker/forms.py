from django import forms


class AddItemForm(forms.Form):
    url = forms.URLField(label="URL to track", max_length=200, required=True)
    requested_price = forms.DecimalField(max_digits=8, decimal_places=2, required=True)