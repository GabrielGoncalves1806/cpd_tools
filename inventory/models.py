from django.db import models
from django.utils import timezone

# Create your models here.
class ItemGroup(models.Model):
    description = models.CharField(max_length=32)
    
    def __str__(self):
        return self.description

class ItemBrand(models.Model):
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description
    
class ItemCondition(models.Model):
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description
    
class Resale(models.Model):
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description

class Employee(models.Model):
    description = models.CharField(max_length=128)
    
    def __str__(self):
        return self.description

class Item(models.Model):
    item_name = models.CharField(max_length=64)
    item_serial = models.CharField(max_length=64)
    item_brand = models.ForeignKey(ItemBrand, on_delete=models.CASCADE)
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    item_condition = models.ForeignKey(ItemCondition,on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

class ItemTransfer(models.Model):
    TRANSFER_TYPES = (
        ('entry','Entry'),
        ('transfer', 'Transfer'),
        ('departure','Departure'),
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    #TODO
    #amount = models.PositiveSmallIntegerField()
    resale = models.ForeignKey(Resale, on_delete=models.CASCADE)
    transfer_type = models.CharField(max_length=32, choices=TRANSFER_TYPES)
    observations = models.TextField(null=True, blank=True)
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE)
    transfer_date = models.DateTimeField(default=timezone.now)
    
    
    
    
    
    
    
