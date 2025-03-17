from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):

        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено. Ответ будет направлен по номеру: {phone}.')
        return render(request, 'contacts.html')


class ProductsListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'


class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products_detail.html'
    context_object_name = 'product'


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        user = self.request.user
        if user == self.object.owner:
            return super().form_valid(form)
        raise PermissionDenied ("У вас нет прав для редактирования этого продукта.")


class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.request.user
        if user == self.object.owner or user.has_perm('catalog.can_unpublish_product'):
            self.object.delete()
            return super().delete(request, *args, **kwargs)
        raise PermissionDenied("У вас нет прав для удаления этого товара.")
