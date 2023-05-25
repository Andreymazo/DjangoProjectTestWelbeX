import random
import string

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from cargo.management.commands.create_number import unik_number_creation

NULLABLE = {'blank': True, 'null': True}


class Cargo(models.Model):

    slug = models.CharField(default=unik_number_creation, editable=False)
    # location_pick_up = models.CharField(max_length=50, verbose_name="Место приема")
    latitude_pick_up = models.DecimalField(max_digits=7, decimal_places=5)
    longtitude_pick_up = models.DecimalField(max_digits=7, decimal_places=5)
    # location_delivery = models.CharField(max_length=50, verbose_name="Место доставки")
    latitude_delivery = models.DecimalField(max_digits=7, decimal_places=5)
    longtitude_delivery = models.DecimalField(max_digits=7, decimal_places=5)
    weigh = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                verbose_name='Вес', **NULLABLE)
    description = models.CharField(max_length=150, verbose_name="Oписание", **NULLABLE)


class Locations(models.Model):
    city = models.CharField(max_length=50, verbose_name="Место доставки")
    state = models.CharField(max_length=50, verbose_name="Место доставки")
    zip = models.CharField(max_length=50, verbose_name="почтовый индекс")
    latitude = models.CharField(max_length=50, verbose_name="Место доставки")
    longtitude = models.CharField(max_length=50, verbose_name="Место доставки")


class Car(models.Model):
    # id = models.IntegerField(primary_key=True)
    unik_number = models.CharField(default=unik_number_creation, editable=False)
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    longtitude = models.DecimalField(max_digits=7, decimal_places=5)

    # location = models.PointField(geography=True, spatial_index=True)

# https://stackoverflow.com/questions/48388366/i-want-to-add-a-location-field-in-django-model-which-take-location-input-by-putt\
# https://realpython.com/location-based-app-with-geodjango-tutorial/
# https://raphael-leger.medium.com/django-handle-latitude-and-longitude-54a4bb2f6e3b

# p = Point(85.3240, 27.7172,srid=4326)
