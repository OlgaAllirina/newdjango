from django.contrib import admin
from .models import Phone


# admin/admin1
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'lte_exists', 'slug']
    list_filter = ['name', 'price']
# Register your models here.
