from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Function untuk mywatchlist/
def show_watchlist_home(request):
    return render(request, "watchlist_home.html", context)

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

# Tugas bonus
# Mengubah mywatchlist_data menjadi dictionary
# lalu mencari jumlah yang sudah ditonton dan belum ditonton
# Jumlah yang sudah ditonton dicari dengan menjumlahlan semua nilai field "watched"
# Jumlah yang belum ditonton dicari dengan mengurangi panjang dictionary dengan jumlah yang telah ditonton
# Lalu kedua nilai tersebut dimasukkan ke context
mywatchlist_data_dict = mywatchlist_data.values()
mywatchlist_length = len(mywatchlist_data_dict)
mywatchlist_watched = 0
for watchlist in mywatchlist_data_dict:
    mywatchlist_watched += watchlist["watched"]
mywatchlist_not_watched = mywatchlist_length - mywatchlist_watched

context={
    "watchlist_data" : mywatchlist_data,
    "sudah_ditonton": mywatchlist_watched,
    "belum_ditonton": mywatchlist_not_watched
}