from backend.services.patient import get_patient_by_id
from backend.models import MultiOrganFailure


def create_mof(payload_dict: dict) -> MultiOrganFailure:
    print(payload_dict)
    patient = get_patient_by_id(patient_id=payload_dict["patient"])
    return MultiOrganFailure.objects.create(
        sofa=payload_dict["sofa"], patient=patient
    )


def get_all_mof_notes():
    return MultiOrganFailure.objects.all()
