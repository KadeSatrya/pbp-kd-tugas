from django.urls import path
from mywatchlist.views import show_watchlist_home, show_watchlist_html, show_watchlist_json, show_watchlist_xml

app_name = 'watchlist'

urlpatterns = [
    path('', show_watchlist_home, name='show_watchlist_home'), # mywatchlist/
    path('html/', show_watchlist_html, name='show_watchlist_html'), # mywatchlist/html/
    path('xml/', show_watchlist_xml, name='show_watchlist_xml'), # mywatchlist/xml/
    path('json/', show_watchlist_json, name='show_watchlist_json'), # mywatchlist/json/
]