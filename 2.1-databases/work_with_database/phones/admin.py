from django.contrib import admin
from phones.models import Phone

# Register your models here.

@admin.register(Phone)

class phone_admin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'slug'
