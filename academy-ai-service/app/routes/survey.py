from typing import Literal
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/survey", tags=["survey"])

Goal = Literal["social_worker_2", "social_worker_1"]
EducationLevel = Literal[
    "highschool",
    "college_dropout",
    "college_graduate",
    "university_graduate",
]
SocialWelfareBackground = Literal["none", "partial_courses", "related_major"]
DesiredPace = Literal["fastest", "within_1_year", "relaxed"]
ConsultationPreference = Literal["result_only", "consult_now"]

class SocialWorkerSurveyBody(BaseModel):
    goal: Goal
    education_level: EducationLevel
    social_welfare_background: SocialWelfareBackground
    desired_pace: DesiredPace
    consultation_preference: ConsultationPreference

@router.post("/start")
def survey_start(body: SocialWorkerSurveyBody):
    return {
        "ok": True,
        "message": "survey started",
        "survey_type": "social_worker",
    }

def _estimated_period(education_level: EducationLevel) -> str:
    if education_level == "highschool":
        return "약 1년 ~ 1년 6개월"
    if education_level in ("college_graduate", "university_graduate"):
        return "약 8개월 ~ 1년"
    return "약 1년 ~ 1년 3개월"

def _base_summary(education_level: EducationLevel) -> str:
    if education_level == "highschool":
        return "고졸 기준 학점은행제 경로로 진행하는 기본 설계입니다."
    if education_level == "college_dropout":
        return "대학 중퇴 기준 학점은행제 경로로 진행하는 기본 설계입니다."
    if education_level == "college_graduate":
        return "전문대 졸업 기준 학점은행제 경로로 진행하는 기본 설계입니다."
    return "대졸 기준 학점은행제 경로로 진행하는 기본 설계입니다."

def _track_title(goal: Goal) -> str:
    if goal == "social_worker_2":
        return "사회복지사 2급 추천 경로"
    return "사회복지사 1급 추천 경로"

@router.post("/result")
def survey_result(body: SocialWorkerSurveyBody):
    period = _estimated_period(body.education_level)
    summary = _base_summary(body.education_level)

    if body.social_welfare_background == "related_major":
        summary = f"{summary} 기존 이수 이력을 반영한 단축 가능 경로입니다."

    if body.consultation_preference == "consult_now":
        next_action = "상담 연결 권장"
    else:
        next_action = "상세 설계 보기"

    return {
        "ok": True,
        "track_title": _track_title(body.goal),
        "estimated_period": period,
        "summary": summary,
        "next_action": next_action,
    }
