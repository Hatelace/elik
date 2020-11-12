from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=150)
    image = models.ImageField("Картинка", upload_to='Category/')
    test = models.CharField("На всякий случай", max_length=150, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField("Название", max_length=200)
    image = models.ImageField("Изображение", upload_to='Products/')
    price = models.SmallIntegerField("Цена")
    value = models.CharField("Вместимость", max_length=50,
                             blank=True, help_text="Для завтраков это описание для напитков вместимость")
    description = models.CharField(
        "Описание", max_length=500, blank=True, help_text="Не обязательное поле")
    test = models.CharField("На всякий случай", max_length=500,
                            blank=True, help_text="Не обязательное поле")
    quantity = models.SmallIntegerField("Количество", default=1)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Order(models.Model):
    order = models.CharField(max_length=500)
    adress = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    networth = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Trdelnik(models.Model):
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50)
    trdelnik_type = models.CharField(max_length=500)
    pomazka_type = models.CharField(max_length=500)
    posypka_type = models.CharField(max_length=500)
    nachinka_type = models.CharField(max_length=500)
    iceCream_type = models.CharField(max_length=500)
    Topping_type = models.CharField(max_length=500)
    Decorations_type = models.CharField(max_length=500)
    Adress_type = models.CharField(max_length=500)

    def __str__(self):
        return self.trdelnik_type
