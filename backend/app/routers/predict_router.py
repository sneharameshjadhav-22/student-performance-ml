from fastapi import APIRouter
import joblib
import numpy as np
from app.models.predict_model import StudentInput

router = APIRouter()

# Load model only once
model = joblib.load("app/models/student_model.pkl")

@router.post("/predict")
def predict_score(data: StudentInput):

    # Convert input into array
    input_data = np.array([[
        data.past_marks,
        data.test_scores,
        data.attendance_percent,
        data.assignment_completion_rate,
        data.stress_level,
        data.study_environment_score,
        data.study_time_hours,
        data.health_condition_score,
        data.travel_time_minutes,
        data.sleep_hours,
        data.parental_involvement,
        data.failed_subjects,
        data.internet_usage_hours,
        data.extra_curricular_hours,
        data.social_activity_hours
    ]])

    # Predict
    prediction = model.predict(input_data)[0]

    return {
        "predicted_score": round(float(prediction), 2)
    }
