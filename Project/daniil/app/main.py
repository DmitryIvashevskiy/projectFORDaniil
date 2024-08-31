from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from .routers import tickets
from .database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()
    await periodic_check_and_send_expired_tickets()
    await periodic_change_status_of_tickets()

app.include_router(tickets.router)

@app.on_event("startup")
@repeat_every(seconds=15)
async def periodic_check_and_send_expired_tickets():
    from .background_tasks import check_and_send_expired_tickets
    await check_and_send_expired_tickets()

@app.on_event("startup")
@repeat_every(seconds=50)
async def periodic_change_status_of_tickets():
    from .background_tasks import change_status_of_tickets
    await change_status_of_tickets()
