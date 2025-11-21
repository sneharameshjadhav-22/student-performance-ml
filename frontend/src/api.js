const API_BASE = "http://127.0.0.1:8000";

export const predictScore = async (data) => {
  const res = await fetch(`${API_BASE}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return await res.json();
};

export const getXAIImage = () => {
  return `${API_BASE}/xai`;  // this returns SHAP image URL
};
