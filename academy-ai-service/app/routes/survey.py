from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class StartRequest(BaseModel):
    name: str
    phone: str
    interest: str

class ResultRequest(BaseModel):
    interest: str
    education_level: str
    goal: str

@router.post("/survey/start")
def survey_start(req: StartRequest):
    return {"ok": True, "message": "survey started"}

@router.post("/survey/result")
def survey_result(req: ResultRequest):
    return {
        "ok": True,
        "track": "사회복지사 2급 기본 경로",
        "next_action": "상담 연결 권장"
    }
