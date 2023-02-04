from django.contrib import admin
from .models import Teacher
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'second_name', 'birth_day', 'email', 'phone',)
    list_display_links = ('pk',)
    search_fields = ('first_name', 'second_name', 'birth_day', 'email', 'phone',)
    list_editable = ('first_name', 'second_name', 'birth_day', 'email', 'phone',)
    readonly_fields = ('login',)



admin.site.register(Teacher, TeacherAdmin)