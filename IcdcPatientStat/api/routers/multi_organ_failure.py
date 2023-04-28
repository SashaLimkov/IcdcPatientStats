from typing import List
from ninja import Router
from api.schemas.multi_organ_failure import MOFOut


mof_router = Router()

# @mof_router.get("/{patient_id}", response=MOFOut|List[MOFOut])
# def get_mof_by_patient_id(request, patient_id: str):
#     pass

