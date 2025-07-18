from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=100, 
        default="N/A"
    )
    userId = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
    )

    def __str__(self):
        return self.title