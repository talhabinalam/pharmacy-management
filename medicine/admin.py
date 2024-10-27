from django.contrib import admin
from .models import *

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'generic_name', 'manufacturer', 'description', 'price', 'batch_number')

admin.site.register(Medicine, MedicineAdmin)
