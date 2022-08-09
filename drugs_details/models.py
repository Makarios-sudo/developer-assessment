
import uuid
from django.db import models

# Create your models here.

class Drug(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    sku = models.CharField(max_length=200, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.CharField(max_length=200, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = "drugs"
        ordering = ["price"]
    
    
    def __str__(self):
        return f"Name:{self.name}, Price:{self.price} "