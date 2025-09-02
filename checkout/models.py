from django.db import models


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=180)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"Order #{self.id} - {self.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=180)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"
