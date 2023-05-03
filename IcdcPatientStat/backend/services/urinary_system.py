from backend.services.patient import get_patient_by_id
from backend.models import UrinarySystem


def create_us(payload_dict: dict) -> UrinarySystem:
    print(payload_dict)
    patient = get_patient_by_id(patient_id=payload_dict["patient"])
    return UrinarySystem.objects.create(
        diurez=payload_dict["diurez"], infuzyy=payload_dict["infuzyy"], patient=patient
    )


def get_all_us_notes():
    return UrinarySystem.objects.all()
