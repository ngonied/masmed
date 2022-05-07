from django.contrib import admin
from users.models import CustomUser
from .models import ProfessionalProfile


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProfessionalProfile)

