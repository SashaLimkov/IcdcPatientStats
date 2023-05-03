from typing import Dict, List
from ninja import Router
from django.shortcuts import get_object_or_404
from api.schemas.multi_organ_failure import MOFOut
from api.schemas.urinary_system import USOut
from api.schemas.imunne_system import ISOut
from api.schemas.central_nervous_system import CNSOut
from api.schemas.cardiovascular_system import CSOut
from api.schemas.respiratory_system import RSOut
from api.schemas.patient import PatientOut, PatientIn, PatientPutOrDelete, PatientHistory
from backend.models import Patient   
from backend.services import patient as patient_data


patient_router = Router()


@patient_router.get("/{patient_id}", response=PatientOut)
def get_patient_by_patient_id(request, patient_id: str):
    return get_patient_obj_by_patient_id(patient_id=patient_id)

@patient_router.get("/{patient_id}/full/", response=PatientHistory)
def get_patient_history_by_patient_id(request, patient_id: str):
    patient = get_patient_obj_by_patient_id(patient_id=patient_id)
    mof =  get_patient_mof(request=request, patient_id=patient_id)
    us =  get_patient_us(request=request, patient_id=patient_id)
    isys =  get_patient_is(request=request, patient_id=patient_id)
    cns =  get_patient_cns(request=request, patient_id=patient_id)
    cs =  get_patient_cs(request=request, patient_id=patient_id)
    rs =  get_patient_rs(request=request, patient_id=patient_id)
    return {
        "patient": patient,
        "imunne_system":list(isys),
        "urinary_system":list(us),
        "mof":list(mof),
        "central_nervous_system":list(cns),
        "cardiovascular_system":list(cs),
        "respiratory_system":list(rs) 
    }


@patient_router.get("/all_patients/", response=List[PatientOut])
def get_all_patients(request):
    qs = patient_data.get_all_patients()
    return qs


@patient_router.post("/", response=PatientOut)
def add_patient(request, payload: PatientIn):
    patient = patient_data.create_patient(**payload.dict())
    return patient


@patient_router.put("/", response=PatientOut)
def update_patient_by_patient_id(request, payload: PatientPutOrDelete):
    if patient := get_patient_obj(payload=payload):
        patient = patient_data.update_obj(patient, payload.dict())
    return patient


@patient_router.delete("/")
def delete_patient_by_patient_id(request, payload: PatientPutOrDelete):
    if patient := get_patient_obj(payload=payload):
        patient.delete()
        return {"success": True}
    return patient


@patient_router.get("/mof_list/{patient_id}", response=MOFOut | List[MOFOut])
def get_patient_mof(request, patient_id: str):
    patient = get_patient_obj_by_patient_id(patient_id=patient_id)
    return patient.mof_collection.all().order_by("-created_at")


@patient_router.get("/us_list/{patient_id}", response=USOut | List[USOut])
def get_patient_us(request, patient_id: str):
    patient = get_patient_obj_by_patient_id(patient_id=patient_id)
    return patient.urin_collection.all().order_by("-created_at")


@patient_router.get("/is_list/{patient_id}", response=ISOut | List[ISOut])
def get_patient_is(request, patient_id: str):
    patient = get_patient_obj_by_patient_id(patient_id=patient_id)
    return patient.is_collection.all().order_by("-created_at")


@patient_router.get("/cns_list/{patient_id}", response=CNSOut | List[CNSOut])
def get_patient_cns(request, patient_id: str):
    patient = get_patient_obj_by_patient_id(patient_id=patient_id)
    return patient.cns_collection.all().order_by("-created_at")


@patient_router.get("/cs_list/{patient_id}", response=CSOut | List[CSOut])
def get_patient_cs(request, patient_id: str):
    patient = get_patient_obj_by_patient_id(patient_id=patient_id)
    return patient.cs_collection.all().order_by("-created_at")


@patient_router.get("/rs_list/{patient_id}", response=RSOut | List[RSOut])
def get_patient_rs(request, patient_id: str):
    patient = get_patient_obj_by_patient_id(patient_id=patient_id)
    return patient.rs_collection.all().order_by("-created_at")


def get_patient_obj(payload: PatientPutOrDelete):
    payload_dict = payload.dict()
    patient_id = payload_dict.get("patient_id", "")
    return get_patient_obj_by_patient_id(patient_id=patient_id)



def get_patient_obj_by_patient_id(patient_id: str):
    return get_object_or_404(Patient, patient_id=patient_id)
