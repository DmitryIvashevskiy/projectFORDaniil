from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from ..schemas import Ticket, TicketCreate, TicketResponse
from ..crud import create_ticket, get_tickets
from ..database import get_db

router = APIRouter()

@router.post("/api/ticket", response_model=Ticket)
async def create_ticket_endpoint(ticket: TicketCreate, db = Depends(get_db)):
    new_ticket = await create_ticket(db, ticket)
    return new_ticket

@router.get("/api/ticket", response_model=TicketResponse)
async def get_tickets_endpoint(db = Depends(get_db)):
    tickets = await get_tickets(db)
    return {"tickets": tickets}

