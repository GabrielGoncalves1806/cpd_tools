from django import forms
from inventory.models import ItemGroup, Brand, Item

class ItemGroupForm(forms.ModelForm):
    class Meta:
        model = ItemGroup
        fields = ['group_name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_sn', 'item_brand', 'item_group', 'item_state']