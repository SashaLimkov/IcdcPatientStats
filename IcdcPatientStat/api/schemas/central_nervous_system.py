from ninja import Schema
from backend.models import CentralNervousSystem
from ninja.orm import create_schema

CNSOut = create_schema(CentralNervousSystem)
CNSOut.__name__ = "CNSOut"

CNSin = create_schema(
    CentralNervousSystem,
    fields=[
        "patient",
        "points"
    ],
)
CNSin.__name__ = "CNSin"

