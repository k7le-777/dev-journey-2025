// Rizq Backend API Server
// Node.js + Express + PostgreSQL

require("dotenv").config();
const express = require("express");
const cors = require("cors");
const db = require("./db");

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(
  cors({
    origin: process.env.FRONTEND_URL || "*",
    credentials: true,
  })
);
app.use(express.json());

// Welcome message
console.log("==================================================");
console.log("🚀 Rizq API Server Running");
console.log(`📍 http://localhost:${PORT}`);
console.log("🕌 Bismillah - In the name of Allah");
console.log("==================================================");

// ============================================
// ROUTES
// ============================================

// Health check endpoint
app.get("/api/health", (req, res) => {
  res.json({
    status: "ok",
    message: "Rizq API is running",
    timestamp: new Date().toISOString(),
  });
});

// Get all jobs with optional filters
app.get("/api/jobs", async (req, res) => {
  try {
    const { location, remote, type, halal, limit = 20, offset = 0 } = req.query;

    // Build dynamic SQL query
    let query = `
      SELECT 
        j.id,
        j.title,
        j.company,
        j.description,
        j.location,
        j.remote,
        j.job_type,
        j.salary_range,
        j.required_skills,
        j.source_url,
        j.posted_date,
        j.is_active,
        j.halal_verified,
        hv.no_riba,
        hv.no_alcohol,
        hv.no_gambling,
        hv.no_haram_products,
        hv.ethical_treatment,
        hv.overall_score
      FROM jobs j
      LEFT JOIN halal_verification hv ON j.id = hv.job_id
      WHERE j.is_active = true
    `;

    const params = [];
    let paramCount = 1;

    // Add filters
    if (location) {
      query += ` AND j.location ILIKE $${paramCount}`;
      params.push(`%${location}%`);
      paramCount++;
    }

    if (remote !== undefined) {
      query += ` AND j.remote = $${paramCount}`;
      params.push(remote === "true");
      paramCount++;
    }

    if (type) {
      query += ` AND j.job_type = $${paramCount}`;
      params.push(type);
      paramCount++;
    }

    if (halal === "true") {
      query += ` AND j.halal_verified = true`;
    }

    // Order by newest first
    query += ` ORDER BY j.posted_date DESC`;

    // Add pagination
    query += ` LIMIT $${paramCount} OFFSET $${paramCount + 1}`;
    params.push(parseInt(limit), parseInt(offset));

    const result = await db.query(query, params);

    res.json({
      success: true,
      count: result.rows.length,
      jobs: result.rows,
    });
  } catch (error) {
    console.error("Error fetching jobs:", error);
    res.status(500).json({
      success: false,
      error: "Failed to fetch jobs",
    });
  }
});

// Get single job by ID with full details
app.get("/api/jobs/:id", async (req, res) => {
  try {
    const { id } = req.params;

    const query = `
      SELECT 
        j.*,
        hv.no_riba,
        hv.no_alcohol,
        hv.no_gambling,
        hv.no_haram_products,
        hv.ethical_treatment,
        hv.overall_score,
        hv.verification_notes
      FROM jobs j
      LEFT JOIN halal_verification hv ON j.id = hv.job_id
      WHERE j.id = $1 AND j.is_active = true
    `;

    const result = await db.query(query, [id]);

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        error: "Job not found",
      });
    }

    res.json({
      success: true,
      job: result.rows[0],
    });
  } catch (error) {
    console.error("Error fetching job:", error);
    res.status(500).json({
      success: false,
      error: "Failed to fetch job",
    });
  }
});

// Search jobs by keyword
app.get("/api/jobs/search", async (req, res) => {
  try {
    const { q, limit = 20, offset = 0 } = req.query;

    if (!q) {
      return res.status(400).json({
        success: false,
        error: "Search query required",
      });
    }

    const query = `
      SELECT 
        j.id,
        j.title,
        j.company,
        j.description,
        j.location,
        j.remote,
        j.job_type,
        j.salary_range,
        j.required_skills,
        j.halal_verified,
        hv.overall_score
      FROM jobs j
      LEFT JOIN halal_verification hv ON j.id = hv.job_id
      WHERE j.is_active = true
      AND (
        j.title ILIKE $1 OR
        j.company ILIKE $1 OR
        j.description ILIKE $1 OR
        $2 = ANY(j.required_skills)
      )
      ORDER BY j.posted_date DESC
      LIMIT $3 OFFSET $4
    `;

    const searchTerm = `%${q}%`;
    const result = await db.query(query, [
      searchTerm,
      q.toLowerCase(),
      parseInt(limit),
      parseInt(offset),
    ]);

    res.json({
      success: true,
      count: result.rows.length,
      query: q,
      jobs: result.rows,
    });
  } catch (error) {
    console.error("Error searching jobs:", error);
    res.status(500).json({
      success: false,
      error: "Failed to search jobs",
    });
  }
});

// Get platform statistics
app.get("/api/stats", async (req, res) => {
  try {
    const statsQuery = `
      SELECT 
        COUNT(*) as total_jobs,
        COUNT(*) FILTER (WHERE halal_verified = true) as verified_jobs,
        COUNT(*) FILTER (WHERE remote = true) as remote_jobs,
        COUNT(DISTINCT company) as total_companies,
        COUNT(*) FILTER (WHERE job_type = 'full-time') as fulltime_jobs,
        COUNT(*) FILTER (WHERE job_type = 'part-time') as parttime_jobs,
        COUNT(*) FILTER (WHERE job_type = 'freelance') as freelance_jobs
      FROM jobs
      WHERE is_active = true
    `;

    const result = await db.query(statsQuery);
    const stats = result.rows[0];

    // Calculate percentages
    const totalJobs = parseInt(stats.total_jobs);

    res.json({
      success: true,
      stats: {
        total_jobs: totalJobs,
        verified_jobs: parseInt(stats.verified_jobs),
        verification_rate:
          totalJobs > 0
            ? Math.round((stats.verified_jobs / totalJobs) * 100)
            : 0,
        remote_jobs: parseInt(stats.remote_jobs),
        remote_rate:
          totalJobs > 0 ? Math.round((stats.remote_jobs / totalJobs) * 100) : 0,
        total_companies: parseInt(stats.total_companies),
        by_type: {
          fulltime: parseInt(stats.fulltime_jobs),
          parttime: parseInt(stats.parttime_jobs),
          freelance: parseInt(stats.freelance_jobs),
        },
      },
    });
  } catch (error) {
    console.error("Error fetching stats:", error);
    res.status(500).json({
      success: false,
      error: "Failed to fetch statistics",
    });
  }
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: "Endpoint not found",
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`✓ Server listening on port ${PORT}`);
});

// Test database connection on startup
db.query("SELECT NOW()", (err, res) => {
  if (err) {
    console.error("❌ Database connection failed:", err.message);
  } else {
    console.log("✓ Connected to PostgreSQL database");
  }
});
