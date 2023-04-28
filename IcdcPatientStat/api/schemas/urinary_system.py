from ninja import Schema
from backend.models import UrinarySystem
from ninja.orm import create_schema

USOut = create_schema(UrinarySystem)
USOut.__name__ = "USOut"

USin = create_schema(UrinarySystem,
                     fields=[
"patient",
"diurez",
"infuzyy",
                     ])
USin.__name__ = "USin"