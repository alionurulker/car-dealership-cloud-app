from django.contrib import admin
# from .models import related models
from .models import CarModel, CarMake
#from .models import Course, Lesson

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# # CarModelAdmin class
# class CarModelAdmin(admin.ModelAdmin):
#     fields = ['dealer_id', 'name', 'type', 'year']

# # CarMakeAdmin class with CarModelInline

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

# # Register models here
# admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
