from django.contrib import admin
from .models import Clothing, Offer


class ClothingAdmin(admin.ModelAdmin):
    list_display = ( 'name','price','stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Offer, OfferAdmin)