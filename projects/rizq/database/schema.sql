-- Rizq Database Schema
-- Halal Income Opportunity Platform
-- Author: Kyle Burns
-- Date: OCT 2025

-- Drop tables if they exist (for clean re-runs)
DROP TABLE IF EXISTS scraper_logs CASCADE;
DROP TABLE IF EXISTS halal_verification CASCADE;
DROP TABLE IF EXISTS jobs CASCADE;

-- =====================================================
-- Table: jobs
-- Core table storing all job opportunities
-- =====================================================
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    remote BOOLEAN DEFAULT FALSE,
    job_type VARCHAR(50) CHECK (job_type IN ('full-time', 'part-time', 'contract', 'freelance', 'internship')),
    salary_range VARCHAR(100),
    required_skills TEXT[],  -- Array of skills
    source_url TEXT UNIQUE NOT NULL,
    source_site VARCHAR(100),
    halal_verified BOOLEAN DEFAULT FALSE,
    verification_score INTEGER CHECK (verification_score >= 0 AND verification_score <= 100),
    posted_date DATE,
    scraped_at TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for faster queries
CREATE INDEX idx_jobs_active ON jobs(is_active);
CREATE INDEX idx_jobs_location ON jobs(location);
CREATE INDEX idx_jobs_remote ON jobs(remote);
CREATE INDEX idx_jobs_halal ON jobs(halal_verified);
CREATE INDEX idx_jobs_posted ON jobs(posted_date DESC);
CREATE INDEX idx_jobs_skills ON jobs USING GIN(required_skills);  -- GIN index for array searches

-- =====================================================
-- Table: halal_verification
-- Detailed halal verification criteria for each job
-- =====================================================
CREATE TABLE halal_verification (
    id SERIAL PRIMARY KEY,
    job_id INTEGER NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    no_riba BOOLEAN DEFAULT TRUE,
    no_alcohol BOOLEAN DEFAULT TRUE,
    no_gambling BOOLEAN DEFAULT TRUE,
    no_haram_products BOOLEAN DEFAULT TRUE,
    ethical_treatment BOOLEAN DEFAULT TRUE,
    has_prayer_facilities BOOLEAN DEFAULT NULL,
    halal_food_available BOOLEAN DEFAULT NULL,
    verification_notes TEXT,
    verified_at TIMESTAMP DEFAULT NOW(),
    verified_by VARCHAR(100) DEFAULT 'automated',
    UNIQUE(job_id)  -- One verification per job
);

-- =====================================================
-- Table: scraper_logs
-- Track scraper runs for monitoring and debugging
-- =====================================================
CREATE TABLE scraper_logs (
    id SERIAL PRIMARY KEY,
    source_site VARCHAR(100) NOT NULL,
    jobs_found INTEGER DEFAULT 0,
    jobs_added INTEGER DEFAULT 0,
    jobs_updated INTEGER DEFAULT 0,
    jobs_rejected INTEGER DEFAULT 0,
    run_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50) CHECK (status IN ('success', 'failed', 'partial')),
    error_message TEXT,
    duration_seconds INTEGER
);

-- Index for viewing recent logs
CREATE INDEX idx_scraper_logs_date ON scraper_logs(run_at DESC);

-- =====================================================
-- Trigger: Update updated_at timestamp automatically
-- =====================================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_jobs_updated_at 
    BEFORE UPDATE ON jobs 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();

-- =====================================================
-- Comments for documentation
-- =====================================================
COMMENT ON TABLE jobs IS 'Core table storing all job opportunities aggregated from multiple sources';
COMMENT ON TABLE halal_verification IS 'Detailed halal verification criteria for each job listing';
COMMENT ON TABLE scraper_logs IS 'Audit log of scraper runs for monitoring and debugging';

COMMENT ON COLUMN jobs.halal_verified IS 'Boolean indicating if job has passed halal verification checks';
COMMENT ON COLUMN jobs.verification_score IS 'Score 0-100 indicating confidence in halal status';
COMMENT ON COLUMN jobs.required_skills IS 'PostgreSQL array of skill strings for this job';
COMMENT ON COLUMN jobs.source_url IS 'Original URL of job posting (must be unique)';

-- =====================================================
-- Success message
-- =====================================================
SELECT 'Database schema created successfully!' AS status;