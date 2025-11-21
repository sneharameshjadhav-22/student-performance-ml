import joblib
import shap
import pandas as pd

# Correct paths
model = joblib.load("../model/student_model.pkl")
df = pd.read_csv("../dataset/student_performance_numeric_score.csv")

# Use the actual column name
X = df.drop(columns=["performance_score"])

explainer = shap.TreeExplainer(model)

joblib.dump(explainer, "../model/explainer.pkl")

print("Explainer saved!")
