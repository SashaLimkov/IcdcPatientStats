from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from backend.services.patient import update_obj
from api.schemas.respiratory_system import RSOut, RSin, RSPut
from backend.services import respiratory_system as rs


rs_router = Router()


@rs_router.get("/get_all/", response=List[RSOut])
def get_all_rs_notes(request):
    return rs.get_all_rs_notes()


@rs_router.get("/{pk}", response=RSOut)
def get_cs_note(request, pk: int):
    return get_rs_nte_obj(pk=pk)


@rs_router.post("/", response=RSOut)
def add_cs_note(request, payload: RSin):
    payload_dict = payload.dict()
    return rs.create_rs(payload_dict)


@rs_router.put("/", response=RSOut)
def update_cns_patient_id(request, payload: RSPut):
    result = None
    if cns_note := get_rs_nte_obj(pk=payload.dict().get("id", -1)):
        result = update_obj(cns_note, payload.dict())
    return result


@rs_router.delete("/{pk}")
def delete_cs_note(request, pk: int):
    get_rs_nte_obj(pk=pk).delete()
    return None


def get_rs_nte_obj(pk: int):
    return get_object_or_404(rs.RespiratorySystem, pk=pk)
