# orders/models.py
from django.db import models

class Order(models.Model):
    PAYMENT_METHODS = [
        ('mpesa', 'M-Pesa'),
        ('cash', 'Cash on Delivery'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    county = models.CharField(max_length=50)
    pickup_station = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='mpesa')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Order {self.id} by {self.first_name} {self.last_name}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=20, blank=True)
    eggs = models.CharField(max_length=20, blank=True)
    icing = models.CharField(max_length=50, blank=True)
    message_on_cake = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
