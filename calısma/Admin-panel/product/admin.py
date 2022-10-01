from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)



admin.site.site_title = "ERHAN PROJECT" #? html deki title gibi
admin.site.site_header = "Erhan Admin Portal"
admin.site.index_title = "Welcome to Erhan Admin Portal"