from django.contrib import admin
from backend.models import MultiOrganFailure


class MultiOrganFailureAdmin(admin.ModelAdmin):
    list_display = [
    "patient", 
    "sofa",
    "created_at"
    ]


admin.site.register(MultiOrganFailure, MultiOrganFailureAdmin)