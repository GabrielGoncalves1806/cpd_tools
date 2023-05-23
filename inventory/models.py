from django.db import models

# Create your models here.
class ItemGroup(models.Model):
    group_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.group_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

    def __str__(self):
        return self.brand_name
    
class State(models.Model):
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return self.state_name
    
class Resale(models.Model):
    resale_name = models.CharField(max_length=30)

    def __str__(self):
        return self.resale_name

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_sn = models.CharField(max_length=50)
    item_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    item_state = models.ForeignKey(State,on_delete=models.CASCADE)
    resale = models.ForeignKey(Resale, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item_name

    
    
    
