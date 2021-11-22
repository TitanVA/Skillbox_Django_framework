from django.db import models

from app_profile.models import User


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Заголовок")
    description = models.CharField(max_length=1000, default="", verbose_name="Описание")
    category = models.ForeignKey("AdvertisementCategory", on_delete=models.CASCADE,
                               verbose_name="Категория")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    price = models.FloatField(default=0, verbose_name="Цена")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    status = models.ForeignKey("AdvertisementStatus", default=None, null=True, on_delete=models.CASCADE,
                               related_name="advertisements", verbose_name="Статус")
    region = models.ManyToManyField("AdvertisementRegion", verbose_name="Регион")
    type = models.ForeignKey("AdvertisementType", default=None, null=True, on_delete=models.CASCADE, verbose_name="Тип")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "advertisements"
        ordering = ["title"]


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class AdvertisementRegion(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name