from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from app.auth import authenticate_user, create_access_token, verify_token

app = FastAPI()

classifier = pipeline("text-classification", device=-1)

class TextInput(BaseModel):
    text: str
    
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    if not authenticate_user(data.username, data.password):
        raise HTTPException(status_code=401, detail= 'Invalid Credentials')
    token = create_access_token({'sub': data.username})
    return {'access_token': token, 'token_type': 'bearer'}

@app.post("/predict")
def predict(input_data: TextInput, user=Depends(verify_token)):
    result = classifier(input_data.text)
    return {
        "user": user,
        "label": result[0]["label"],
        "score": round(result[0]["score"], 4)}
    
@app.get("/")
def root():
    return {"message": "Welcome to the NLP Text Classification API"}