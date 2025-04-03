from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField("ID", primary_key=True)
    email = models.EmailField("E-mail", max_length=128, unique=True)
    first_name = models.CharField("First Name", max_length=128)
    last_name = models.CharField("Last Name", max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "customers"


class Order(models.Model):
    order_id = models.AutoField("ID", primary_key=True)
    product = models.CharField("Product", max_length=128)
    order_date = models.DateField("Order Date", auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return f"Order {self.order_id}: {self.product}"

    class Meta:
        db_table = "orders"
