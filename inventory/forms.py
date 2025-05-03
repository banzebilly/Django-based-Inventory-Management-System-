
from django import forms
from .models import Shoe

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['country', 'code', 'product', 'cost', 'quantity']

    def __init__(self, *args, **kwargs):
        super(ShoeForm, self).__init__(*args, **kwargs)

        # Set placeholder text for input fields
        self.fields['country'].widget.attrs['placeholder'] = 'Enter your country'
        self.fields['code'].widget.attrs['placeholder'] = 'Enter product code'
        self.fields['product'].widget.attrs['placeholder'] = 'Enter your product'
        self.fields['cost'].widget.attrs['placeholder'] = 'Enter the cost'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter the quantity'

        # Apply consistent Bootstrap styling to all fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
