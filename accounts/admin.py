from django.contrib import admin
from django.contrib.admin import ModelAdmin


from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
  ordering = ['user']
  list_display = ['user', 'id']
  list_display_links = ['id', 'user']
  list_per_page = 20



