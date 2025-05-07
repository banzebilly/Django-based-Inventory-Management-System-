from django.shortcuts import render
from .forms import InvestmentForm, BondForm
# Create your views here.


def finance_home(request):
    return render(request, 'finance/home.html')
    


def investment(request):
    final_amount = None  # Declare it with a default value for GET requests

    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            deposit = form.cleaned_data['deposit']
            interest_rate = form.cleaned_data['interest_rate']
            years = form.cleaned_data['years']
            interest_type = form.cleaned_data['interest_type']

            if interest_type == 'simple':
                final_amount = deposit * (1 + (interest_rate / 100) * years)
            elif interest_type == 'compound':
                final_amount = deposit * ((1 + (interest_rate / 100)) ** years)
        form.save()

    else:
        form = InvestmentForm()

    return render(request, 'finance/investment.html', {
        'form': form,
        'final_amount': final_amount
    })




def bond(request):
    monthly_payment = None

    if request.method == 'POST':
        form = BondForm(request.POST)
        if form.is_valid():
            present_value = form.cleaned_data['present_value']
            interest_rate = form.cleaned_data['interest_rate'] / 100  # Convert % to decimal
            months = form.cleaned_data['months']

            monthly_interest_rate = interest_rate / 12

            if monthly_interest_rate > 0:
                # Amortized monthly payment formula
                monthly_payment = (
                    present_value * monthly_interest_rate * (1 + monthly_interest_rate) ** months
                ) / (
                    (1 + monthly_interest_rate) ** months - 1
                )
            else:
                # If interest rate is 0%
                monthly_payment = present_value / months
    else:
        form = BondForm()

    return render(request, 'finance/bond.html', {
        'form': form,
        'monthly_payment': monthly_payment
    })
