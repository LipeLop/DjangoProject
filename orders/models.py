from django.db import models


class Order(models.Model):
    order_id = models.AutoField("ID", primary_key=True)
    order_date = models.DateField("Order Date", auto_now_add=True)
    first_name = models.CharField("First Name", max_length=128)
    last_name = models.CharField("Last Name", max_length=128)

    def __str__(self):
        return f"Order {self.order_id}"

    class Meta:
        db_table = "orders"

    def get_total_cost(self):
        return sum(item.price * item.quantity for item in self.items.all())


from django.db import models


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('cart.Product', on_delete=models.CASCADE)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Quantity", default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    class Meta:
        db_table = "order_items"
