from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    '''Получает данные по списку продуктов из кэша, а если кэш пуст, то из БД'''
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)
