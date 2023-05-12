from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from backend.services.patient import update_obj
from api.schemas.cardiovascular_system import CSOut, CSin, CSPut
from backend.services import cardiovascular_system as cs
from backend.models import CardiovascularSystem

cvs_router = Router()


@cvs_router.get("/get_all/", response=List[CSOut])
def get_all_cs_notes(request):
    return cs.get_all_cs_notes()


@cvs_router.get("/{pk}", response=CSOut)
def get_cs_note(request, pk: int):
    return get_cs_nte_obj(pk=pk)


@cvs_router.post("/", response=CSOut)
def add_cs_note(request, payload: CSin):
    """
    Добавление сердечно сосудистой записи
    """
    payload_dict = payload.dict()
    return cs.create_cs(payload_dict)


@cvs_router.put("/", response=CSOut)
def update_cns_patient_id(request, payload: CSPut):
    result = None
    if cns_note := get_cs_nte_obj(pk=payload.dict().get("id", -1)):
        result = update_obj(cns_note, payload.dict())
    return result


@cvs_router.delete("/{pk}")
def delete_cs_note(request, pk: int):
    get_cs_nte_obj(pk=pk).delete()
    return None


def get_cs_nte_obj(pk: int):
    return get_object_or_404(CardiovascularSystem, pk=pk)
