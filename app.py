 
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests
from chatbot_ai import extract_city

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "1e7129ac0c020be4f8ebe408e46e4441"

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat/{question}")
def chat(question: str):
    city = extract_city(question)
    print("Detected city:",city)

    if city is None:
        return {"reply": "Please tell the city name 😊"}
         

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    if data.get("cod") != 200:
        return {"reply": "City not found 😢"}

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return {"reply": f"Weather in {city}: {temp}°C, {desc}"}

