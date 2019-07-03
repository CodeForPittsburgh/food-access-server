from django.contrib import admin
from https://github.com/CodeForPittsburgh/food-access-server.git.models import  FoodLocation

# Register your models here.
@admin.register(FoodLocation)
class FoodLocationAdmin(admin.ModelAdmin):
    pass