from django.contrib import admin
from .models import Product

admin.site.register(Product) # admin site でどのモデルを見るか定義する
