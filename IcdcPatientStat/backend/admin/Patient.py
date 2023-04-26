from django.contrib import admin
from backend.models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = [
        "fio",
        "patient_id",
        "ilness_history_num",
        "ema",
        "empz",
    ]


admin.site.register(Patient, PatientAdmin)
