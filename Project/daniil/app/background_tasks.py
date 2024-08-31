import random
from datetime import datetime
from .database import get_db
from .models import Ticket

async def check_and_send_expired_tickets():
    async with get_db() as conn:
        now = datetime.utcnow()
        query = "SELECT * FROM tickets WHERE time_to_resolve <= $1 AND source_system = 'client'"
        expired_tickets = await conn.fetch(query, now)
        for ticket in expired_tickets:
            # Simulate sending a message
            print(f"Sending message for ticket: {ticket['id']}")

async def change_status_of_tickets():
    async with get_db() as conn:
        query = "SELECT * FROM tickets WHERE status = 'New' AND source_system = 'client'"
        new_tickets = await conn.fetch(query)
        if new_tickets:
            tickets_to_update = random.sample(new_tickets, k=min(3, len(new_tickets)))
            for ticket in tickets_to_update:
                update_query = "UPDATE tickets SET status = 'Waiting for response' WHERE id = $1"
                await conn.execute(update_query, ticket['id'])
                print(f"Ticket status updated: {ticket['id']}")
