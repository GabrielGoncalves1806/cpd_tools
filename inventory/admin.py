from django.contrib import admin
from .models import Item, ItemGroup, Brand

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'item_brand', 'item_sn','item_group']

@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ['id','group_name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','brand_name']