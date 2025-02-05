from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_views, contacts_views

app_name = CatalogConfig.name


urlpatterns = [
    path('home/', home_views, name='home'),
    path('contacts/', contacts_views, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
