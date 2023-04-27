from backend.models import Patient


def get_all_patients():
    return Patient.objects.all()


def create_patient(*args, **kwargs):
    return Patient.objects.create(**kwargs)


def update_patient(patient: Patient, data: dict):
    for attr, value in data.items():
        if value:
            setattr(patient, attr, value)
        patient.save()
    return {"Success": True}
