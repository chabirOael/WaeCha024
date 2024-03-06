from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
classifier = pipeline("text-classification", model="waelChr/tc")  

class TextInput(BaseModel):
    text: str

class PredictionResult(BaseModel):
    text: str
    label: str
    score: float

@app.post("/classify", response_model=PredictionResult)
def classify_text(request: TextInput = Body(...)):
    predictions = classifier(request.text)
    prediction_dict = predictions[0] 
    label = prediction_dict["label"]
    score = prediction_dict["score"]

    return {"text":request.text, "label": label, "score": score} 

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
