from django import forms
from inventory.models import ItemGroup, Brand

class ItemGroupForm(forms.ModelForm):
    class Meta:
        model = ItemGroup
        fields = ['group_name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']