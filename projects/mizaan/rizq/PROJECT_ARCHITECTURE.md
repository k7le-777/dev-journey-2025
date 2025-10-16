# Rizq - Halal Income Opportunity Platform
## Complete Technical Architecture

**Version:** 1.0  
**Author:** Kyle Burns  
**Date:** OCT 2025  
**Timeline:** Days 8-28 (21 days)

---

## Executive Summary

**Mission:** Connect Muslims with verified halal income opportunities, emphasizing dignity of labor and economic self-reliance.

**Quranic Foundation:** Surah Al-Mulk 67:15 - "It is He who made the earth tame for you - so walk among its slopes and eat of His provision."

**Core Value Proposition:** Muslim professionals and job seekers can find employment opportunities that align with Islamic values, with transparent halal verification.

---

## System Architecture

### High-Level Components

```
┌─────────────────────────────────────────────────┐
│                  USER BROWSER                   │
│                  (Any Device)                   │
└─────────────┬───────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────┐
│             FRONTEND (React)                    │
│  - Job listings with search/filter              │
│  - Halal verification display                   │
│  - Responsive UI (Tailwind CSS)                 │
└─────────────┬───────────────────────────────────┘
              │ HTTP Requests (REST API)
              ▼
┌─────────────────────────────────────────────────┐
│           BACKEND (Node.js + Express)           │
│  - API endpoints for jobs                       │
│  - Search and filter logic                      │
│  - Database queries                             │
└─────────────┬───────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────┐
│           DATABASE (PostgreSQL)                 │
│  - Job listings                                 │
│  - Halal verification data                      │
│  - Platform statistics                          │
└─────────────▲───────────────────────────────────┘
              │
              │ Daily Updates
┌─────────────┴───────────────────────────────────┐
│          SCRAPER (Python Scripts)               │
│  - Scrape multiple job sources                  │
│  - Apply halal filters                          │
│  - Detect duplicates                            │
│  - Schedule: Daily at 2 AM                      │
└─────────────────────────────────────────────────┘
```

---

## Technology Stack

### Frontend
- **Framework:** React 18
- **Styling:** Tailwind CSS 3
- **Icons:** Lucide React
- **Routing:** React Router v6
- **HTTP Client:** Axios
- **Deployment:** Vercel

### Backend
- **Runtime:** Node.js 18+
- **Framework:** Express 4
- **Database Client:** node-postgres (pg)
- **Environment:** dotenv
- **CORS:** cors middleware
- **Deployment:** Render / Railway

### Database
- **System:** PostgreSQL 15
- **Hosting:** Supabase (free tier)
- **ORM:** Raw SQL (learn fundamentals first)

### Scraper
- **Language:** Python 3.13
- **Libraries:** 
  - BeautifulSoup4 (HTML parsing)
  - Requests (HTTP)
  - psycopg2 (PostgreSQL connection)
  - schedule (task scheduling)

### DevOps
- **Version Control:** Git + GitHub
- **Environment Variables:** .env files
- **Deployment:** 
  - Frontend: Vercel
  - Backend: Render
  - Database: Supabase
  - Scraper: Cron job (Render or local)

---

## Database Schema

### Table: `jobs`

```sql
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    remote BOOLEAN DEFAULT FALSE,
    job_type VARCHAR(50), -- 'full-time', 'part-time', 'contract', 'freelance'
    salary_range VARCHAR(100),
    required_skills TEXT[], -- Array of skills
    source_url TEXT UNIQUE NOT NULL,
    source_site VARCHAR(100),
    halal_verified BOOLEAN DEFAULT FALSE,
    verification_score INTEGER, -- 0-100
    posted_date DATE,
    scraped_at TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_jobs_active ON jobs(is_active);
CREATE INDEX idx_jobs_location ON jobs(location);
CREATE INDEX idx_jobs_remote ON jobs(remote);
CREATE INDEX idx_jobs_halal ON jobs(halal_verified);
```

### Table: `halal_verification`

```sql
CREATE TABLE halal_verification (
    id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES jobs(id) ON DELETE CASCADE,
    no_riba BOOLEAN DEFAULT TRUE,
    no_alcohol BOOLEAN DEFAULT TRUE,
    no_gambling BOOLEAN DEFAULT TRUE,
    no_haram_products BOOLEAN DEFAULT TRUE,
    ethical_treatment BOOLEAN DEFAULT TRUE,
    has_prayer_facilities BOOLEAN DEFAULT NULL,
    halal_food_available BOOLEAN DEFAULT NULL,
    verification_notes TEXT,
    verified_at TIMESTAMP DEFAULT NOW(),
    verified_by VARCHAR(100) DEFAULT 'automated'
);
```

### Table: `scraper_logs`

```sql
CREATE TABLE scraper_logs (
    id SERIAL PRIMARY KEY,
    source_site VARCHAR(100) NOT NULL,
    jobs_found INTEGER,
    jobs_added INTEGER,
    jobs_updated INTEGER,
    jobs_rejected INTEGER,
    run_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50), -- 'success', 'failed', 'partial'
    error_message TEXT
);
```

---

## API Endpoints

### Jobs

**GET /api/jobs**
- Get all active jobs with optional filters
- Query params: 
  - `location`: Filter by location
  - `remote`: Filter remote jobs (boolean)
  - `job_type`: Filter by type
  - `halal_only`: Show only verified (boolean)
  - `skills`: Comma-separated skills
  - `limit`: Results per page (default: 20)
  - `offset`: Pagination offset

**GET /api/jobs/:id**
- Get single job details
- Includes halal verification data

**GET /api/jobs/search**
- Search jobs by keyword
- Query params:
  - `q`: Search query
  - All filters from GET /api/jobs

**GET /api/stats**
- Platform statistics
- Returns:
  - Total jobs
  - Halal verified count
  - Jobs by type
  - Top locations
  - Recent additions

---

## Halal Verification System

### Automated Checks (Keyword-based)

**Red Flags (Reject automatically):**
- "alcohol", "wine", "liquor", "brewery"
- "casino", "gambling", "betting"
- "interest rate", "loan officer", "mortgage"
- "nightclub", "bar", "pub"
- "pork", "bacon", "ham"

**Yellow Flags (Manual review needed):**
- "bank" (some Islamic banks are halal)
- "restaurant" (may serve halal or haram)
- "retail" (depends on products sold)

**Green Signals (Likely halal):**
- "halal", "Islamic", "Muslim"
- "charity", "nonprofit", "NGO"
- "education", "tech", "healthcare"

### Verification Score (0-100)

```
Score = (criteria_met / total_criteria) × 100

Criteria:
1. No riba involvement (25 points)
2. No alcohol/gambling (25 points)
3. No haram products (20 points)
4. Ethical treatment (15 points)
5. Muslim-friendly environment (15 points)
```

---

## Frontend Pages & Features

### 1. Home/Landing Page (`/`)

**Sections:**
- Hero section with search bar
- Featured halal-verified jobs
- Platform statistics
- Islamic foundation quote
- Call-to-action

### 2. Jobs Listing Page (`/jobs`)

**Features:**
- Search bar (top)
- Filters sidebar:
  - Location
  - Remote (checkbox)
  - Job type (dropdown)
  - Halal verified only (toggle)
  - Salary range
- Job cards grid:
  - Company logo placeholder
  - Job title
  - Company name
  - Location / Remote
  - Salary range
  - Halal verification badge (✅ or pending)
  - Posted date
  - "View Details" button

### 3. Job Detail Page (`/jobs/:id`)

**Sections:**
- Job title & company
- Location, type, salary
- Halal verification status (detailed)
- Full description
- Required skills (chips/tags)
- "Apply" button (external link)
- Share buttons
- Report inaccurate button

### 4. About Page (`/about`)

**Content:**
- Mission statement
- Quranic foundation (67:15)
- Hadith on dignity of labor
- How halal verification works
- Team/contact information

---

## Scraper Implementation

### Base Scraper Class

```python
class BaseScraper:
    def __init__(self, source_name):
        self.source = source_name
        self.jobs_found = 0
        self.jobs_added = 0
        
    def fetch_page(self, url):
        """Fetch HTML from URL"""
        
    def parse_job(self, html_element):
        """Extract job data from HTML element"""
        
    def apply_halal_filter(self, job_data):
        """Check if job passes halal criteria"""
        
    def save_to_db(self, job_data):
        """Insert job into PostgreSQL"""
        
    def run(self):
        """Main scraping flow"""
```

### Individual Scrapers

**1. IslamicJobs.com Scraper**
- URL: https://www.islamicjobs.com/
- Strategy: BeautifulSoup HTML parsing
- Frequency: Daily
- Halal assumption: High (Islamic site)

**2. HalalJobs.co.uk Scraper**
- URL: https://halaljobs.co.uk/
- Strategy: BeautifulSoup HTML parsing
- Frequency: Daily
- Halal assumption: High (Halal-focused)

**3. Indeed.com Scraper (Filtered)**
- Strategy: Search for Muslim-friendly keywords
- Keywords: "halal", "Islamic", "Muslim", "charity"
- Filter: Apply strict halal checks
- Frequency: Daily
- Halal assumption: Low (must verify)

### Duplicate Detection

```python
def is_duplicate(new_job, existing_jobs):
    # Check by source URL (exact match)
    if new_job.source_url in existing_urls:
        return True
    
    # Check by title + company (fuzzy match)
    if similar(new_job.title, existing.title) > 0.85 and \
       new_job.company == existing.company:
        return True
    
    return False
```

---

## Deployment Strategy

### Phase 1: Local Development (Days 8-21)
- Run backend locally (localhost:5000)
- Run frontend locally (localhost:3000)
- PostgreSQL local or Supabase
- Manual scraper runs

### Phase 2: Staging Deployment (Day 25-26)
- Deploy backend to Render
- Deploy frontend to Vercel
- Connect to Supabase PostgreSQL
- Test everything works online

### Phase 3: Production (Day 27)
- Configure custom domain (optional)
- Setup scraper cron job
- Monitoring and logging
- Create demo video

### Environment Variables

**Backend (.env):**
```
DATABASE_URL=postgresql://user:pass@host:port/db
PORT=5000
NODE_ENV=production
```

**Frontend (.env):**
```
VITE_API_URL=https://rizq-api.render.com
```

**Scraper (.env):**
```
DATABASE_URL=postgresql://user:pass@host:port/db
```

---

## Development Timeline

### Week 1: Foundation (Days 8-14)
- **Day 8:** Complete architecture planning ✓
- **Day 9:** Database schema + setup Supabase
- **Day 10:** Backend skeleton (Express + PostgreSQL connection)
- **Day 11:** Basic API endpoints (GET /jobs, GET /jobs/:id)
- **Day 12:** Frontend skeleton (React + Tailwind setup)
- **Day 13:** Frontend routing + basic pages
- **Day 14:** Connect frontend to backend (axios setup)

### Week 2: Core Features (Days 15-21)
- **Day 15:** Python scraper base class
- **Day 16:** Implement 1-2 scrapers
- **Day 17:** Halal filter logic
- **Day 18:** Test scraping + database insertion
- **Day 19:** Frontend job listing page
- **Day 20:** Frontend job detail page
- **Day 21:** Search and filter functionality

### Week 3: Polish & Deploy (Days 22-28)
- **Day 22:** Halal verification display
- **Day 23:** About page + Islamic content
- **Day 24:** UI polish (mobile responsive)
- **Day 25:** Deploy backend to Render
- **Day 26:** Deploy frontend to Vercel
- **Day 27:** Setup scraper automation
- **Day 28:** Testing + Demo video

---

## Success Metrics

### Technical Success
- ✅ 100+ jobs aggregated
- ✅ 3+ sources scraped
- ✅ Search < 1 second response
- ✅ Mobile responsive
- ✅ Deployed and accessible online

### Islamic Success
- ✅ Halal verification for all jobs
- ✅ Islamic foundation clearly stated
- ✅ Educational about dignity of labor
- ✅ No riba/haram employment listed

### User Success
- ✅ 10+ people find opportunities
- ✅ Feedback collected
- ✅ Muslims report usefulness
- ✅ Could scale to production

---

## Risks & Mitigation

### Risk 1: Scraping gets blocked
**Mitigation:** 
- Rotate user agents
- Add delays between requests
- Use multiple sources
- Manual fallback option

### Risk 2: Halal verification inaccurate
**Mitigation:**
- Conservative filters (reject if unsure)
- Manual review queue
- User reporting system
- Disclaimer about verification

### Risk 3: No jobs in database
**Mitigation:**
- Seed with manual entries
- Multiple scraping sources
- Lower frequency if needed
- Focus on 1-2 reliable sources initially

---

## Future Enhancements (Post-Day 28)

**V2 Features:**
- User accounts (save jobs, set alerts)
- Company profiles
- Application tracking
- Mentorship matching
- Business starter kits
- Mobile app (React Native)
- Multi-language (Arabic, Urdu)

---

## Islamic Integration Points

**Throughout Platform:**
1. **Bismillah** on home page
2. **Quranic verse** (67:15) prominently displayed
3. **Hadith** on dignity of labor in About
4. **Dua** for job seekers
5. **Halal verification** as core feature
6. **Empowerment messaging** (not just employment)
7. **Charity mindset** (help others find work)

---

**Last Updated:** [Date]  
**Status:** Planning Complete → Ready for Implementation  
**Next Step:** Day 9 - Database Setup & Schema Implementation