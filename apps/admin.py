# from django.contrib import admin
#
# # Register your models here.
# from django.contrib.admin import ModelAdmin
#
# from apps.models import Category, Task
#
#
# @admin.register(Category)
# class CategoryAdmin(ModelAdmin):
#     list_display = ('name',)
#     exclude = ('slug',)
#
#
# @admin.register(Task)
# class TaskAdmin(ModelAdmin):
#     list_display = ('name', 'description', 'is_important', 'term')
#     exclude = ('created_at', 'status', 'slug')
from django.contrib import admin
from apps import models

admin.site.register(models.Task)
