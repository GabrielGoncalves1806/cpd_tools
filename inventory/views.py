from django.shortcuts import render
from .models import Item, ItemBrand, ItemGroup, Resale, Employee, ItemCondition, ItemTransfer

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def new_item(request):
    return render(request, 'pages/new_item.html')

def list_itens(request):
    return render(request, 'pages/list_itens.html')

def dashboards(request):
    return render(request, 'pages/dashboards.html')

def config(request):
    return render(request, 'pages/config.html')