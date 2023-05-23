from django.shortcuts import render
from .models import Item, Brand, ItemGroup
from cpd_inventory.forms import ItemGroupForm, BrandForm

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def new_item(request):
    brands = Brand.objects.all()
    groups = ItemGroup.objects.all()
    if request.POST:

        item_name = request.POST.get('item_name')
        item_brand = request.POST.get('item_brand')
        item_sn = request.POST.get('item_sn')
        item_group = request.POST.get('item_group')
        print(item_name)
        print(item_brand)
        print(item_sn)
        print(item_group)
        brand = Brand.objects.get(id=item_brand)
        group = ItemGroup.objects.get(id=item_group)
        Item.objects.create(
            item_group=group,
            item_name=item_name,
            item_brand=brand,
            item_sn=item_sn
            )
    return render(request, 'pages/new_item.html',{'brands':brands,'groups':groups})

def list_itens(request):
    itens = Item.objects.all()

    def filter_itens(itens):
        search = request.GET.get('search','').lower()
        if search in itens.item_name.lower():
            return True
        return False
        
    itens_filter = list(filter(filter_itens,itens))
    return render(request, 'pages/list_itens.html', {'itens':itens_filter})

def dashboards(request):
    return render(request, 'pages/dashboards.html')

def config(request):
    group_form = ItemGroupForm()
    brand_form = BrandForm()
    context = {
        'group_form':group_form,
        'brand_form':brand_form
    }
    if request.POST.get('group_name'):
        new_group = request.POST.get('group_name')
        ItemGroup.objects.create(group_name=new_group)
    elif request.POST.get('brand_name'):
        new_brand = request.POST.get('brand_name')
        Brand.objects.create(brand_name=new_brand)
    
    return render(request, 'pages/config.html',context=context)