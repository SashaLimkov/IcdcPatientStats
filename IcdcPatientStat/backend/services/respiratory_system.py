from backend.services.patient import get_patient_by_id
from backend.models import RespiratorySystem


def create_rs(payload_dict: dict) -> RespiratorySystem:
    patient = get_patient_by_id(patient_id=payload_dict.pop("patient"))
    return RespiratorySystem.objects.create(
        **payload_dict, patient=patient
    )

def get_all_rs_notes():
    return RespiratorySystem.objects.all()