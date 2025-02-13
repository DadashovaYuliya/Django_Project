from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts_views, products_list, home_views, products_detail, add_product

app_name = CatalogConfig.name


urlpatterns = [
    path('', products_list, name='products_list'),
    path('contacts/', contacts_views, name='contacts'),
    path('products/<int:pk>/', products_detail, name='products_detail'),
    path('add_product/', add_product, name='add_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
