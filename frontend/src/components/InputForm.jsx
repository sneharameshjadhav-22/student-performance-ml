import React, { useState } from "react";
import "./InputForm.css";

function InputForm({ onSubmit }) {
  const [form, setForm] = useState({
    past_marks: "",
    test_scores: "",
    attendance_percent: "",
    assignment_completion_rate: "",
    stress_level: "",
    study_environment_score: "",
    study_time_hours: "",
    health_condition_score: "",
    travel_time_minutes: "",
    sleep_hours: "",
    parental_involvement: "",
    failed_subjects: "",
    internet_usage_hours: "",
    extra_curricular_hours: "",
    social_activity_hours: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: Number(e.target.value) });
  };

  return (
    <div className="input-container">
      {Object.keys(form).map((field) => (
        <input
          key={field}
          name={field}
          type="number"
          placeholder={field.replace(/_/g, " ")}
          value={form[field]}
          onChange={handleChange}
        />
      ))}

      <button onClick={() => onSubmit(form)}>Predict Student Score</button>
    </div>
  );
}

export default InputForm;
