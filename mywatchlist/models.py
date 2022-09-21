from django.db import models

class MyWatchList(models.Model):
    
    watched = models.IntegerField(default=0)#0 untuk ya, 1 untuk tidak
    title = models.CharField(max_length=255, default="")#max_length wajib untuk CharField, maksimal 255
    rating = models.IntegerField(default=0)
    release_date = models.CharField(max_length=10, default="")#DD/MM/YYYY
    review = models.TextField(default="") #TextField bisa lebih dari 255 karakter

    # Semua bersifat non-nullable sehingga harus ada default, kalau tidak akan error ketika migrations
    # Sehingga tidak bisa loaddata karena operationalerror: no such column
    """
    () di akhir itu penting, kalo tidak saay migration akan didelete secara otomatis 
    Learnt it the hard way
    """