from django.contrib import admin
from django.urls import path
from inventory.views import main_page, new_item, list_itens, dashboards, config

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main-page'),
    path('new-item/', new_item, name='new-item'),
    path('list-itens/', list_itens, name='list-itens'),
    path('dashboards/', dashboards, name='dashboards'),
    path('config/', config, name='config'),
]
