// JobCard Component - Individual job listing card

const JobCard = ({ job }) => {
  return (
    <div
      style={{
        backgroundColor: "white",
        border: "1px solid #e5e7eb",
        borderRadius: "12px",
        padding: "24px",
        marginBottom: "16px",
        boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
        transition: "all 0.2s",
        cursor: "pointer",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.15)";
        e.currentTarget.style.transform = "translateY(-2px)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.boxShadow = "0 1px 3px rgba(0,0,0,0.1)";
        e.currentTarget.style.transform = "translateY(0)";
      }}
    >
      {/* Job Title */}
      <h2
        style={{
          fontSize: "24px",
          fontWeight: "600",
          marginBottom: "8px",
          color: "#111827",
        }}
      >
        {job.title}
      </h2>

      {/* Company */}
      <p
        style={{
          fontSize: "18px",
          color: "#374151",
          marginBottom: "8px",
          fontWeight: "500",
        }}
      >
        🏢 {job.company}
      </p>

      {/* Location and Remote */}
      <p
        style={{
          fontSize: "14px",
          color: "#6b7280",
          marginBottom: "12px",
        }}
      >
        📍 {job.location}{" "}
        {job.remote && <span style={{ color: "#3b82f6" }}>• 🌐 Remote</span>}
      </p>

      {/* Job Type and Salary */}
      <div
        style={{
          display: "flex",
          gap: "12px",
          alignItems: "center",
          marginBottom: "12px",
        }}
      >
        <span
          style={{
            padding: "4px 12px",
            backgroundColor: "#f3f4f6",
            borderRadius: "6px",
            fontSize: "13px",
            color: "#4b5563",
            textTransform: "capitalize",
          }}
        >
          {job.job_type}
        </span>

        <span
          style={{
            color: "#16a34a",
            fontWeight: "600",
            fontSize: "16px",
          }}
        >
          💰 {job.salary_range}
        </span>
      </div>

      {/* Skills */}
      {job.required_skills && job.required_skills.length > 0 && (
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "8px",
            marginBottom: "12px",
          }}
        >
          {job.required_skills.slice(0, 4).map((skill, index) => (
            <span
              key={index}
              style={{
                padding: "4px 10px",
                backgroundColor: "#dbeafe",
                color: "#1e40af",
                borderRadius: "6px",
                fontSize: "12px",
                fontWeight: "500",
              }}
            >
              {skill}
            </span>
          ))}
        </div>
      )}

      {/* Halal Verification Badge */}
      {job.halal_verified && (
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: "6px",
            padding: "8px 16px",
            backgroundColor: "#dcfce7",
            color: "#166534",
            borderRadius: "20px",
            fontSize: "14px",
            fontWeight: "600",
          }}
        >
          <span>✅</span>
          <span>100% Halal Verified</span>
          <span
            style={{
              fontSize: "12px",
              fontWeight: "400",
              color: "#15803d",
            }}
          >
            (Score: {job.overall_score}/100)
          </span>
        </div>
      )}
    </div>
  );
};

export default JobCard;
