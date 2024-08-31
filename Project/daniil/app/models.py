class TicketCreate:
    def __init__(self, source_system: str, name: str, status: str, timeToSolve: str):
        self.source_system = source_system
        self.name = name
        self.status = status
        self.timeToSolve = timeToSolve


class Ticket:
    def __init__(self, id: str, source_system: str, name: str, status: str, timeCreate: str, timeToResolve: str):
        self.id = id
        self.source_system = source_system
        self.name = name
        self.status = status
        self.timeCreate = timeCreate
        self.timeToResolve = timeToResolve
    
