from django.db import models

class Critic(models.Model):
    name = models.CharField(max_length=255)
    comapny = models.CharField(max_length =255)

class Pub(models.Model):
    pub_name = models.CharField(max_length=255)
    issue = models.IntegerField()

class Restaurant(models.Model):
    res_name = models.CharField(max_length=255)
    address = models.CharField(max_length =255)

class Review(models.Model):
    rev_name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    comapny = models.CharField(max_length =255)
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE, related_name = 'critic')
    pub = models.ForeignKey(Pub, on_delete=models.CASCADE, related_name = 'pub')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name = 'restaurant')

   
