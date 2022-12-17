from django import forms
from store.models import Order


class AddOrderInfoForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["order_by"].disabled = True
    #     self.fields["order_status"].disabled = True
    #     self.fields["phone"].disabled = True

    class Meta:
        model = Order
        fields = ["street", "house", "postal_code", "city", "shipping", "payment_method"]
        widgets = {
            "street": forms.TextInput(attrs={"placeholder": "Street"}),
            "house": forms.TextInput(attrs={"placeholder": "House"}),
            "postal_code": forms.TextInput(attrs={"placeholder": "Postal code"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
            "shipping": forms.RadioSelect(attrs={"class": "form-check-input"}),
            "payment_method": forms.RadioSelect(attrs={"class": "form-check-input"})
        }

