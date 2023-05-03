from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from backend.services.patient import update_obj
from api.schemas.imunne_system import ISOut, ISin, ISPut
from backend.models import ImmuneSystem
from backend.services import imunne_system as ims

is_router = Router()

@is_router.get("/get_all/", response=List[ISOut])
def get_all_imunne_system_notes(request):
    return ims.get_all_is_notes()


@is_router.get("/{pk}", response=ISOut)
def get_imunne_system_note(request, pk: int):
    return get_imunne_nte_obj(pk=pk)


@is_router.delete("/{pk}")
def delete_imunne_system_note(request, pk: int):
    get_imunne_nte_obj(pk=pk).delete()
    return None


@is_router.post("/", response=ISOut)
def add_imunne_system_note(request, payload: ISin):
    payload_dict = payload.dict()
    return ims.create_is(payload_dict)

@is_router.put("/", response=ISOut)
def update_patient_by_patient_id(request, payload: ISPut):
    result=None
    if cns_note := get_imunne_nte_obj(pk=payload.dict().get("id", -1)):
        result = update_obj(cns_note, payload.dict())
    return result


def get_imunne_nte_obj(pk: int):
    return get_object_or_404(ImmuneSystem, pk=pk)

