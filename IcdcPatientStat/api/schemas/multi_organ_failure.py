from ninja import Schema
from backend.models import MultiOrganFailure
from ninja.orm import create_schema

MOFOut = create_schema(MultiOrganFailure)
MOFOut.__name__ = "MOFOut"
