from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from api.schemas import PatientOut, PatientIn, PatientPutOrDelete
from backend.models import Patient
from backend.services import patient as patient_data


patient_router = Router()


@patient_router.get("/{patient_id}", response=PatientOut)
def get_patient_by_patient_id(request, patient_id: str):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return patient


@patient_router.get("/all_patients/", response=List[PatientOut])
def get_all_patients(request):
    qs = patient_data.get_all_patients()
    return qs


@patient_router.post("/", response=PatientOut)
def add_patient(request, payload: PatientIn):
    patient = patient_data.create_patient(**payload.dict())
    return patient


@patient_router.put("/")
def update_patient_by_patient_id(request, payload: PatientPutOrDelete):
    if patient := get_patient_obj(payload=payload):
        patient = patient_data.update_patient(patient, payload.dict())
    return patient


@patient_router.delete("/")
def delete_patient_by_patient_id(request, payload: PatientPutOrDelete):
    if patient := get_patient_obj(payload=payload):
        patient.delete()
        return {"success": True}
    return patient


def get_patient_obj(payload: PatientPutOrDelete):
    payload_dict = payload.dict()
    patient_id = payload_dict.get("patient_id")
    return get_object_or_404(Patient, patient_id=patient_id)
