from backend.models import Patient


def get_all_patients():
    return Patient.objects.all()


def get_patient_by_id(patient_id: str):
    return Patient.objects.filter(patient_id=patient_id).first()


def create_patient(*args, **kwargs) -> Patient:
    return Patient.objects.create(**kwargs)


def update_patient(patient: Patient, data: dict) -> Patient:
    for attr, value in data.items():
        if value:
            setattr(patient, attr, value)
        patient.save()
    return patient
