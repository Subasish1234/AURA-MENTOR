from fastapi import FastAPI

app = FastAPI(title="AURA API")

@app.get("/")
def root():
    return {"message": "AURA Backend Running"}