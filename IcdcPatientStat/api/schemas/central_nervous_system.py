from ninja import Schema
from backend.models import CentralNervousSystem
from ninja.orm import create_schema

CNSOut = create_schema(CentralNervousSystem)
CNSOut.__name__ = "CNSOut"
