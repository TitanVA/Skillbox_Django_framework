from django.contrib import admin
from app_profile.models import User


@admin.register(User)
class AppProfileAdmin(admin.ModelAdmin):
    pass