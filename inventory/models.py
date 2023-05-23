from django.db import models

# Create your models here.
class ItemGroup(models.Model):
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name

class Item(models.Model):
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    item_sn = models.CharField(max_length=255)
