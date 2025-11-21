import shap
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../dataset/student_performance_numeric_score.csv")

# Load model
model = joblib.load("../model/student_model.pkl")

# Select features
X = df.drop("performance_score", axis=1)

# Initialize SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Create SHAP summary plot
plt.figure()
shap.summary_plot(shap_values, X, show=False)

# Save plot as PNG
output_path = "../model/shap_summary.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"SHAP summary plot saved successfully at: {output_path}")
