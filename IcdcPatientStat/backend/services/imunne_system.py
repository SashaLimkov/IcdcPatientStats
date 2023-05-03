from backend.services.patient import get_patient_by_id
from backend.models import ImmuneSystem


def create_is(payload_dict: dict) -> ImmuneSystem:
    print(payload_dict)
    patient = get_patient_by_id(patient_id=payload_dict["patient"])
    return ImmuneSystem.objects.create(
        temperature=payload_dict["temperature"], patient=patient
    )


def get_all_is_notes():
    return ImmuneSystem.objects.all()
