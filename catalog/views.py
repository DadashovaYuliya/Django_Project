from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

from catalog.forms import ProductForm, ProductsModeratorForm
from catalog.models import Product, Category
from catalog.services import get_products_from_cache, get_products_by_category


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

    def get_queryset(self):
        return get_products_from_cache()


class ProductsCategoryListView(ListView):
    model = Product
    template_name = 'products_category_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')

        if category_id:
            category = get_object_or_404(Category, id=category_id)
            context['category'] = category

        return context

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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductsModeratorForm
        raise PermissionDenied ("У вас нет прав для редактирования этого продукта.")


class ProductsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user.has_perm("catalog.delete_product") or user == product.owner
