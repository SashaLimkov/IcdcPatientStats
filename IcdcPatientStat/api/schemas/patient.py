from ninja import Schema
from backend.models import Patient
from ninja.orm import create_schema

PatientOut = create_schema(Patient)
PatientIn = create_schema(
    Patient,
    fields=[
        "fio",
        "patient_id",
        "ilness_history_num",
        "ema",
        "empz",
    ],
)


class PatientPutOrDelete(Schema):
    fio: str = None
    patient_id: str
    ilness_history_num: str = None
    ema: str = None
    empz: str = None


PatientOut.__name__ = "PatientOut"
PatientIn.__name__ = "PatientIn"
