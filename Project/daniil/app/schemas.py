from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

class TicketCreate(BaseModel):
    source_system: str
    name: str
    status: str
    timeToSolve: datetime

class Ticket(BaseModel):
    id: uuid.UUID
    source_system: str
    name: str
    status: str
    timeCreate: datetime
    timeToResolve: datetime

class TicketResponse(BaseModel):
    tickets: List[Ticket]

