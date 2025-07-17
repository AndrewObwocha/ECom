from django.db import models
from django.contrib.auth.models import User
from orderComponent.models import Order

# Create your models here.
class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=100, 
        default="N/A"
    )
    userId = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
    )
    orderId = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title