from django.db import models

class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
    
    imageProduct = models.ImageField(upload_to="upload/menu/")
    nameProduct = models.CharField(max_length=100)
    descProduct = models.CharField(max_length=100)
    sizeProduct = models.CharField(max_length=2, choices=SIZE_CHOICES)
    stockProduct = models.PositiveIntegerField()
    priceProduct = models.IntegerField()
    
    def __str__(self):
        return self.name
    