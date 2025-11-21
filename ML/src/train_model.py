import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("../dataset/student_performance_numeric_score.csv")

# Split features and label
X = df.drop("performance_score", axis=1)
y = df["performance_score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=300, random_state=42)

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "../model/student_model.pkl")

print("Model training completed!")
