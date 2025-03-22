from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product
from django.conf import settings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image', ]

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной. Введите корректную цену.')
        return price

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in settings.FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError('Наименование товара содержит запрещенные слова.')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in settings.FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError('Наименование товара содержит запрещенные слова.')
        return description

class ProductsModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['is_published', ]
