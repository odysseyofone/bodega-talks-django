from django import forms


class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=180)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
