from django.db import models

# Create your models here.
class StockIndex(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    url = models.CharField(max_length=2048)
    def __str__(self):
        return self.name