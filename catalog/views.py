from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# def home_views(request):
#     return render(request, 'home.html')

class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):

        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено. Ответ будет направлен по номеру: {phone}.')
        return render(request, 'contacts.html')

# def contacts_views(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено. Ответ будет направлен по номеру: {phone}.')
#     return render(request, 'contacts.html')


class ProductsListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
# def products_list(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'products_list.html', context)

class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'
    context_object_name = 'product'
# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'products_detail.html', context)


class ProductsCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'category', 'price', 'image']
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductsUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'price', 'image']
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('catalog:products_list')
#     else:
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'add_product.html', context)