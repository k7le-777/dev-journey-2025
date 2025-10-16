// SearchBar Component - Search and filter jobs

import { useState } from "react";

const SearchBar = ({ onSearch, onFilterChange }) => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = (e) => {
    e.preventDefault();
    onSearch(searchTerm);
  };

  return (
    <div
      style={{
        backgroundColor: "white",
        padding: "24px",
        borderRadius: "12px",
        marginBottom: "24px",
        boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
      }}
    >
      {/* Search Form */}
      <form onSubmit={handleSearch} style={{ marginBottom: "16px" }}>
        <div style={{ display: "flex", gap: "12px" }}>
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search jobs (e.g., developer, marketing, teacher)..."
            style={{
              flex: 1,
              padding: "12px 16px",
              border: "2px solid #e5e7eb",
              borderRadius: "8px",
              fontSize: "16px",
              outline: "none",
              transition: "border-color 0.2s",
            }}
            onFocus={(e) => (e.target.style.borderColor = "#3b82f6")}
            onBlur={(e) => (e.target.style.borderColor = "#e5e7eb")}
          />

          <button
            type="submit"
            style={{
              padding: "12px 32px",
              backgroundColor: "#16a34a",
              color: "white",
              border: "none",
              borderRadius: "8px",
              fontSize: "16px",
              fontWeight: "600",
              cursor: "pointer",
              transition: "background-color 0.2s",
            }}
            onMouseEnter={(e) => (e.target.style.backgroundColor = "#15803d")}
            onMouseLeave={(e) => (e.target.style.backgroundColor = "#16a34a")}
          >
            🔍 Search
          </button>
        </div>
      </form>

      {/* Filter Buttons */}
      <div
        style={{
          display: "flex",
          gap: "12px",
          flexWrap: "wrap",
        }}
      >
        <span
          style={{
            fontSize: "14px",
            color: "#6b7280",
            marginRight: "8px",
            alignSelf: "center",
          }}
        >
          Filter:
        </span>

        <button
          onClick={() => onFilterChange({ remote: true })}
          style={{
            padding: "8px 16px",
            backgroundColor: "#f3f4f6",
            border: "1px solid #d1d5db",
            borderRadius: "8px",
            fontSize: "14px",
            cursor: "pointer",
            transition: "all 0.2s",
          }}
          onMouseEnter={(e) => {
            e.target.style.backgroundColor = "#3b82f6";
            e.target.style.color = "white";
          }}
          onMouseLeave={(e) => {
            e.target.style.backgroundColor = "#f3f4f6";
            e.target.style.color = "#000";
          }}
        >
          🌐 Remote Only
        </button>

        <button
          onClick={() => onFilterChange({ type: "full-time" })}
          style={{
            padding: "8px 16px",
            backgroundColor: "#f3f4f6",
            border: "1px solid #d1d5db",
            borderRadius: "8px",
            fontSize: "14px",
            cursor: "pointer",
            transition: "all 0.2s",
          }}
          onMouseEnter={(e) => {
            e.target.style.backgroundColor = "#3b82f6";
            e.target.style.color = "white";
          }}
          onMouseLeave={(e) => {
            e.target.style.backgroundColor = "#f3f4f6";
            e.target.style.color = "#000";
          }}
        >
          💼 Full-Time
        </button>

        <button
          onClick={() => onFilterChange({ type: "part-time" })}
          style={{
            padding: "8px 16px",
            backgroundColor: "#f3f4f6",
            border: "1px solid #d1d5db",
            borderRadius: "8px",
            fontSize: "14px",
            cursor: "pointer",
            transition: "all 0.2s",
          }}
          onMouseEnter={(e) => {
            e.target.style.backgroundColor = "#3b82f6";
            e.target.style.color = "white";
          }}
          onMouseLeave={(e) => {
            e.target.style.backgroundColor = "#f3f4f6";
            e.target.style.color = "#000";
          }}
        >
          ⏰ Part-Time
        </button>

        <button
          onClick={() => onFilterChange({})}
          style={{
            padding: "8px 16px",
            backgroundColor: "#fef3c7",
            border: "1px solid #fbbf24",
            borderRadius: "8px",
            fontSize: "14px",
            cursor: "pointer",
            transition: "all 0.2s",
          }}
          onMouseEnter={(e) => (e.target.style.backgroundColor = "#fde68a")}
          onMouseLeave={(e) => (e.target.style.backgroundColor = "#fef3c7")}
        >
          🔄 Clear Filters
        </button>
      </div>
    </div>
  );
};

export default SearchBar;
