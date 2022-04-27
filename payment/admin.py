from django.contrib import admin
from .models import Cart, Products

# Register your models here.
admin.site.register(Products)
admin.site.register(Cart)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id','name','quantity','currency','amount']