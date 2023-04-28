from ninja import Schema
from backend.models import ImmuneSystem
from ninja.orm import create_schema

ISOut = create_schema(ImmuneSystem)
ISOut.__name__ = "ISOut"
