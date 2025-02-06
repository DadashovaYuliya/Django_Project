
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from catalog.models import Product, ProductForm


def home_views(request):
    return render(request, 'home.html')


def contacts_views(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено. Ответ будет направлен по номеру: {phone}.')
    return render(request, 'contacts.html')


def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products_list.html', context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'products_detail.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:products_list')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'add_product.html', context)