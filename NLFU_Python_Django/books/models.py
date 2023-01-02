from django.db import models

# Create your models here.
class Book(models.Model): # models.Model → 資料表
    name = models.CharField(max_length=255)  # 書名
    author = models.CharField(max_length=255)  # 作者
    isbn = models.CharField(max_length=10, unique=True)  # ISBN，不可重複
    price = models.PositiveIntegerField()  # 價格
    publish_date = models.DateField()  # 出版日期
    description = models.TextField()  # 介紹