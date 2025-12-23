import React, { useState } from "react";
import "../App.css"; // Adjust if your CSS file path is different

function Fake_News() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");
  const [confidence, setConfidence] = useState(null); // Changed initial state to null
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (!text.trim()) return;

    setLoading(true);
    setResult("");
    setConfidence(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      console.log("Server response:", data);

      if (data.prediction && typeof data.confidence !== "undefined") {
        setResult(data.prediction);
        // Ensure confidence is converted to number if it comes as string
        setConfidence(Number(data.confidence));
      } else {
        console.error("Invalid server response format", data);
        setResult("error");
      }
    } catch (error) {
      console.error("Prediction error:", error);
      setResult("error");
      alert("Server error! Please check if backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1>
          Fake News{" "}
          <span role="img" aria-label="news">
            📰
          </span>{" "}
          Detector
        </h1>

        <textarea
          placeholder="Paste your news article here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          rows={10}
        />

        <button onClick={handlePredict} disabled={!text.trim() || loading}>
          {loading ? "Predicting..." : "Predict"}
        </button>

        {result && (
          <div
            className={`result ${
              result === "Fake" ? "fake" : result === "Real" ? "real" : "error"
            }`}
          >
            {result === "Fake"
              ? "⚠️ Looks like Fake News 📰"
              : result === "Real"
              ? "✅ Looks Real News 📰"
              : "❌ Something went wrong. Please try again!"}
          </div>
        )}

        {confidence !== null && !isNaN(confidence) && (
          <div className="confidence">
            Confidence: {(confidence * 100).toFixed(2)}%
          </div>
        )}
      </div>
    </div>
  );
}

export default Fake_News;
