from django.db import models
from django.conf import settings
from mamazon.models import Product

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
#    context_object_name = 'carts_list'#臨時
    user =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE) #Many to one たくさんのカートそれぞれに一つのユーザー. nullはDB上の値、blankは登録フォーム上の値
    products = models.ManyToManyField(Product, blank=True) #　Many to Many たくさんのカートそれぞれにたくさんの商品
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2) #小数点OKフィールド（詳細設定）
    created = models.DateTimeField(auto_now_add=True)#作られた時間だけ
    updated = models.DateTimeField(auto_now=True) #更新された時間も表示する
