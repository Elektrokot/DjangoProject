from django.contrib import admin

# Register your models here.
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'year')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')


