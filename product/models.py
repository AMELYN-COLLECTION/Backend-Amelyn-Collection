from django.db import models

class Product(models.Model):
    SIZE_CHOICES = [
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
    ]
    
    nameProduct = models.CharField(max_length=100)
    priceProduct = models.IntegerField()
    imageProduct = models.ImageField(upload_to="upload/menu/")
    descProduct = models.CharField(max_length=100)
    sizeProduct = models.CharField(max_length=2, choices=SIZE_CHOICES)
    stockProduct = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    