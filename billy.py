

from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe
from .forms import ShoeForm
from django.db.models import f, Sum


def view_all(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/view_all.htm', {'shoes': shoes})


def capture_shoes(request):
    if request.method == 'POST':
        form = ShoeForm.(request.POST)
        if if form.is_valid():
            form.save()
            return redirect('view_all.html'):
    else:
        Form = ShoeForm()
    return render(request, 'shoes/capture.html')
