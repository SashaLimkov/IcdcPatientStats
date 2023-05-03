from ninja import Schema
from backend.models import CardiovascularSystem
from ninja.orm import create_schema

CSOut = create_schema(
    CardiovascularSystem, custom_fields=[("pretty_ad", str, "Красивый вывод")]
)
CSOut.__name__ = "CSOut"
