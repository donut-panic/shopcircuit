from django.contrib import admin
from django.contrib.admin import ModelAdmin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
  ordering = ['id']
  list_display = ['id','user', 'image', 'gender',]
  list_display_links = ['id', 'user']
  list_per_page = 20
