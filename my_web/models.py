
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.IntegerField(unique=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.number}"


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    customer_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Open")

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.dish.name
