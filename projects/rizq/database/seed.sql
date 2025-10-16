-- Rizq Seed Data
-- Test job listings for development

-- Clear existing data
TRUNCATE TABLE halal_verification CASCADE;
TRUNCATE TABLE jobs RESTART IDENTITY CASCADE;
TRUNCATE TABLE scraper_logs RESTART IDENTITY CASCADE;

-- =====================================================
-- Insert Test Jobs
-- =====================================================

-- Job 1: Software Developer at Islamic Relief
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Full Stack Software Developer',
    'Islamic Relief UK',
    'Join our tech team to build platforms that help deliver humanitarian aid worldwide. Work on web applications serving millions. Must have experience with React and Node.js.',
    'Birmingham, UK',
    TRUE,
    'full-time',
    '£40,000 - £55,000',
    ARRAY['React', 'Node.js', 'JavaScript', 'PostgreSQL'],
    'https://example.com/jobs/islamic-relief-dev-001',
    'IslamicJobs',
    TRUE,
    95,
    CURRENT_DATE - INTERVAL '2 days'
);

-- Job 2: Data Analyst at Muslim Aid
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Data Analyst - Impact Measurement',
    'Muslim Aid',
    'Analyze data to measure the impact of our charitable programs. Create visualizations and reports for stakeholders. Experience with Python and data visualization required.',
    'London, UK',
    FALSE,
    'full-time',
    '£35,000 - £45,000',
    ARRAY['Python', 'SQL', 'Data Analysis', 'Excel'],
    'https://example.com/jobs/muslim-aid-analyst-002',
    'HalalJobs',
    TRUE,
    98,
    CURRENT_DATE - INTERVAL '5 days'
);

-- Job 3: Content Writer (Remote)
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Islamic Content Writer',
    'Halal Gems Media',
    'Write engaging Islamic content for our website and social media. Topics include spirituality, lifestyle, and community. Must have excellent English writing skills.',
    'Remote',
    TRUE,
    'freelance',
    '£25 - £40 per hour',
    ARRAY['Writing', 'Islamic Knowledge', 'SEO', 'Content Strategy'],
    'https://example.com/jobs/halalgems-writer-003',
    'IslamicJobs',
    TRUE,
    90,
    CURRENT_DATE - INTERVAL '1 day'
);

-- Job 4: Graphic Designer
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Graphic Designer - Halal Food Brand',
    'Pure Halal Foods Ltd',
    'Design packaging, marketing materials, and social media graphics for our halal food products. Experience with Adobe Creative Suite required.',
    'Manchester, UK',
    TRUE,
    'part-time',
    '£18,000 - £25,000',
    ARRAY['Adobe Illustrator', 'Photoshop', 'Design', 'Branding'],
    'https://example.com/jobs/purehalal-designer-004',
    'Indeed',
    TRUE,
    85,
    CURRENT_DATE - INTERVAL '7 days'
);

-- Job 5: Teacher at Islamic School
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Secondary School Teacher - Mathematics',
    'Al-Furqan Islamic School',
    'Teach mathematics to secondary students (ages 11-16) in an Islamic environment. QTS required. Prayer facilities available.',
    'London, UK',
    FALSE,
    'full-time',
    '£30,000 - £40,000',
    ARRAY['Teaching', 'Mathematics', 'Classroom Management', 'QTS'],
    'https://example.com/jobs/alfurqan-teacher-005',
    'HalalJobs',
    TRUE,
    100,
    CURRENT_DATE - INTERVAL '3 days'
);

-- Job 6: Accountant
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Accountant - Islamic Finance',
    'Al Rayan Bank',
    'Manage accounts for Shariah-compliant banking products. Must understand Islamic finance principles. ACCA or equivalent qualification preferred.',
    'Birmingham, UK',
    FALSE,
    'full-time',
    '£35,000 - £50,000',
    ARRAY['Accounting', 'Islamic Finance', 'ACCA', 'Financial Reporting'],
    'https://example.com/jobs/alrayan-accountant-006',
    'IslamicJobs',
    TRUE,
    95,
    CURRENT_DATE - INTERVAL '10 days'
);

-- Job 7: Marketing Manager
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Digital Marketing Manager',
    'Amaliah Media',
    'Lead digital marketing strategy for Muslim lifestyle platform. Manage social media, email campaigns, and content strategy. Experience with Muslim audience required.',
    'Remote',
    TRUE,
    'full-time',
    '£40,000 - £55,000',
    ARRAY['Digital Marketing', 'Social Media', 'SEO', 'Analytics'],
    'https://example.com/jobs/amaliah-marketing-007',
    'HalalJobs',
    TRUE,
    92,
    CURRENT_DATE
);

-- Job 8: Customer Service
INSERT INTO jobs (
    title, company, description, location, remote, job_type,
    salary_range, required_skills, source_url, source_site,
    halal_verified, verification_score, posted_date
) VALUES (
    'Customer Service Representative',
    'Halal Travel UK',
    'Assist customers with halal holiday bookings. Handle inquiries via phone, email, and chat. Experience in travel industry preferred. Flexible hours available.',
    'Leeds, UK',
    FALSE,
    'part-time',
    '£10 - £12 per hour',
    ARRAY['Customer Service', 'Communication', 'Travel Industry'],
    'https://example.com/jobs/halaltravel-cs-008',
    'Indeed',
    TRUE,
    88,
    CURRENT_DATE - INTERVAL '4 days'
);

-- =====================================================
-- Insert Halal Verification Data
-- =====================================================

-- Verification for Job 1 (Islamic Relief)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, has_prayer_facilities, halal_food_available,
    verification_notes, verified_by
) VALUES (
    1, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Islamic charity organization. Fully compliant with Islamic values. Prayer facilities available.',
    'automated'
);

-- Verification for Job 2 (Muslim Aid)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, has_prayer_facilities, halal_food_available,
    verification_notes, verified_by
) VALUES (
    2, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Islamic humanitarian organization. All programs are Shariah-compliant.',
    'automated'
);

-- Verification for Job 3 (Content Writer)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, verification_notes, verified_by
) VALUES (
    3, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Remote freelance position writing Islamic content. Fully halal.',
    'automated'
);

-- Verification for Job 4 (Graphic Designer)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, halal_food_available, verification_notes, verified_by
) VALUES (
    4, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Halal food company. Products are all Shariah-compliant.',
    'automated'
);

-- Verification for Job 5 (Teacher)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, has_prayer_facilities, halal_food_available,
    verification_notes, verified_by
) VALUES (
    5, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Islamic school with full Islamic environment. Prayer times observed.',
    'automated'
);

-- Verification for Job 6 (Accountant)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, has_prayer_facilities, verification_notes, verified_by
) VALUES (
    6, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Islamic bank operating under Shariah principles. No riba involvement.',
    'automated'
);

-- Verification for Job 7 (Marketing)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, verification_notes, verified_by
) VALUES (
    7, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Muslim lifestyle media platform. Content is halal-focused.',
    'automated'
);

-- Verification for Job 8 (Customer Service)
INSERT INTO halal_verification (
    job_id, no_riba, no_alcohol, no_gambling, no_haram_products,
    ethical_treatment, verification_notes, verified_by
) VALUES (
    8, TRUE, TRUE, TRUE, TRUE, TRUE,
    'Halal travel company specializing in Muslim-friendly holidays.',
    'automated'
);

-- =====================================================
-- Insert Sample Scraper Log
-- =====================================================
INSERT INTO scraper_logs (
    source_site, jobs_found, jobs_added, jobs_updated, jobs_rejected,
    status, duration_seconds
) VALUES (
    'manual_seed',
    8,
    8,
    0,
    0,
    'success',
    0
);

-- =====================================================
-- Verify the data
-- =====================================================
SELECT 
    'Seed data inserted successfully!' AS status,
    (SELECT COUNT(*) FROM jobs) AS total_jobs,
    (SELECT COUNT(*) FROM halal_verification) AS total_verifications;

-- Show sample of inserted jobs
SELECT 
    id,
    title,
    company,
    location,
    remote,
    halal_verified,
    verification_score
FROM jobs
ORDER BY posted_date DESC;