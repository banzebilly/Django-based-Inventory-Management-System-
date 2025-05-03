from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe
from .forms import ShoeForm  # You'll create a form
from django.db.models import F, Sum

# View all shoes
def view_all(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/view_all.html', {'shoes': shoes})

# Add new shoe
def capture_shoes(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all')
    else:
        form = ShoeForm()
    return render(request, 'shoes/capture.html', {'form': form})

# Find and restock shoe with lowest quantity
def re_stock(request):
    shoe = Shoe.objects.order_by('quantity').first()
    if request.method == 'POST':
        qty_to_add = int(request.POST.get('quantity'))
        shoe.quantity += qty_to_add
        shoe.save()
        return redirect('view_all')
    return render(request, 'shoes/restock.html', {'shoe': shoe})

# Search shoe by code
def search_shoe(request):
    code = request.GET.get('code')
    shoe = Shoe.objects.filter(code=code).first()
    return render(request, 'shoes/search.html', {'shoe': shoe})

# Value per item
def value_per_item(request):
    shoes = Shoe.objects.all()
    values = [(shoe, shoe.cost * shoe.quantity) for shoe in shoes]
    return render(request, 'shoes/value.html', {'values': values})

# Highest quantity
def highest_qty(request):
    shoe = Shoe.objects.order_by('-quantity').first()
    return render(request, 'shoes/highest.html', {'shoe': shoe})
