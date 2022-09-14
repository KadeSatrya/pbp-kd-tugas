from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)

data_item_katalog = CatalogItem.objects.all()
context = {
    "list_item": data_item_katalog,
    "nama": "Kade Satrya Noto Sadharma",
    "npm": "2106752376"
    }