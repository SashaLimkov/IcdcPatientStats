import random
from ninja import NinjaAPI, Schema

from api.routers import (
    cvs_router,
    cns_router,
    is_router,
    mof_router,
    patient_router,
    rs_router,
    us_router,
)

api = NinjaAPI()

api.add_router("/patient/", patient_router)
api.add_router("/cvs/", cvs_router)
api.add_router("/cns/", cns_router)
api.add_router("/is/", is_router)
api.add_router("/mof/", mof_router)
api.add_router("/rs/", rs_router)
api.add_router("/us/", us_router)


# add error handler, need to add it to routers
class ServiceUnavailableError(Exception):
    pass


@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, exc):
    return api.create_response(
        request,
        {"message": "Please retry later"},
        status=503,
    )
