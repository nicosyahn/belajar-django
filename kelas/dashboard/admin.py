from django.contrib import admin

# Register your models here.
from .models import Barang, Transaksi, Detailtrans, Jenis, Membership, Level

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrg', 'nama', 'stok', 'harga', 'link_gbr', 'jenis_id']
    search_fields=['kodebrg', 'nama']
    list_filter=('jenis_id',)
    list_per_page= 3

class kolomLevel(admin.ModelAdmin):
    list_display=['level', 'bonus']
    search_fields=['level']
    list_per_page= 3


class kolomMembership(admin.ModelAdmin):
    list_display=['kodemem', 'nama', 'status', 'level_id']
    search_fields=['kodemem', 'nama']
    list_filter=('level_id',)
    list_per_page= 3


admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)
admin.site.register(Membership, kolomMembership)
admin.site.register(Level, kolomLevel)
admin.site.register(Transaksi)
admin.site.register(Detailtrans)