from backend.services.patient import get_patient_by_id
from backend.models import CardiovascularSystem


def create_cs(payload_dict: dict) -> CardiovascularSystem:
    patient = get_patient_by_id(patient_id=payload_dict.pop("patient"))
    return CardiovascularSystem.objects.create(
        **payload_dict, patient=patient
    )

def get_all_cs_notes():
    return CardiovascularSystem.objects.all()