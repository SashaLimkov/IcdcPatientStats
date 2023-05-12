from typing import List
from ninja import Schema
from api.schemas.multi_organ_failure import MOFOut, MOFin
from api.schemas.urinary_system import USOut, USin
from api.schemas.imunne_system import ISOut, ISin
from api.schemas.central_nervous_system import CNSOut, CNSin
from api.schemas.cardiovascular_system import CSOut, CSin
from api.schemas.respiratory_system import RSOut, RSin
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


class PatientHistory(Schema):
    patient: PatientOut
    imunne_system: List[ISOut] = None
    urinary_system: List[USOut] = None
    mof: List[MOFOut] = None
    central_nervous_system: List[CNSOut] = None
    cardiovascular_system: List[CSOut] = None
    respiratory_system: List[RSOut] = None


class AddAll(Schema):
    patient: PatientIn
    imunne_system: ISin = None
    urinary_system: USin = None
    mof: MOFin = None
    central_nervous_system: CNSin = None
    cardiovascular_system: CSin = None
    respiratory_system: RSin = None