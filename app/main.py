from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Interview Intelligence API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "AI Interview Intelligence API"}
