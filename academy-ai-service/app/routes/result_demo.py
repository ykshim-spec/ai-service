from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["result-demo"])

_BASE = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=str(_BASE / "templates"))

_SAMPLE_RESULT = {
    "track_title": "사회복지사 2급 추천 경로",
    "estimated_period": "약 1년",
    "summary": "고졸 기준으로 학점은행제 과정을 통해 사회복지사 자격 취득을 준비하는 기본 경로입니다.",
    "recommended_steps": [
        "현재 학력 기준으로 필요한 이수 경로를 확인합니다.",
        "과목 이수 및 실습 일정을 함께 설계합니다.",
        "자격 취득까지의 예상 기간과 등록 계획을 안내받습니다.",
    ],
    "caution_note": "최종 이수 기간과 인정 범위는 기존 학력 및 이수 이력에 따라 달라질 수 있습니다.",
    "next_action": "추천 경로 자세히 보기",
}

@router.get("/result-demo")
def result_demo(request: Request):
    return templates.TemplateResponse(
        request,
        "result_demo.html",
        {"result": _SAMPLE_RESULT},
    )
