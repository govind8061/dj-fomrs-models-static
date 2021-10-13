from django.contrib import admin
from .models.product import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','image']