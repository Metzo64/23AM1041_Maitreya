from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import joblib

app = FastAPI()


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    mean_radius: float = Form(...),
    mean_texture: float = Form(...),
    mean_perimeter: float = Form(...)
):


    features = [mean_radius, mean_texture, mean_perimeter] + [0]*27

    features = np.array(features).reshape(1, -1)

    scaled = scaler.transform(features)

    prediction = model.predict(scaled)

    result = "Malignant (Cancer)" if prediction[0] == 0 else "Benign (No Cancer)"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": result}
    )