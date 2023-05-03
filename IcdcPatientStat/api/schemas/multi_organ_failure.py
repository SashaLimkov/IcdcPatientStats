from ninja import Schema
from backend.models import MultiOrganFailure
from ninja.orm import create_schema

MOFOut = create_schema(MultiOrganFailure)
MOFOut.__name__ = "MOFOut"

MOFin = create_schema(
    MultiOrganFailure,
    fields=[
        "patient",
        "sofa"
    ],
)
MOFin.__name__ = "MOFin"

class MOFPut(Schema):
    id: int
    patient_id: str = None
    sofa: int = None