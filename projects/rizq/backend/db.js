// Database connection module
// Connects to PostgreSQL using connection pool

const { Pool } = require("pg");

// Create connection pool
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false, // Required for Supabase
  },
});

// Test connection on startup
pool.on("connect", () => {
  console.log("✓ Connected to PostgreSQL database");
});

// Handle errors
pool.on("error", (err) => {
  console.error("Unexpected error on idle client", err);
  process.exit(-1);
});

// Export query function
module.exports = {
  query: (text, params) => pool.query(text, params),
  pool,
};
