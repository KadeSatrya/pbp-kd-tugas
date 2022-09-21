from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Function untuk mywatchlist/
def show_watchlist_home(request):
    return render(request, "watchlist_home.html")

# Function untuk mywatchlist/html
def show_watchlist_html(request):
    return render(request, "mywatchlist.html", context)

# Function untuk mywatchlist/xml
def show_watchlist_xml(request):
    return HttpResponse(serializers.serialize("xml", mywatchlist_data), content_type="application/xml")

# Function untuk mywatchlist/json
def show_watchlist_json(request):
    return HttpResponse(serializers.serialize("json", mywatchlist_data), content_type="application/json")
#Note: request pada fungsi xml dan json tetap harus dimasukkan pada parameter meskipun tak diakses
mywatchlist_data = MyWatchList.objects.all()
context={
    "watchlist_data" : mywatchlist_data
}