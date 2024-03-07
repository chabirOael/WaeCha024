from fastapi import FastAPI, Body, HTTPException
import uvicorn
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
classifier = pipeline("text-classification", model="waelChr/tc")  

class TextInput(BaseModel):
    text: str | list[str]  # Accept either str or list of str

class PredictionResult(BaseModel):
    text: str
    label: str
    score: float

@app.post("/classify", response_model=list[PredictionResult]) 
def classify_text(request: TextInput = Body(...)):
    # Handle single string input
    if isinstance(request.text, str):  
        predictions = classifier(request.text)
        prediction_dict = predictions[0]
        label = prediction_dict["label"]
        score = prediction_dict["score"]
        return [{"text": request.text, "label": label, "score": score}]  

    # Handle list of strings
    elif isinstance(request.text, list):  
        predictions = classifier(request.text)
        results = []
        for text in request.text:
            predictions = classifier(text)
            prediction_dict = predictions[0]
            label = prediction_dict["label"]
            score = prediction_dict["score"]
            results.append({"text": text, "label": label, "score": score})
        return results

    else:
        raise HTTPException(status_code=400, detail="Input must be a string or a list of strings")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
