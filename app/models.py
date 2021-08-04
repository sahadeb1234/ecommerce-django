from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinValueValidator
STATE_CHOICES = (
    ('State No. 1', 'State No. 1'),
      ('State No. 2', 'State No. 2'),
        ('State No. 3', 'State No. 3'),
          ('State No. 4', 'State No. 4'),
           ('State No. 5', 'State No. 5'),
              ('State No. 6', 'State No. 6'),
                ('State No. 7', 'State No. 7')

)

class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (

    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Ware'),
    ('BW', 'Bottom Wear'),
    
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    descriptin = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    Product_imgae  = models.ImageField(upload_to = 'productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.id)



STATUS_CHOICES = (

    ('Accepted', 'Accepted'),
      ('Packed', 'Packed'),
      ('On the way', 'On the  way '),
        ('Delivered', 'Delivered'),
          ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
      User = models.ForeignKey(User, on_delete= models.CASCADE)
      Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      Product = models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity = models.PositiveBigIntegerField(default=1)
      odrder_date = models.DateTimeField(auto_now_add=True)
      status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')





