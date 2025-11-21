from fastapi import APIRouter
from app.schemas.student_schema import StudentInput

router = APIRouter(prefix="/recommend", tags=["Recommendations"])

@router.post("/recommend")
def recommend(data: StudentInput):

    rec = []

    if data.past_marks < 60:
        rec.append("Focus on improving your basics through revision classes or online videos.")

    if data.study_time_hours < 1:
        rec.append("Increase daily study time to at least 1–2 hours.")

    if data.failed_subjects > 0:
        rec.append("Create a recovery plan for failed subjects with extra practice sessions.")

    if data.attendance_percent < 75:
        rec.append("Increase class attendance to above 85% for better understanding.")

    if data.stress_level > 3:
        rec.append("Practice stress-relief activities like yoga, meditation, or breaks.")

    if data.sleep_hours < 6:
        rec.append("Increase sleep to maintain at least 7–8 hours daily.")

    if data.internet_usage_hours > 4:
        rec.append("Reduce internet usage to avoid distractions.")

    if not rec:
        rec.append("You are doing well! Maintain consistency and keep practicing.")

    return {"recommendations": rec}
