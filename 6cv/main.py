from fastapi import FastAPI
from typing import List
from models import Flight, FlightResponse  # Import modelů z models.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# FastAPI aplikace
app = FastAPI()

# Funkce pro získání letů z webu WizzAir
def get_flights_from_website(url: str):
    # Spuštění Chrome WebDriveru s webdriver-manager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    # Načtení stránky
    driver.get(url)
    
    # Počkání na načtení dat
    time.sleep(5)

    flights = []
    
    # Pokus o získání dat
    try:
        flight_elements = driver.find_elements(By.CSS_SELECTOR, ".flight-card")
        
        for flight in flight_elements:
            airline = "Wizz Air"  # Zde předpokládáme, že letecká společnost je vždy Wizz Air
            price = float(flight.find_element(By.CSS_SELECTOR, ".current-price").text.strip("€").replace(",", "."))
            departure_time = flight.find_element(By.CSS_SELECTOR, ".flight-card__time--departure").text
            arrival_time = flight.find_element(By.CSS_SELECTOR, ".flight-card__time--arrival").text
            
            flights.append({
                "airline": airline,
                "price": price,
                "departure_time": departure_time,
                "arrival_time": arrival_time
            })
    except Exception as e:
        print(f"Chyba při extrahování dat: {e}")
    
    driver.quit()  # Zavření prohlížeče
    return flights

# API endpoint pro získání seznamu letů
@app.get("/flights", response_model=FlightResponse)
async def get_flights():
    url = "https://www.wizzair.com/cs-cz/booking/select-flight/VIE/TFS/2025-04-03/2025-04-08/1/0/0/null"
    flights_data = get_flights_from_website(url)
    
    # Mapování dat na Flight model
    flight_objects = [Flight(**flight) for flight in flights_data]
    return FlightResponse(flights=flight_objects)

# Pokud spustíš aplikaci, použij uvicorn pro nasazení FastAPI:
# uvicorn main:app --reload
