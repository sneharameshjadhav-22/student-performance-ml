from pydantic import BaseModel

class StudentInput(BaseModel):
    past_marks: float
    test_scores: float
    attendance_percent: float
    assignment_completion_rate: float
    stress_level: float
    study_environment_score: float
    study_time_hours: float
    health_condition_score: float
    travel_time_minutes: float
    sleep_hours: float
    parental_involvement: float
    failed_subjects: float
    internet_usage_hours: float
    extra_curricular_hours: float
    social_activity_hours: float
