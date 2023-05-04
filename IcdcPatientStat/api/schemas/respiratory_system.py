from ninja import Schema
from backend.models import RespiratorySystem
from ninja.orm import create_schema

RSOut = create_schema(RespiratorySystem)
RSOut.__name__ = "RSOut"


class RSin(Schema):
    patient: str
    system_type: str
    ventilation_type: str = None
    do: int = None
    chd: int
    FiO2: int = None
    peep: int = None
    saturation: int


class RSPut(RSin):
    id: int
    patient: str = None
    system_type: str = None
    chd: int = None
    saturation: int = None
