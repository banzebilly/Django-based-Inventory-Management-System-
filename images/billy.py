




def re_stock(request):
    shoe = Shoe.objects.order_by('quantity').first()
    if request.method == 'POST':
        qty_to_add = int(request.POST.get('quantity'))
        shoe.quantity += qty_to_add
        shoe.save()
        return redirect('view_all')
    return render(request, 'shoes/restock.html', {'shoe': shoe})




def value_per_item(request):
    shoes = Shoe.objects.all()
    values = [(shoe, shoe.cost * shoe.quantity) for shoe in shoes]
    return render(request, 'shoes/value.html', {'values': values})