from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    national_animal = models.CharField(max_length=255)

class Province(models.Model):
    prov_name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')

class City(models.Model):
    city_name = models.CharField(max_length =255)
    year_founded = models.IntegerField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province')

class Residence(models.Model):
    res_address = models.CharField(max_length = 255)
    year_built = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

class Person(models.Model):
    person_name = models.CharField(max_length = 255)
    age = models.IntegerField()
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name ='residence')
