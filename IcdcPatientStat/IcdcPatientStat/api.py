from ninja import NinjaAPI, Schema

from api.routers import cvs_router, cns_router, is_router, mof_router, patient_router, rs_router, us_router

api = NinjaAPI()

api.add_router("/patient/", patient_router)
api.add_router("/cvs/", cvs_router)
api.add_router("/cns/", cns_router)
api.add_router("/is/", is_router)
api.add_router("/mof/", mof_router)
api.add_router("/rs/", rs_router)
api.add_router("/us/", us_router)
