from django.contrib import admin
from .models import Item, ItemGroup, ItemBrand, ItemCondition, Resale, ItemTransfer, Employee


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'item_serial', 'item_brand', 'item_group', 'item_condition']

@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ['id','description']

@admin.register(ItemBrand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','description']

@admin.register(ItemCondition)
class ItemConditionAdmin(admin.ModelAdmin):
    list_display = ['id','description']

@admin.register(Resale)
class ResaleAdmin(admin.ModelAdmin):
    list_display = ['id','description']
    
@admin.register(ItemTransfer)
class ItemTransferAdmin(admin.ModelAdmin):
    list_display = ['id','item','resale','transfer_type','observations','responsible','transfer_date']
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','description']    