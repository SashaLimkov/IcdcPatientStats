from django.contrib import admin
from backend.models import ImmuneSystem


class ImmuneSystemAdmin(admin.ModelAdmin):
    list_display = [
    "patient", 
    "temperature", 
    "description",
    "created_at"
    ]



admin.site.register(ImmuneSystem, ImmuneSystemAdmin)