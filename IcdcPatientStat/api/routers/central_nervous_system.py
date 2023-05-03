from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from backend.services.patient import update_obj
from api.schemas.central_nervous_system import CNSPut
from backend.models import CentralNervousSystem
from backend.services import central_nervous_system as cns
from api.schemas.central_nervous_system import CNSOut, CNSin



cns_router = Router()


@cns_router.get("/get_all/", response=List[CNSOut])
def get_all_cns_notes(request):
    return cns.get_all_cns_notes()


@cns_router.get("/{pk}", response=CNSOut)
def get_cns_note(request, pk: int):
    return get_cns_nte_obj(pk=pk)


@cns_router.put("/", response=CNSOut)
def update_cns_patient_id(request, payload: CNSPut):
    result=None
    if cns_note := get_cns_nte_obj(pk=payload.dict().get("id", -1)):
        result = update_obj(cns_note, payload.dict())
    return result


@cns_router.delete("/{pk}")
def delete_cns_note(request, pk: int):
    get_cns_nte_obj(pk=pk).delete()
    return None


@cns_router.post("/", response=CNSOut)
def add_cns_note(request, payload: CNSin):
    payload_dict = payload.dict()
    return cns.create_cns(payload_dict)


def get_cns_nte_obj(pk: int):
    return get_object_or_404(CentralNervousSystem, pk=pk)
