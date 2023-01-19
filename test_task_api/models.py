from django.db import models

from core.models import User


class Products(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    model_of_product = models.CharField(verbose_name="Модель продукта", max_length=255)
    release = models.DateTimeField(verbose_name="Дата выхода продукта на рынок", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт',
        verbose_name_plural = "Продукты"


class Object(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    email = models.EmailField(verbose_name="Электронная почта", max_length=254, blank=True)
    country = models.CharField(verbose_name="Страна", max_length=100)
    city = models.CharField(verbose_name="Город", max_length=254)
    street = models.CharField(verbose_name="Улица", max_length=300)
    house_number = models.CharField(verbose_name="Номер дома", max_length=20)
    products = models.ForeignKey(
        Products,
        verbose_name='Продукты компании',
        on_delete=models.CASCADE,
        null=True
    )
    staff = models.ForeignKey(
        User,
        verbose_name="Сотрудники",
        on_delete=models.PROTECT,
    )
    supplier = models.ForeignKey(
        'self',
        verbose_name="Поставщик",
        on_delete=models.SET_NULL,
        null=True
    )
    arrears = models.FloatField(verbose_name="Задолженность", default=0.0)
    level = models.IntegerField(verbose_name="Уровень", default=0)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now_add=True)

    class TypeObject(models.IntegerChoices):
        factory = 1, "Фабрика"
        distributor = 2, "Дистрибьютор"
        dealership = 3, "Дилерский центр"
        large_retail_chain = 4, "Большая розничная сеть"
        individual_entrepreneur = 5, "Индивидуальный предприниматель"

    object_type = models.PositiveSmallIntegerField(
        verbose_name="Тип объекта", choices=TypeObject.choices
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объект сети"
        verbose_name_plural = "Объекты сети"
