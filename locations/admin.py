from django.contrib import admin
from .models import  FoodLocation

# Register your models here.
@admin.register(FoodLocation)
class FoodLocationAdmin(admin.ModelAdmin):
    pass