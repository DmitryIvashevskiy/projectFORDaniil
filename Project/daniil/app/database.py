import asyncpg

DATABASE_URL = "postgresql://user:password@localhost/dbname"

async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    query = """
    CREATE TABLE IF NOT EXISTS tickets (
        id UUID PRIMARY KEY,
        source_system VARCHAR(255),
        name VARCHAR(255),
        status VARCHAR(255),
        time_create TIMESTAMP,
        time_to_resolve TIMESTAMP,
        time_to_solve TIMESTAMP
    )
    """
    await conn.execute(query)
    await conn.close()
    
async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

