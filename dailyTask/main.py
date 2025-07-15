from fastapi import FastAPI
from dailyTask.routes import router
from dailyTask.database import create_index

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await create_index()