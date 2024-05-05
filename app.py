from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client

# Initialize FastAPI app
app = FastAPI()

# Initialize Gradio Client
gradio_client = Client("https://70d454cda5e3d6a6eb.gradio.live/")

class PredictionInput(BaseModel):
    url_input: str

@app.post("/predict")
async def predict(input_data: PredictionInput):
    # Make prediction using gradio_client
    result = gradio_client.predict(url_input=input_data.url_input, api_name="/predict")
    return {"prediction_result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
