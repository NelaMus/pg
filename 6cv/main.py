from pydantic import BaseModel

class Flight(BaseModel):
    source_iata: str
    target_iata: str
    departure_date: str
    return_date: str