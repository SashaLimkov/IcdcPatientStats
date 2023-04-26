from django.contrib import admin
from backend.models import CardiovascularSystem


class CarfiovascularSystemAdmin(admin.ModelAdmin):
    list_display = ["patient", "pulse", "chss", "created_at"]


admin.site.register(CardiovascularSystem, CarfiovascularSystemAdmin)
