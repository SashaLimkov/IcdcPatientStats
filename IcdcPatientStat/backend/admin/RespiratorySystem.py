from django.contrib import admin
from backend.models import RespiratorySystem


class RespiratorySystemAdmin(admin.ModelAdmin):
    list_display = [
        "patient",
        "system_type",
        "ventilation_type",
        "do",
        "chd",
        "FiO2",
        "peep",
        "saturation",
    ]


admin.site.register(RespiratorySystem, RespiratorySystemAdmin)
