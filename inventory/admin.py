from django.contrib import admin
from .models import Shoe
# from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.




class ShoeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    list_display = ["country", "code", "product", "cost", "quantity", "created_at"]

    search_field = ['code', 'product']
  
    list_display_link = ("product", "code")



admin.site.register( Shoe, ShoeAdmin)