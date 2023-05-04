from ninja import Schema
from backend.models import CardiovascularSystem
from ninja.orm import create_schema

CSOut = create_schema(
    CardiovascularSystem, custom_fields=[("pretty_ad", str, "Красивый вывод")]
)
CSOut.__name__ = "CSOut"

CSin = create_schema(
    CardiovascularSystem, fields=["patient", "pulse", "chss", "ad_up", "ad_down"]
)
CSin.__name__ = "CSin"


class CSPut(Schema):
    id: int
    patient_id: str = None
    pulse: int = None
    chss: int = None
    ad_up: int = None
    ad_down: int = None
