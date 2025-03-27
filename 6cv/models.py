from pydantic import BaseModel
from typing import List

# Model pro jednotlivý let
class Flight(BaseModel):
    airline: str
    price: float
    departure_time: str
    arrival_time: str

# Odpověď pro API, která obsahuje seznam letů
class FlightResponse(BaseModel):
    flights: List[Flight]
