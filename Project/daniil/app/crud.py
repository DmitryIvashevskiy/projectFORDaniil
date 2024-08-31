import uuid
from datetime import datetime
import asyncpg
from .models import TicketCreate, Ticket

async def create_ticket(conn, ticket: TicketCreate):
    ticket_id = str(uuid.uuid4())
    time_create = datetime.utcnow()
    query = """
    INSERT INTO tickets (id, source_system, name, status, time_create, time_to_resolve, time_to_solve)
    VALUES ($1, $2, $3, $4, $5, $6, $7)
    RETURNING id, source_system, name, status, time_create, time_to_resolve
    """
    row = await conn.fetchrow(query, ticket_id, ticket.source_system, ticket.name, ticket.status, time_create, ticket.timeToSolve, ticket.timeToSolve)
    return Ticket(id=row['id'], source_system=row['source_system'], name=row['name'], status=row['status'], timeCreate=row['time_create'], timeToResolve=row['time_to_resolve'])

async def get_tickets(conn):
    query = "SELECT id, source_system, name, status, time_create, time_to_resolve FROM tickets"
    rows = await conn.fetch(query)
    tickets = [Ticket(id=row['id'], source_system=row['source_system'], name=row['name'], status=row['status'], timeCreate=row['time_create'], timeToResolve=row['time_to_resolve']) for row in rows]
    return tickets

