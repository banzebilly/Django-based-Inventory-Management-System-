from django.contrib import admin
from .models import Shoe

# Register your models here.

class ShoeAdmin(admin.ModelAdmin):
    list_display = ("country", "code", "product", "cost", "quantity", "created_at")

    list_display_link = ("product", "code")



admin.site.register( Shoe, ShoeAdmin)