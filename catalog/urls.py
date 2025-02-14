from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsCreateView, ProductsListView, ProductsDetailView, ProductsUpdateView, \
    ProductsDeleteView, ContactsTemplateView

app_name = CatalogConfig.name


urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='products_detail'),
    path('products/new/', ProductsCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/edit/', ProductsUpdateView.as_view(), name='products_edit'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='products_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
