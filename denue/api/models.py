# https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/geolibs/#gdalbuild
# https://docs.djangoproject.com/en/3.2/ref/contrib/gis/model-api/
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ComercialActivity(models.Model):
    name = models.CharField(max_length=100)


class Stratum(models.Model):
    name = models.CharField(max_length=100)


class ShopType(models.Model):
    name = models.CharField(max_length=100)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    activity = models.ForeignKey(
        ComercialActivity,
        on_delete=models.CASCADE,
        related_name='shops'
        )
    stratum = models.ForeignKey(
        Stratum,
        on_delete=models.CASCADE,
        related_name='shops')
    address = models.CharField(max_length=250)
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    shop_type = models.ForeignKey(
        ShopType,
        on_delete=models.CASCADE,
        related_name='shops'
        )
    position = models.PointField()
