from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)



admin.site.site_title = "ERHAN PROJECT" #? html deki title gibi
admin.site.site_header = "Erhan Admin Portal"
admin.site.index_title = "Welcome to Erhan Admin Portal"

#? admin i istediğimiz gibi düzenliyoruz
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "update_date")
    list_editable = ("is_in_stock",)
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name",)  
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}   #? when adding product in admin site example: erhan-tezer
    list_per_page = 25
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock") #? fieldset kullandığımız zaman bunu kullanamayız