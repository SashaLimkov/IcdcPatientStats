from django.contrib import admin
from backend.models import UrinarySystem


class UrinarySystemAdmin(admin.ModelAdmin):
    list_display =[
    "patient", 
    "diurez", 
    "infuzyy",
    ]



admin.site.register(UrinarySystem, UrinarySystemAdmin)