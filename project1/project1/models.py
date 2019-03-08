from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 255)
    mailing_address = models.CharField(max_length = 255)
    email = models.EmailField(max_length =254)

class Order(models.Model):
    order_num = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name ='customer' )
