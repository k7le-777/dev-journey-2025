# Mizaan + Rizq: Quranic Economic Empowerment Tools

## Mission Statement
To build tools that embody Quranic economic principles, helping Muslims achieve prosperity with piety, balance in spending, and dignity in earning. These projects serve as sadaqah jariyah and practical application of divine guidance in daily economic life.

---

## PROJECT 1: MIZAAN - BALANCED SPENDING TRACKER

### Quranic Foundation

**Primary Verse:**
*"And those who, when they spend, are neither extravagant nor niggardly, but hold a medium way between those extremes."* - Quran 25:67

**Supporting Guidance:**
- *"...and do not commit excess. Indeed, He does not like those who commit excess."* - Quran 6:141
- *"And do not make your hand [as] chained to your neck or extend it completely and [thereby] become blamed and insolvent."* - Quran 17:29
- *"And give the relative his right, and [also] the poor and the traveler, and do not spend wastefully."* - Quran 17:26
- *"O you who have believed, spend from the good things which you have earned..."* - Quran 2:267

**Hadith Foundation:**
- "The best of wealth is that which is earned through one's own effort." - Bukhari
- "Richness is not having many possessions, but richness is being content with oneself." - Bukhari

### Core Problem Statement

**Problem:** Muslims lack practical tools that integrate Quranic spending ethics into daily financial decisions.

**Specific Pain Points:**
1. Current budgeting apps ignore Islamic principles entirely
2. Muslims struggle to define "balanced" spending practically
3. Zakat calculation is confusing and often inaccurate
4. No tools help identify wasteful vs. necessary spending from Islamic perspective
5. Brand culture (Qarun mindset) goes unchallenged in financial tools

**Why This Matters:**
Financial decisions are spiritual decisions. Every purchase either brings us closer to or further from Quranic balance. Without tools that integrate Islamic ethics, Muslims default to secular financial frameworks that may contradict divine guidance.

### Target Users

**Primary User 1: Young Muslim Professional**
- Age 25-35
- Earning modest income (£30-50k/year)
- Wants to live Islamically but struggles with consumer culture
- Unsure if zakat calculations are correct
- Desires balance between enjoying provision and avoiding excess

**Primary User 2: Muslim Family (Head of Household)**
- Age 30-50
- Managing family budget
- Wants to teach children Islamic spending values
- Struggles with distinguishing needs vs. wants
- Seeks tools that reinforce Quranic principles

**Secondary Users:**
- New Muslims learning Islamic financial ethics
- Students managing limited budgets Islamically
- Muslims recovering from debt seeking structure

### MVP Features (Weeks 3-4)

#### Core Functionality
1. **Expense Entry System**
   - Manual entry (amount, category, date, description)
   - CSV import (bank statement compatibility)
   - Quick-add for common expenses

2. **Quranic Categorization Framework**
   - **Daruriyyat (Essential):** Food, shelter, basic clothing, healthcare, education
   - **Hajiyyat (Needed):** Transportation, modest comfort, communication tools
   - **Tahsiniyyat (Improvements):** Quality upgrades, halal entertainment, travel
   - **Israf (Wasteful):** Excessive spending, brand obsession, impulse purchases
   - **Haram:** Prohibited spending (riba, gambling, alcohol, etc.)

3. **Balance Algorithm**
    - Input: Monthly income + Expenses by category
    - Calculate: Ideal proportions based on income level

- Essential: 50-60%
- Needed: 20-30%
- Improvements: 10-15%
- Savings/Charity: 10-20% 
- Wasteful: 0%

    - Output: Balance Score (0-100) + Specific recommendations

4. **Zakat Calculator**
   - Track zakatable assets (cash, savings, gold, silver, business inventory)
   - Automatic nisab calculation (live gold/silver prices)
   - Hijri calendar integration (lunar year tracking)
   - Zakat due alerts

5. **Insights Dashboard**
   - Monthly spending breakdown with Quranic categories
   - Balance score with trend (improving/declining)
   - Wasteful spending identification
   - Surplus calculation → Sadaqah suggestions
   - Islamic reminders based on spending patterns

6. **Islamic Guidance Integration**
   - Context-sensitive Quranic verses
   - Hadith reminders for overspending/hoarding
   - Balanced spending affirmations

#### Technical Architecture

**Backend:**
- Python 3.13 + Flask
- SQLAlchemy ORM
- PostgreSQL database
- RESTful API design

**Frontend:**
- HTML5 + CSS3 (responsive)
- Vanilla JavaScript
- Chart.js for visualizations

**External Integrations:**
- Gold/silver price API (for nisab calculation)
- Hijri date conversion library
- CSV parsing (Pandas)

**Database Schema:**
- Users: id, name, email, monthly_income, created_at
- Expenses: id, user_id, amount, category, subcategory, date, description, is_necessary
- ZakatTracking: id, user_id, zakatable_assets, nisab_threshold, zakat_due, hijri_year
- BalanceScores: id, user_id, month, score, category_percentages, recommendations

### Success Metrics

**Technical Success:**
- Deployed and accessible online
- 100% test coverage for zakat calculations
- <2 second page load time
- Mobile responsive design

**User Success (Month 1):**
- 50 active users tracking expenses
- £50,000+ in zakat accurately calculated
- 10+ user testimonials about improved spending awareness

**Impact Success (Month 3):**
- Users report 20% average reduction in wasteful spending
- 100+ users fulfilling zakat obligations accurately
- 5+ success stories of debt elimination using Mizaan principles

**Barakah Indicators:**
- Users share it organically with Muslim community
- Mosques/Islamic centers recommend it
- Open-source contributions from other Muslim developers

---

## PROJECT 2: RIZQ - HALAL INCOME OPPORTUNITY PLATFORM

### Quranic Foundation

**Primary Verse:**
*"It is He who made the earth tame for you - so walk among its slopes and eat of His provision..."* - Quran 67:15

**Supporting Guidance:**
- *"And when the prayer has been concluded, disperse within the land and seek from the bounty of Allah..."* - Quran 62:10
- *"So seek provision from Allah and worship Him..."* - Quran 29:17
- *"Indeed, Allah is the [continual] Provider, the firm possessor of strength."* - Quran 51:58
- *"O mankind, eat from whatever is on earth [that is] lawful and good..."* - Quran 2:168

**Hadith Foundation:**
- "Nobody has ever eaten a better meal than that which one has earned by working with one's own hands." - Bukhari
- "The upper hand is better than the lower hand (i.e., the spending hand is better than the receiving hand)." - Bukhari
- "Truthful and trustworthy merchant will be with the prophets, the truthful and the martyrs." - Tirmidhi

### Core Problem Statement

**Problem:** Muslims struggle to find verified halal income opportunities that provide dignity and self-reliance.

**Specific Pain Points:**
1. No centralized platform for halal-verified job opportunities
2. Muslims unknowingly work for companies dealing in haram (riba, alcohol, etc.)
3. Charity culture creates dependency rather than empowerment
4. Talented Muslims lack connections to halal freelance/business opportunities
5. No emphasis on dignity of labor from Islamic perspective

**Why This Matters:**
The Quran commands economic participation and self-reliance. Empowering Muslims to earn halal income is the highest form of charity - it transforms people from charity receivers to charity givers, restoring dignity and function in society.

### Target Users

**Primary User 1: Unemployed/Underemployed Muslim**
- Seeking dignified halal work
- May have skills but lacks connections
- Wants to ensure income source is halal
- Desires to move from receiving charity to giving charity

**Primary User 2: Muslim Professional Seeking Career Change**
- Currently in job with questionable halal status
- Willing to earn less for halal certainty
- Has skills but needs halal opportunities
- Values Islamic work environment

**Secondary Users:**
- Recent Muslim graduates entering workforce
- Muslim freelancers seeking halal clients
- Aspiring Muslim entrepreneurs needing business ideas
- Muslims seeking side income (halal side hustles)

### MVP Features (Weeks 5-6)

#### Core Functionality

1. **Job Aggregation System**
   - Web scraping from multiple sources:
     - Islamic job boards (IslamicJobs, HalalJobs)
     - General job sites (filtered by halal criteria)
     - Remote work platforms
     - Freelance marketplaces (Upwork, Fiverr - filtered)
   - Daily automated updates
   - Duplicate detection

2. **Halal Verification Framework**
   - Automated filtering (keywords: riba, alcohol, gambling, etc.)
   - Manual verification for flagged opportunities
   - Company halal rating system
   - User-reported verification
   - Clear disclosure of verification status

3. **User Profile System**
   - Skills inventory
   - Experience level
   - Location/remote preferences
   - Availability (full-time, part-time, freelance)
   - Job alert preferences

4. **Intelligent Matching Algorithm**
    - Input: User profile + All opportunities
    - Score each opportunity:

- Skill match (40%)
- Experience fit (25%)
- Location preference (15%)
- Halal verification score (20%)

    - Output: Ranked list of best matches

5. **Empowerment Features**
   - Success stories (Muslims who found work/started businesses)
   - Skill development resources (free/affordable courses)
   - Business starter kits (halal side business templates)
   - Mentorship connection (experienced Muslims help newcomers)
   - Community support (not just transactions)

6. **Islamic Integration**
   - Dua for seeking provision
   - Hadith on dignity of work
   - Reminders: Work is ibadah with right intention
   - Success stories framed as Allah's provision

#### Technical Architecture

**Backend:**
- Node.js + Express (REST API)
- Python (web scraping scripts - Beautiful Soup/Scrapy)
- PostgreSQL database
- Redis (caching for fast searches)
- JWT authentication

**Frontend:**
- React 18
- Tailwind CSS
- Lucide React icons
- React Router

**Scraping Infrastructure:**
- Scheduled cron jobs (daily scraping)
- Rotating user agents
- Rate limiting compliance
- Error handling/retry logic

**Deployment:**
- Docker containerization
- Heroku/Render hosting
- CI/CD pipeline

**Database Schema:**
- Users: id, name, email, password_hash, skills[], experience_level, location, preferences
- Opportunities: id, title, company, description, required_skills[], location, remote, salary_range, type, source_url, halal_verified, posted_date
- Matches: id, user_id, opportunity_id, match_score, viewed, applied
- SuccessStories: id, user_id (optional), title, story, outcome, approved

### Success Metrics

**Technical Success:**
- Aggregate 100+ halal opportunities within Week 1
- Search results <1 second response time
- 95%+ uptime
- Mobile-responsive design

**User Success (Month 1):**
- 100 registered users
- 1000+ opportunities viewed
- 50+ applications submitted through platform
- 10+ users report finding opportunities

**Impact Success (Month 3):**
- 10 confirmed hires through platform
- 5 documented success stories
- £200k+ in halal income generated through platform connections
- 20+ users transition from charity receivers to self-sufficient

**Barakah Indicators:**
- Muslim communities share platform organically
- Users volunteer to help verify opportunities
- Mentorship connections form naturally
- Platform becomes known as trusted halal income resource

---

## How Mizaan + Rizq Work Together

### The Complete Economic Framework
* QURANIC ECONOMIC CYCLE:

- EARN (Rizq) → Find halal, dignified income
- SPEND (Mizaan) → Balance spending Islamically
- SAVE → Emergency fund + Future goals
- GIVE → Zakat (obligation) + Sadaqah (voluntary)
- REINVEST → Business/education (back to EARN)

**Future Integration Possibilities:**
- Mizaan identifies surplus → Rizq suggests investment in Muslim businesses
- Rizq user finds job → Mizaan helps budget new income Islamically
- Both platforms share success metrics: comprehensive economic empowerment
- API integration: One profile, both tools working together

### Complementary Strengths

**Mizaan addresses:** "How do I manage the wealth I have?"
**Rizq addresses:** "How do I earn halal wealth with dignity?"

Together: Complete Quranic economic empowerment.

---

## Long-term Vision (6-12 Months Post-Launch)

### Expansion Features

**Mizaan V2:**
- Mobile app (iOS/Android)
- Family accounts (multiple users, one budget)
- Financial literacy courses (Islamic finance basics)
- Investment tracking (halal stocks, business ownership)
- Debt elimination planner (riba-free alternatives)

**Rizq V2:**
- Micro-investment platform (profit-sharing in Muslim businesses)
- Skills assessment tool (gap analysis + learning paths)
- Muslim business directory (support ummah economy)
- Internship/apprenticeship matching
- Global expansion (beyond English-speaking markets)

### Business Model (Halal Monetization)

**Freemium Model:**
- **Free tier:** Basic features for all (empowerment for everyone)
- **Premium tier (£5-10/month):**
  - Advanced analytics and insights
  - Priority job alerts
  - Multiple account management
  - Export features for tax filing
  - No ads

**B2B Opportunities:**
- Islamic financial institutions (white-label integration)
- Mosques/Islamic centers (community subscriptions)
- Muslim businesses (verified listings)
- Career counseling services (referral partnerships)

**Non-Negotiables:**
- Never sell user data
- No interest-based revenue
- No haram advertising
- Transparent pricing
- Reinvest profits into platform improvement and charity

### Impact Goals (Year 1)

**Mizaan:**
- 10,000 active users
- £10 million in zakat accurately calculated
- 50% average reduction in wasteful spending among users
- Partnership with 10 mosques/Islamic centers

**Rizq:**
- 5,000 active users
- 1,000 halal opportunities aggregated
- 100 confirmed hires
- £5 million in halal income generated through platform

**Combined:**
- Recognized by major Islamic organizations
- Featured in Muslim media
- Open-source community of Muslim developers contributing
- Replicated in other languages/regions

---

## Barakah Measurement

### How Will I Know These Projects Are Pleasing to Allah?

**Spiritual Indicators:**
1. **Sincerity Check:** Am I building this for fame/money or to serve the ummah?
2. **User Transformation:** Are people's lives becoming more aligned with Islamic principles?
3. **Organic Growth:** Does the platform spread through genuine recommendation, not marketing manipulation?
4. **Community Ownership:** Do other Muslims contribute and feel ownership?

**Measurable Impact:**
1. **Financial Literacy:** Muslims understanding and applying Quranic economic principles
2. **Debt Reduction:** Families eliminating riba and achieving financial stability
3. **Employment:** Muslims finding dignified halal work, moving from dependency to self-reliance
4. **Zakat Accuracy:** Millions accurately calculated and distributed to those in need
5. **Generational Impact:** Parents teaching children Islamic spending values through the tool

**Long-term Legacy:**
1. **Sadaqah Jariyah:** Platform continues benefiting ummah after I'm gone
2. **Open Source:** Other developers build upon this foundation
3. **Normalization:** Islamic economic tools become expected, not exceptional
4. **Systemic Change:** Shift from Qarun culture to Quranic balance in Muslim communities

---

## Development Philosophy

**Every commit is ibadah when written with this intention:**
- Code comments include Quranic references
- Function names reflect Islamic concepts
- User messages incorporate hadith
- Testing ensures accuracy in religious obligations (zakat)
- Documentation serves as da'wah through excellent work

**"Indeed, Allah loves those who do their work with ihsan (excellence)." - Inspired by hadith**

---

**Last Updated:** 9 Oct 2025  
**Status:** Planning Phase - Ready to Begin Week 1 Foundation Building  
**Next Milestone:** Complete micro-projects by Day 14, begin Mizaan development Week 3