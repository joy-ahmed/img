from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'done', 'img')
    list_editable = ['title', 'done',]