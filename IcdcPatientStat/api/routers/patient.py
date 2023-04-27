from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from api.schemas import PatientOut, PatientIn, PatientPutOrDelete
from backend.models import Patient


patient_router = Router()


@patient_router.get("/{patient_id}", response=PatientOut)
def get_patient_by_patient_id(request, patient_id:str):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return patient



@patient_router.get("/all_patients/", response=List[PatientOut])
def get_all_patients(request):
    qs = Patient.objects.all()
    return qs



@patient_router.post("/", response=PatientOut)
def add_patient(request, payload:PatientIn):
    patient = Patient.objects.create(**payload.dict())
    return patient

@patient_router.put("/")
def update_patient_by_patient_id(request, payload: PatientPutOrDelete):
    payload_dict = payload.dict()
    patient_id = payload_dict.get("patient_id")
    patient = get_object_or_404(Patient, patient_id=patient_id)
    if patient:
        for attr, value in payload_dict.items():
            if value:
                setattr(patient, attr, value)
        patient.save()
        patient = {"Success":True}
    return patient

@patient_router.delete("/")
def delete_patient_by_patient_id(request, payload: PatientPutOrDelete):
    payload_dict = payload.dict()
    patient_id = payload_dict.get("patient_id")
    patient = get_object_or_404(Patient, patient_id=patient_id)
    if patient:
        patient.delete()
        return {"success": True}
    return patient