from backend.services.patient import get_patient_by_id
from backend.models import CentralNervousSystem


def create_cns(payload_dict: dict) -> CentralNervousSystem:
    print(payload_dict)
    patient = get_patient_by_id(patient_id=payload_dict["patient"])
    return CentralNervousSystem.objects.create(
        points=payload_dict["points"], patient=patient
    )


def get_all_cns_notes():
    return CentralNervousSystem.objects.all()
