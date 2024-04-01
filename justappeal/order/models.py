# from django.db import models
# from contents.models import Ticket, Gift
# class Order(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order by {self.name} at {self.created_at}"

# class OrderedItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     ticket = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE)
#     gift = models.ForeignKey(Gift, null=True, blank=True, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.quantity} x {self.ticket or self.gift} in order {self.order}"
