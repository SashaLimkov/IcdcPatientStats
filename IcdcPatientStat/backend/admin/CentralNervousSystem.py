from django.contrib import admin
from backend.models import CentralNervousSystem



class CentralNervousSystemAdmin(admin.ModelAdmin):
    list_display = ["patient", "points", "description", "created_at"]



admin.site.register(CentralNervousSystem, CentralNervousSystemAdmin)
