from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.survey import router as survey_router

app = FastAPI()

app.include_router(health_router)
app.include_router(survey_router)
