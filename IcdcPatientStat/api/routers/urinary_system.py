from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from backend.services.patient import update_obj
from backend.models import UrinarySystem
from api.schemas.urinary_system import USOut, USin, USPut
from backend.services import urinary_system as us

us_router = Router()


@us_router.get("/get_all/", response=List[USOut])
def get_all_urinary_system_notes(request):
    return us.get_all_us_notes()


@us_router.get("/{pk}", response=USOut)
def get_urinary_system_note(request, pk: int):
    return get_us_nte_obj(pk=pk)


@us_router.delete("/{pk}")
def delete_urinary_system_note(request, pk: int):
    return get_us_nte_obj(pk=pk).delete()


@us_router.post("/", response=USOut)
def add_urinary_system_note(request, payload: USin):
    payload_dict = payload.dict()
    return us.create_us(payload_dict)

@us_router.put("/", response=USOut)
def update_patient_by_patient_id(request, payload: USPut):
    result=None
    if cns_note := get_us_nte_obj(pk=payload.dict().get("id", -1)):
        result = update_obj(cns_note, payload.dict())
    return result

def get_us_nte_obj(pk: int):
    return get_object_or_404(UrinarySystem, pk=pk)
