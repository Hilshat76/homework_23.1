from django.shortcuts import render, get_object_or_404

from catalog.utils.add_data import add_to_json_file
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog.html', context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products_detail.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(name, phone, message)
        add_to_json_file(name, phone, message)

    return render(request, 'contacts.html')
