from ninja import Schema
from backend.models import RespiratorySystem
from ninja.orm import create_schema

RSOut = create_schema(RespiratorySystem)
RSOut.__name__ = "RSOut"
