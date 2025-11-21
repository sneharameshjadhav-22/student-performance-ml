import React from "react";

const XAIExplanation = ({ shapImage }) => {
  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Why did the model predict this score?</h3>
      <p>The graph below shows how different features affected your performance score.</p>

      {shapImage ? (
        <img
          src={shapImage}
          alt="XAI SHAP Explanation"
          style={{ width: "60%", borderRadius: "10px", marginTop: "10px" }}
        />
      ) : (
        <p style={{ color: "gray" }}>No XAI image generated yet.</p>
      )}
    </div>
  );
};

export default XAIExplanation;
