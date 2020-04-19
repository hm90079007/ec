from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/ ')

    def __str__(self):
        return self.name
        ##インスタンスを生成した際にまず自動的に呼び出すメソッドの事です。
        ##クラスの初期設定などを行うためのメソッドになります。
