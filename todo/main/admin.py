from django.contrib import admin


from .models import *
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','is_completed', 'created_at']
    list_filter = ['title', 'created_at']
    list_display_links = ['id']
    list_editable = ['title']

admin.site.register(Task, TaskAdmin)
