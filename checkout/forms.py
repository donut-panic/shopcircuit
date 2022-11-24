from django import forms
from store.models import Order


class AddOrderInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['order_by'].disabled = True
        # self.fields['created'].disabled = True


    class Meta:
        model = Order
        fields = '__all__'

        widgets = {'order_by': forms.Select(attrs={'class': 'form-control text-center bg-white'}),
                   'created': forms.DateTimeInput(attrs={'class': 'form-control text-center bg-white'}, format='%m/%d/%y'),
                   'address_street': forms.Textarea(attrs={'class': 'form-control', 'placeholder':
                       'Please eneter your full adress here', 'rows': 2}),
                   'address_postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                       'Postal-code'}),
                   'address_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                       'City name'}),
                   'shipping': forms.Select(attrs={'class': 'form-control'}),
                   'payment': forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                       'I don\'t know'}),
                   'payment_method': forms.RadioSelect(attrs={'class': 'radio'})
                   }

