import React from "react";
import "./ResultSection.css";

function ResultSection({ prediction, recommendations }) {
  if (prediction === null) return null;

  return (
    <div className="result-card">
      <h2>📌 Predicted Score: <span className="score">{prediction}</span></h2>

      <h3>📝 Recommended Actions</h3>
      <ul>
        {recommendations.length > 0 ? (
          recommendations.map((r, i) => <li key={i}>{r}</li>)
        ) : (
          <li>No recommendations generated</li>
        )}
      </ul>
    </div>
  );
}

export default ResultSection;
