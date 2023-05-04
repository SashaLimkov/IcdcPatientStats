from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from backend.services.patient import update_obj
from backend.models import MultiOrganFailure
from api.schemas.multi_organ_failure import MOFOut, MOFin, MOFPut
from backend.services import multi_organ_failure as mof

mof_router = Router()


@mof_router.get("/get_all/", response=List[MOFOut])
def get_all_mof_notes(request):
    return mof.get_all_mof_notes()


@mof_router.get("/{pk}", response=MOFOut)
def get_mof_note(request, pk: int):
    return get_mof_nte_obj(pk=pk)


@mof_router.delete("/{pk}")
def delete_mof_note(request, pk: int):
    get_mof_nte_obj(pk=pk).delete()
    return None


@mof_router.post("/", response=MOFOut)
def add_mof_note(request, payload: MOFin):
    payload_dict = payload.dict()
    return mof.create_mof(payload_dict)


@mof_router.put("/", response=MOFOut)
def update_mof_patient_id(request, payload: MOFPut):
    result = None
    if cns_note := get_mof_nte_obj(pk=payload.dict().get("id", -1)):
        result = update_obj(cns_note, payload.dict())
    return result


def get_mof_nte_obj(pk: int):
    return get_object_or_404(MultiOrganFailure, pk=pk)
