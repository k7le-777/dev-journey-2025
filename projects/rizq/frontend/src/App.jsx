import { useEffect, useState } from "react";
import api from "./services/api";
import JobCard from "./components/JobCard";
import SearchBar from "./components/SearchBar";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [filteredJobs, setFilteredJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({});

  // Fetch all jobs on mount
  useEffect(() => {
    fetchJobs();
  }, []);

  // Apply filters whenever they change
  useEffect(() => {
    applyFilters();
  }, [jobs, filters]);

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

  function applyFilters() {
    let filtered = [...jobs];

    // Filter by remote
    if (filters.remote !== undefined) {
      filtered = filtered.filter((job) => job.remote === filters.remote);
    }

    // Filter by job type
    if (filters.type) {
      filtered = filtered.filter((job) => job.job_type === filters.type);
    }

    setFilteredJobs(filtered);
  }

  async function handleSearch(searchTerm) {
    if (!searchTerm.trim()) {
      
      setFilteredJobs(jobs);
      return;
    }

    // Search locally in the jobs array
    const searchLower = searchTerm.toLowerCase();
    const results = jobs.filter(
      (job) =>
        job.title.toLowerCase().includes(searchLower) ||
        job.company.toLowerCase().includes(searchLower) ||
        job.description?.toLowerCase().includes(searchLower) ||
        job.required_skills?.some((skill) =>
          skill.toLowerCase().includes(searchLower)
        )
    );

    setFilteredJobs(results);
  }

  function handleFilterChange(newFilters) {
    setFilters(newFilters);
  }

  if (loading) {
    return (
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          minHeight: "100vh",
        }}
      >
        <div style={{ textAlign: "center" }}>
          <div
            style={{
              fontSize: "48px",
              marginBottom: "16px",
            }}
          >
            ⏳
          </div>
          <p style={{ fontSize: "18px", color: "#6b7280" }}>
            Loading halal opportunities...
          </p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          minHeight: "100vh",
        }}
      >
        <div
          style={{
            backgroundColor: "#fee2e2",
            border: "1px solid #fca5a5",
            borderRadius: "12px",
            padding: "24px",
            maxWidth: "500px",
          }}
        >
          <p
            style={{
              color: "#991b1b",
              fontSize: "18px",
              marginBottom: "8px",
              fontWeight: "600",
            }}
          >
            ❌ Error Loading Jobs
          </p>
          <p style={{ color: "#7f1d1d" }}>{error}</p>
          <button
            onClick={fetchJobs}
            style={{
              marginTop: "16px",
              padding: "8px 16px",
              backgroundColor: "#dc2626",
              color: "white",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer",
            }}
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  const displayJobs = filteredJobs.length > 0 ? filteredJobs : jobs;

  return (
    <div
      style={{
        minHeight: "100vh",
        padding: "40px 20px",
        backgroundColor: "#f9fafb",
      }}
    >
      <div
        style={{
          maxWidth: "1000px",
          margin: "0 auto",
        }}
      >
        {/* Header */}
        <div style={{ marginBottom: "32px" }}>
          <h1
            style={{
              fontSize: "48px",
              fontWeight: "bold",
              marginBottom: "8px",
              color: "#111827",
              display: "flex",
              alignItems: "center",
              gap: "12px",
            }}
          >
            <span>🕌</span>
            <span>Rizq</span>
          </h1>
          <p
            style={{
              fontSize: "20px",
              color: "#6b7280",
              marginBottom: "8px",
            }}
          >
            Halal Income Opportunities - Dignity Through Work
          </p>
          <p
            style={{
              fontSize: "16px",
              color: "#16a34a",
              fontWeight: "600",
            }}
          >
            ✅ {displayJobs.length} Verified Halal Jobs Available
          </p>
        </div>

        {/* Search and Filters */}
        <SearchBar
          onSearch={handleSearch}
          onFilterChange={handleFilterChange}
        />

        {/* Active Filters Display */}
        {(filters.remote || filters.type) && (
          <div
            style={{
              padding: "12px 16px",
              backgroundColor: "#dbeafe",
              borderRadius: "8px",
              marginBottom: "16px",
              fontSize: "14px",
              color: "#1e40af",
            }}
          >
            <strong>Active Filters:</strong>
            {filters.remote && " Remote Jobs"}
            {filters.type && ` ${filters.type}`}
          </div>
        )}

        {/* Job Count */}
        <p
          style={{
            fontSize: "14px",
            color: "#6b7280",
            marginBottom: "16px",
          }}
        >
          Showing {displayJobs.length} of {jobs.length} jobs
        </p>

        {/* Jobs List */}
        {displayJobs.length === 0 ? (
          <div
            style={{
              backgroundColor: "white",
              padding: "48px",
              borderRadius: "12px",
              textAlign: "center",
            }}
          >
            <p
              style={{
                fontSize: "48px",
                marginBottom: "16px",
              }}
            >
              🔍
            </p>
            <p
              style={{
                fontSize: "18px",
                color: "#6b7280",
              }}
            >
              No jobs found matching your criteria
            </p>
            <button
              onClick={() => {
                setFilters({});
                setFilteredJobs(jobs);
              }}
              style={{
                marginTop: "16px",
                padding: "10px 24px",
                backgroundColor: "#16a34a",
                color: "white",
                border: "none",
                borderRadius: "8px",
                cursor: "pointer",
              }}
            >
              View All Jobs
            </button>
          </div>
        ) : (
          <div>
            {displayJobs.map((job) => (
              <JobCard key={job.id} job={job} />
            ))}
          </div>
        )}

        {/* Footer */}
        <div
          style={{
            marginTop: "48px",
            padding: "24px",
            backgroundColor: "white",
            borderRadius: "12px",
            textAlign: "center",
            border: "1px solid #e5e7eb",
          }}
        >
          <p
            style={{
              fontSize: "14px",
              color: "#6b7280",
              marginBottom: "8px",
            }}
          >
            Built with ❤️ for the Ummah
          </p>
          <p
            style={{
              fontSize: "12px",
              color: "#9ca3af",
            }}
          >
            "The upper hand is better than the lower hand" - Prophet Muhammad ﷺ
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
