

from django import forms
from .models import Investment, Bond


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['deposit', 'interest_rate', 'years', 'interest_type', ]


    def __init__(self, *args, **kwargs):
        super(InvestmentForm, self).__init__(*args, **kwargs)
        self.fields['deposit'].widget.attrs['class'] = 'form-control'
        self.fields['interest_rate'].widget.attrs['class'] = 'form-control'
        self.fields['years'].widget.attrs['class'] = 'form-control'
        self.fields['interest_type'].widget.attrs['class'] = 'form-control'

        
class BondForm(forms.ModelForm):
    class Meta:
        model = Bond
        fields = ['present_value', 'interest_rate', 'months' ]
    


    
    def __init__(self, *args, **kwargs):
        super(BondForm, self).__init__(*args, **kwargs)
        self.fields['present_value'].widget.attrs['class'] = 'form-control'
        self.fields['interest_rate'].widget.attrs['class'] = 'form-control'
        self.fields['months'].widget.attrs['class'] = 'form-control'
    


