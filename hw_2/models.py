from django.db import models
from django.db.models import F, Sum


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Имя клиента: {self.name}, email: {self.email}, номер телефона: {self.phone}, адрес: {self.address}, дата регистрации: {self.registration_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Название товара: {self.name}, описание: {self.description}, цена: {self.price}, количество: {self.count}, дата поступления: {self.create_date}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_sum = models.DecimalField(max_digits=8, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Клиент: {self.client.name}, товары: {self.products.name}, сумма покупки: {self.order_sum}, дата заказа: {self.create_date}'

