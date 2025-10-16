import { useEffect, useState } from "react";
import api from "./services/api";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchJobs() {
      try {
        const data = await api.getJobs();
        setJobs(data.jobs);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    }
    fetchJobs();
  }, []);

  if (loading)
    return (
      <div style={{ padding: "40px", textAlign: "center" }}>
        Loading jobs...
      </div>
    );
  if (error)
    return (
      <div style={{ padding: "40px", textAlign: "center", color: "red" }}>
        Error: {error}
      </div>
    );

  return (
    <div style={{ minHeight: "100vh", padding: "40px" }}>
      <div style={{ maxWidth: "900px", margin: "0 auto" }}>
        <h1
          style={{ fontSize: "36px", fontWeight: "bold", marginBottom: "10px" }}
        >
          🕌 Rizq - Halal Income Opportunities
        </h1>
        <p style={{ color: "#666", marginBottom: "40px" }}>
          Found {jobs.length} halal job opportunities
        </p>

        <div>
          {jobs.map((job) => (
            <div
              key={job.id}
              style={{
                backgroundColor: "white",
                border: "1px solid #e5e7eb",
                borderRadius: "8px",
                padding: "24px",
                marginBottom: "16px",
                boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
              }}
            >
              <h2
                style={{
                  fontSize: "24px",
                  fontWeight: "600",
                  marginBottom: "8px",
                }}
              >
                {job.title}
              </h2>
              <p
                style={{
                  fontSize: "18px",
                  color: "#374151",
                  marginBottom: "4px",
                }}
              >
                {job.company}
              </p>
              <p
                style={{
                  fontSize: "14px",
                  color: "#6b7280",
                  marginBottom: "12px",
                }}
              >
                {job.location} {job.remote && "• Remote"}
              </p>
              <p style={{ color: "#16a34a", fontWeight: "500" }}>
                {job.salary_range}
              </p>
              {job.halal_verified && (
                <div
                  style={{
                    marginTop: "12px",
                    display: "inline-block",
                    padding: "6px 12px",
                    backgroundColor: "#dcfce7",
                    color: "#166534",
                    borderRadius: "20px",
                    fontSize: "14px",
                    fontWeight: "500",
                  }}
                >
                  ✅ 100% Halal Verified
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
