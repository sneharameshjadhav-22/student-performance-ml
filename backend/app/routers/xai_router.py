from fastapi import APIRouter
from fastapi.responses import FileResponse
import joblib
import numpy as np
import shap
import matplotlib.pyplot as plt
import os

from app.schemas.student_schema import StudentInput

router = APIRouter(prefix="/xai", tags=["Explainability"])

model = joblib.load("app/models/student_model.pkl")
explainer = joblib.load("app/ml/explainer.pkl")


@router.post("/image")
def generate_shap_image(data: StudentInput):

    input_array = np.array([[ 
        data.past_marks, data.test_scores, data.attendance_percent,
        data.assignment_completion_rate, data.stress_level,
        data.study_environment_score, data.study_time_hours,
        data.health_condition_score, data.travel_time_minutes,
        data.sleep_hours, data.parental_involvement, data.failed_subjects,
        data.internet_usage_hours, data.extra_curricular_hours,
        data.social_activity_hours
    ]])

    shap_values = explainer.shap_values(input_array)

    plt.clf()
    plt.figure(figsize=(8, 6))

    # 🔥 USE THIS — works 100%
    shap.summary_plot(shap_values, input_array, show=False)

    save_dir = "app/xai_plots"
    os.makedirs(save_dir, exist_ok=True)

    filepath = os.path.join(save_dir, "shap_plot.png")

    plt.savefig(filepath, bbox_inches="tight")
    plt.close()

    return FileResponse(filepath, media_type="image/png")
