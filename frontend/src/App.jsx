import React, { useState } from "react";
import InputForm from "./components/InputForm";
import ResultSection from "./components/ResultSection";
import XAIExplanation from "./components/XAIExplanation";

function App() {
  const [prediction, setPrediction] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [shapImage, setShapImage] = useState(null);

  const handleSubmit = async (formData) => {
    try {
      console.log("Sending Data:", formData);

      // 1️⃣ Predict Score API
      const predictRes = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!predictRes.ok) throw new Error("Prediction failed");
      const predictData = await predictRes.json();
      setPrediction(predictData.predicted_score);

      // 2️⃣ Recommendation API
      const recRes = await fetch(
        "http://127.0.0.1:8000/recommend/recommend",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formData),
        }
      );

      if (!recRes.ok) throw new Error("Recommendation failed");
      const recData = await recRes.json();
      setRecommendations(recData.recommendations);

      // 3️⃣ XAI SHAP Image API
      const xaiRes = await fetch("http://127.0.0.1:8000/xai/image", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!xaiRes.ok) throw new Error("XAI image fetch failed");

      const blob = await xaiRes.blob();
      setShapImage(URL.createObjectURL(blob));

    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong! Check backend logs.");
    }
  };

  return (
    <div style={{ padding: "25px", fontFamily: "Arial" }}>
      <h1 style={{ marginBottom: "20px" }}>
        🎓 Student Performance Prediction System
      </h1>

      <InputForm onSubmit={handleSubmit} />

      <ResultSection
        prediction={prediction}
        recommendations={recommendations}
      />

      <XAIExplanation shapImage={shapImage} />
    </div>
  );
}

export default App;
