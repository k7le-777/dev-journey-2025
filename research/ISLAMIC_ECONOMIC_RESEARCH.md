# Islamic Economic Research Foundation

**Purpose:** This document compiles the Quranic and hadith foundation for Mizaan and Rizq, ensuring every feature is grounded in authentic Islamic scholarship.

**Last Updated:** 9 January 2025  
**Status:** Living document - expands as projects develop

---

## TABLE OF CONTENTS

1. [Balanced Spending - Mizaan Foundation](#part-1-balanced-spending)
2. [Zakat Calculation - Mizaan Foundation](#part-2-zakat-calculation)
3. [Earning and Provision - Rizq Foundation](#part-3-earning-and-provision)
4. [Dignity of Labor - Rizq Foundation](#part-4-dignity-of-labor)
5. [Halal Income Criteria - Rizq Foundation](#part-5-halal-income-criteria)
6. [Economic Justice Principles](#part-6-economic-justice)
7. [Contemporary Fiqh Applications](#part-7-contemporary-applications)
8. [Scholarly Resources](#part-8-resources)

---

## PART 1: BALANCED SPENDING (Mizaan Foundation)

### Primary Quranic Command

**Verse:** Surah Al-Furqan 25:67  
**Arabic:** وَالَّذِينَ إِذَآ أَنفَقُوا۟ لَمْ يُسْرِفُوا۟ وَلَمْ يَقْتُرُوا۟ وَكَانَ بَيْنَ ذَٰلِكَ قَوَامًا  
**Translation:** "And those who, when they spend, are neither extravagant nor niggardly, but hold a medium way between those extremes."

**Context:** This verse appears in Surah Al-Furqan describing the qualities of 'ibad ar-Rahman (servants of the Most Merciful). It was revealed in Makkah addressing both the pre-Islamic Arab tendency toward extravagance and extreme asceticism practiced by some religious groups.  
**Application to Mizaan:** This verse provides the core algorithm principle - measuring balance between excess (israf) and miserliness (qatr). The platform helps users find "qawaman" - the balanced middle path.  
**Implementation Logic:** 
def calculate_balance_score(expense, income, category):
    """
    Implements Quran 25:67's middle path principle
    Returns: 'balanced', 'excessive', or 'insufficient'
    """
    
    # Category-specific thresholds based on Islamic need hierarchy
    thresholds = {
        'food': {'min': 0.10, 'max': 0.25},  # 10-25% of income
        'housing': {'min': 0.20, 'max': 0.35},  # 20-35% of income
        'charity': {'min': 0.025, 'max': float('inf')},  # min 2.5% (zakat), no max
        'luxury': {'min': 0, 'max': 0.05}  # max 5% for non-essentials
    }
    
    ratio = expense / income
    threshold = thresholds.get(category)
    
    if ratio < threshold['min']:
        return 'qatr'  # Insufficiency (potential stinginess)
    elif ratio > threshold['max']:
        return 'israf'  # Excess
    else:
        return 'qawaman'  # Balance - Quranic ideal
        
    # Trigger verse reminder when imbalance detected
    if result != 'qawaman':
        show_ayah_reminder("Al-Furqan 25:67")

### Additional Quranic Verses on Spending

**Verse 2:Neither Tightly Closed nor Fully Extended:** Al-Isra 17:29  
Arabic:
وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ وَلَا تَبْسُطْهَا كُلَّ ٱلْبَسْطِ فَتَقْعُدَ مَلُومًا مَّحْسُورًا
**Translation(Sahih International):** "And do not make your hand [as] chained to your neck or extend it completely and [thereby] become blamed and insolvent."

**Context:** Revealed in Makkah during a period of economic hardship for Muslims. Some Companions were so generous they gave away everything, leaving themselves destitute. Others became miserly from fear of poverty. This verse addresses both extremes using powerful imagery. 
**Application to Mizaan:** 
- "Chained hand" (يَدَكَ مَغْلُولَةً) = hoarding, miserliness, refusing to spend even on necessities
- "Fully extended" (تَبْسُطْهَا كُلَّ ٱلْبَسْطِ) = uncontrolled spending, giving everything away
- Two negative outcomes mentioned: "blamed" (maluman -socially criticized) and "insolvent" (mahsuran - financially ruined)
**Implementation Logic:** 
def analyze_monthly_pattern(user_expenses, user_income):
    """
    Implements Quran 17:29's warning against both extremes
    Checks overall spending pattern across all categories
    """
    
    total_spent = sum(user_expenses.values())
    spending_ratio = total_spent / user_income
    
    # "Chained hand" detection (hoarding)
    if spending_ratio < 0.40:  # Spending less than 40% of income
        # Check if they're saving for valid reason (hajj, marriage, house)
        if not user.has_active_savings_goal:
            return {
                'status': 'chained_hand',
                'warning': 'You may be holding back excessively.',
                'ayah': 'Al-Isra 17:29',
                'guidance': 'Islam encourages circulation of wealth. Consider sadaqah or valid savings goals.'
            }
    
    # "Fully extended" detection (overspending)
    elif spending_ratio > 0.95:  # Spending more than 95% of income
        return {
            'status': 'fully_extended',
            'warning': 'You risk becoming "blamed and insolvent"',
            'ayah': 'Al-Isra 17:29',
            'guidance': 'Reduce non-essential spending. Build emergency fund (3-6 months expenses).'
        }
    
    else:
        return {'status': 'balanced', 'message': 'Your overall spending pattern reflects Quranic moderation.'}
**Edge Cases**
- High income earners: Someone earning £10,000/month spending £4,000 (40%) is not miserly - they're saving/investing. Don't flag unless savings have no purpose.
- Poverty situations: Someone earning £1,000/month spending £950 (95%) may have no choice. Check income level before warning.
- Temporary situations: Moving house, medical emergency, wedding. Allow users to mark months as "exceptional circumstances."


**Verse 3: Do Not Commit Excess** Al-An'am
Arabic:
وَكُلُوا۟ مِن ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ ۖ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ

**Translation(Sahih International):** "...And eat of its fruit when it ripens, but give [the due] charity on the day of its harvest. And do not commit excess. Indeed, He does not like those who commit excess."

**Context:** 
Revealed in Makkah regarding agricultural produce. Allah grants permission to enjoy the harvest but with two commands: (1) give the poor their due, (2) don't commit israf (excess). Classical scholars extended "israf" beyond food to all consumption.
**Application to Mizaan:** 
- Israf (إِسْرَاف) = excess, wastefulness, extravagance
- Applies to both quantity (too much) and quality (unnecessarily luxurious)
"He does not like" (لَا يُحِبُّ) is strong warning - Allah's displeasure
- Even halal things become haram when done excessively
**Implementation Logic:** 
def detect_israf(expense_item):
    """
    Implements Quran 6:141's prohibition of excess
    Flags specific transactions, not just overall spending
    """
    
    israf_indicators = {
        'luxury_brand': False,
        'impulse_buy': False,
        'duplicate_purchase': False,
        'excessive_quantity': False,
        'unnecessary_upgrade': False
    }
    
    # Luxury brand detection
    if expense_item.brand in LUXURY_BRANDS:
        israf_indicators['luxury_brand'] = True
        
    # Impulse buy detection (purchased within 24 hours of browsing)
    if expense_item.time_since_first_view < timedelta(hours=24):
        israf_indicators['impulse_buy'] = True
        
    # Duplicate purchase (already own similar item)
    similar_items = user.existing_items.filter(category=expense_item.category)
    if len(similar_items) > 3:  # e.g., 4th pair of shoes this month
        israf_indicators['duplicate_purchase'] = True
    
    # Excessive quantity (10 shirts when you own 30 already)
    if expense_item.quantity > reasonable_threshold(expense_item.category):
        israf_indicators['excessive_quantity'] = True
    
    if any(israf_indicators.values()):
        return {
            'is_israf': True,
            'indicators': israf_indicators,
            'ayah': 'Al-An\'am 6:141',
            'reminder': 'Allah does not like those who commit excess.',
            'suggestion': 'Consider if this purchase is needed or wasteful.'
        }
    
**Scholarly Notes**
- Imam Al-Ghazali: Defines israf as "spending on what's not needed" or "spending more than necessary on what is needed"
- Ibn Kathir: Explains this verse as Allah allowing enjoyment but forbidding wastefulness
- Modern application: Brand worship, fast fashion, impulse buying all fall under israf

**Verse 4: Satan Commands Immorality and Poverty** Al-Baqarah 2:268
Arabic:
وَكُلُوا۟ مِن ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ ۖ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ

**Translation(Sahih International):** 
"Satan threatens you with poverty and orders you to immorality, while Allah promises you forgiveness from Him and bounty. And Allah is all-Encompassing and Knowing."

**Context:** 
Revealed in Madinah regarding charity and spending. Some Muslims hesitated to give sadaqah, fearing they'd become poor. Shaytan exploits this fear to prevent both generosity and lawful earning. Allah promises His bounty is greater than any financial fear.
**Application to Mizaan:** 
- Addresses the psychological barrier to balanced spending: fear of poverty
- Two Satanic whispers: (1) "If you spend, you'll be poor" (2) "Be stingy/immoral with money"
- Allah's counter-promise: forgiveness + fadl (abundance/bounty)
- Encourages trust in Allah's provision (tawakkul)
**Implementation Logic:** 
def handle_charity_hesitation(user_profile):
    """
    Implements Quran 2:268's encouragement to spend in Allah's way
    Addresses psychological barriers to charitable giving
    """
    
    # Detect if user consistently avoids charity despite means
    if user_profile.charity_percentage < 0.01 and user_profile.income > poverty_line * 2:
        
        # Check income trend (has income been stable/growing?)
        if user_profile.income_trend in ['stable', 'growing']:
            return {
                'message': 'Consider increasing your sadaqah',
                'ayah': 'Al-Baqarah 2:268',
                'reflection': 'Satan threatens with poverty, but Allah promises bounty.',
                'suggested_action': 'Start with 1% additional charity this month',
                'barakah_tracking': 'Track how your provisions change when you give more'
            }
    
    # Positive reinforcement when user gives generously
    if user_profile.charity_percentage >= 0.05:  # 5% or more
        return {
            'affirmation': 'You are choosing Allah\'s promise over Shaytan\'s fear!',
            'ayah': 'Al-Baqarah 2:268',
            'dua': 'May Allah increase you in bounty and forgiveness.'
        }
    
**Psychological Apllication**
- This verse addresses scarcity mindset that prevents both earning and giving
- Users should see that Quranic economics is based on trust in Allah's abundance, not fear
- Feature suggestion: "Barakah Tracker" - users optionally record how provisions come after increased charity

**Verse 5: Do Not Squander Wastefully** Al-Isra 17:26-27
Arabic:
وَءَاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ وَلَا تُبَذِّرْ تَبْذِيرًا ﴿٢٦﴾ إِنَّ ٱلْمُبَذِّرِينَ كَانُوٓا۟ إِخْوَٰنَ ٱلشَّيَـٰطِينِ ۖ وَكَانَ ٱلشَّيْطَـٰنُ لِرَبِّهِۦ كَفُورًا ﴿٢٧﴾

**Translation(Sahih International):** 
"And give the relative his right, and [also] the poor and the traveler, and do not spend wastefully. Indeed, the wasteful are brothers of the devils, and ever has Satan been to his Lord ungrateful."

**Context:** 
Revealed in Makkah. After commanding generosity to relatives, poor, and travelers, Allah immediately forbids tabdhir (wasteful squandering). The severity is shown by calling wasteful people "brothers of devils" - one of the harshest descriptions in the Quran.
**Application to Mizaan:** 
- Tabdhir (تَبْذِير) = wasteful squandering, aimless spending
- Different from israf: tabdhir is spending on wrong things, israf is spending too much on right things
- "Brothers of devils" (إِخْوَٰنَ ٱلشَّيَـٰطِينِ) = extremely strong warning
- Contrast: give to the deserving (relatives, poor, travelers) but don't squander
**Implementation Logic:** 
def detect_tabdhir(expense_history):
    """
    Implements Quran 17:26-27's prohibition of wasteful squandering
    Tabdhir = aimless, purposeless spending on wrong things
    """
    
    tabdhir_patterns = []
    
    # Pattern 1: Spending on haram (gambling, alcohol, interest)
    haram_expenses = expense_history.filter(category__in=HARAM_CATEGORIES)
    if haram_expenses.exists():
        tabdhir_patterns.append({
            'type': 'haram_spending',
            'severity': 'CRITICAL',
            'message': 'Spending on prohibited items is tabdhir (wasteful squandering)',
            'ayah': 'Al-Isra 17:26-27'
        })
    
    # Pattern 2: Aimless spending (no clear purpose, frequent random purchases)
    random_purchases = expense_history.filter(
        category='miscellaneous',
        amount__lt=average_expense * 0.1  # small, frequent purchases
    ).count()
    
    if random_purchases > 20:  # More than 20 random purchases per month
        tabdhir_patterns.append({
            'type': 'aimless_spending',
            'severity': 'WARNING',
            'message': 'Many small, aimless purchases detected',
            'suggestion': 'Set clear intention before each purchase'
        })
    
    # Pattern 3: Neglecting obligations while spending on luxuries
    charity_ratio = expense_history.filter(category='charity').sum() / total_income
    luxury_ratio = expense_history.filter(category='luxury').sum() / total_income
    
    if charity_ratio < 0.025 and luxury_ratio > 0.10:
        tabdhir_patterns.append({
            'type': 'misplaced_priorities',
            'severity': 'WARNING',
            'message': 'Verse commands giving to relatives and poor before indulging',
            'ayah': 'Al-Isra 17:26',
            'suggestion': 'Fulfill obligations before luxuries'
        })
    
    return tabdhir_patterns
    
**Scholalarly Distinction (Important)**
- Israf (excess): Spending too much on permissible things (e.g., £500 on halal restaurant meal)
- Tabdhir (squandering): Spending on wrong/prohibited things OR aimless spending with no benefit
- Classical example: Buying a £1000 phone when you need the money for rent = tabdhir. Buying a £1000 phone when you're wealthy but already have 3 phones = israf.
**User-Facing Message**
- "Islam distinguishes your rights (family, poor) from luxuries. The Quran (17:26-27) commands fulfilling rights first, then enjoying blessings with gratitude - never squandering aimlessly. Review your priorities?" 

### Hadith on Balanced Spending

**Hadith 1: Every Person is a Shepherd:**  
**Full Text**
"Every one of you is a shepherd and is responsible for his flock. The leader of people is a guardian and is responsible for his subjects. A man is the guardian of his family and he is responsible for them. A woman is the guardian of her husband's home and his children and she is responsible for them. The servant of a man is a guardian of the property of his master and he is responsible for it. No doubt, every one of you is a shepherd and is responsible for his flock."
**Source**
Sahih al-Bukhari 893, Sahih Muslim 1829
**Authentication**
Sahih (Authentic) - Agreed upon by both Bukhari and Muslim (highest level)
Narrator: Abdullah ibn Umar (RA)
**Context**
The Prophet ﷺ delivered this in response to people asking about their responsibilities. The hadith establishes that everyone has a sphere of trust (amanah) for which they're accountable to Allah.
**Application to Mizaan**
- Your money is not absolutely yours - it's an amanah (trust) from Allah
- You are a "shepherd" (ra'in) of your wealth = responsible steward
- Will be questioned on Judgment Day: "How did you earn it? How did you spend it?" (see Hadith 2)
- Creates moral weight for every spending decision
**User-Facing Message Suggestion**
def welcome_message_islamic_frame():
    return {
        'greeting': 'Assalamu alaykum! Welcome to Mizaan.',
        'frame': 'Your wealth is an amanah (trust) from Allah.',
        'hadith': 'The Prophet ﷺ said: "Every one of you is a shepherd and responsible for his flock." (Bukhari & Muslim)',
        'implication': 'Mizaan helps you fulfill this responsibility through Quranic balance.',
        'call_to_action': 'Let\'s track your spending with Islamic awareness.'
    }



**Hadith 2: Two Questions About Wealth on Judgment Day**  
**Full Text**
"The feet of the son of Adam will not move on the Day of Resurrection until he is asked about five things: his life and how he spent it, his youth and how he used it, his wealth and how he earned it and how he spent it, and how he acted upon what he knew."
**Source**
Sunan al-Tirmidhi 2417
Authentication: Hasan (Good/Sound) - authenticated by Imam al-Tirmidhi and later scholars
Narrator: Abu Barzah al-Aslami (RA)
**Context**
The Prophet ﷺ listed five matters for which every person will be held accountable. Two directly concern wealth: earning and spending. This establishes accountability for economic behavior.
**Application to Mizaan**
- Question 1: "How did you earn it?" → Connects to Rizq project (halal income verification)
- Question 2: "How did you spend it?" → Core purpose of Mizaan (tracking spending with Islamic consciousness)
- Creates urgency: this isn't optional self-improvement, it's preparation for divine accountability
- Both earning AND spending matter - can't compensate one with the other
**Implementation Logic**
def generate_monthly_reflection(user_spending_data):
    """
    Creates end-of-month reflection based on Judgment Day questions
    Helps user prepare for accountability
    """
    
    return {
        'title': 'Monthly Accountability Reflection',
        'hadith': 'The Prophet ﷺ said you will be asked: "How did you spend your wealth?" (Tirmidhi)',
        'questions': [
            {
                'question': 'What percentage went to obligations (family, bills)?',
                'user_data': f"{user_spending_data.obligations_percentage}%"
            },
            {
                'question': 'What percentage went to charity and good causes?',
                'user_data': f"{user_spending_data.charity_percentage}%"
            },
            {
                'question': 'What percentage was wasteful (israf/tabdhir)?',
                'user_data': f"{user_spending_data.wasteful_percentage}%",
                'flagged_transactions': user_spending_data.wasteful_items[:5]
            },
            {
                'question': 'Did your spending reflect Quranic balance (25:67)?',
                'user_data': user_spending_data.balance_score
            }
        ],
        'action': 'Review flagged transactions and make tawbah for any wasteful spending.',
        'dua': 'O Allah, make my wealth a means of blessing, not a source of trial.'
    }
**User-Facing Message**
- "In Judgment Day accountability, Allah will ask about both earning and spending. Mizaan helps you prepare for this question while still living. Track with intention."




**Hadith 3: Blessing is in the Middle**  
**Full Text**
"The best of matters are those that are moderate (middle/balanced)."
**Source**
Al-Bayhaqi in Shu'ab al-Iman 5322
**Authentication**
Hasan (Good) - authenticated by multiple scholars including Al-Albani
Narrator: Anas ibn Malik (RA)
**Context**

A principle stated by the Prophet ﷺ that scholars apply across all aspects of Islam: worship, character, economics, relationships. Extremism in any direction moves away from prophetic way.
**Application to Mizaan**
- Directly supports the "Mizaan" (balance/scale) concept
- Neither extreme poverty (voluntary or involuntary) nor extreme wealth obsession is the goal
- "Middle" doesn't mean mathematical average - it means wise moderation contextual to circumstances
- Links to Quranic verses on balance (25:67, 17:29)
**Implementation Logic**
def calculate_balance_blessing_indicator(user_data):
    """
    Visual indicator showing how close user is to 'middle path'
    Based on hadith: "The best of matters are moderate"
    """
    
    balance_factors = {
        'spending_moderation': assess_spending_pattern(user_data),  # Not too tight, not too loose
        'charity_consistency': assess_charity_habit(user_data),  # Regular, not sporadic
        'debt_management': assess_debt_level(user_data),  # Manageable, not crushing
        'savings_wisdom': assess_savings_behavior(user_data),  # Prepared, not hoarding
        'luxury_restraint': assess_luxury_spending(user_data)  # Enjoyed, not obsessed
    }
    
    # Score each factor 0-100
    overall_balance = sum(balance_factors.values()) / len(balance_factors)
    
    if overall_balance >= 70:
        message = "Masha'Allah! Your financial pattern reflects prophetic moderation."
        hadith_ref = "The Prophet ﷺ said: 'The best of matters are moderate.' (Al-Bayhaqi)"
    elif overall_balance >= 40:
        message = "You're on the path to balance. Keep refining with Islamic awareness."
        suggestion = "Focus on improving: " + lowest_scoring_factors(balance_factors)
    else:
        message = "Your finances show imbalance. Let Quranic guidance help."
        action = "Review spending categories and adjust toward middle path."
    
    return {
        'balance_score': overall_balance,
        'message': message,
        'hadith': hadith_ref,
        'breakdown': balance_factors
    }

**Hadith 4: Wealth is a Good Thing for the Righteous**  
**Full Text**
"How excellent is righteous wealth for a righteous man!"
**Source**
Musnad Ahmad 17404, authenticated by Ahmad Shakir
**Authentication**
Sahih (Authentic) according to Ahmad Shakir and Al-Albani
**Narrator** 
Amr ibn al-'As (RA)
**Context**
This hadith counters the misconception that Islam views wealth negatively. The Prophet ﷺ clarifies that wealth itself is neutral - it becomes good or bad based on who possesses it and how they use it. The condition is "righteous wealth" (al-mal al-salih) for a "righteous person" (al-rajul al-salih).
**Application to Mizaan**
- Islam doesn't vilify wealth - it teaches responsibility with wealth
- "Righteous wealth" = earned through halal means, spent in balanced ways
- "Righteous person" = one who sees wealth as trust, not ultimate goal
- Mizaan's purpose: help users become "righteous people with righteous wealth"
**User-Facing Message**
def frame_wealth_positively():
    """
    Counter negative self-talk about having money
    Many Muslims feel guilty for comfort - this hadith corrects that
    """
    
    messages = {
        'high_income_user': {
            'frame': 'Wealth is not sinful. The Prophet ﷺ said: "How excellent is righteous wealth for a righteous person!" (Ahmad)',
            'challenge': 'Your responsibility is to earn it righteously and spend it with balance.',
            'action': 'Use your provision to benefit yourself, family, and ummah.'
        },
        'growing_wealth': {
            'affirmation': 'Masha\'Allah, your wealth is increasing!',
            'hadith': 'The Prophet ﷺ praised righteous wealth for righteous people.',
            'reminder': 'As Allah increases your provision, increase your charity proportionally.',
            'suggested_action': f"Consider raising charity from {current_charity}% to {suggested_charity}%"
        },
        'guilt_about_comfort': {
            'reframe': 'Allah's provision is a blessing, not a sin.',
            'hadith': 'The Prophet ﷺ: "How excellent is righteous wealth for a righteous person!"',
            'condition': 'The key is HOW you earned it and HOW you spend it.',
            'action': 'Ensure your income is halal and your spending is balanced. Then enjoy with gratitude.'
        }
    }
**Important Scholarly Note**
# This hadith is often misunderstood. It does NOT mean "money is always good." The conditions are:
- 1.Righteous wealth (mal salih) - halal sources, honest earnings
- 2.Righteous person (rajul salih) - someone who fulfills obligations, avoids extravagance, uses wealth for good
- The inverse is implied: unrighteous wealth or wealth in the hands of unrighteous person is a curse.

**Hadith 5: Seven Categories Shaded on Judgment Day**  
**Full Text(relevant portion)**
"Seven people will be shaded by Allah under His shade on the Day when there will be no shade except His... [including] a man who gives charity so secretly that his left hand does not know what his right hand has given..."
**Source**
Sahih al-Bukhari 660, Sahih Muslim 1031
**Context**
The Prophet ﷺ described seven categories of people who will receive special mercy on Judgment Day. One category is those who give charity with complete sincerity and secrecy, avoiding showing off (riya).
**Application to Mizaan**
- Charity tracking must protect privacy and prevent showing off
- "Left hand not knowing what right hand gave" = ultimate discretion
- Encourages regular, private charitable giving
- Creates technical requirement: charity data must be deeply private
**Implementation Logic (Critical for Ethcis)**
- class CharityPrivacyProtection:
    """
    Implements hadith: "Left hand doesn't know what right hand gave"
    Charity tracking must be maximally private to prevent riya (showing off)
    """
    
    def __init__(self):
        self.encryption_key = generate_user_specific_key()  # Only user can decrypt
    
    def log_charity(self, amount, recipient, date):
        """
        Encrypt charity details so even database admins can't see specifics
        """
        encrypted_entry = encrypt({
            'amount': amount,
            'recipient': recipient,
            'date': date,
            'note': 'May Allah accept and conceal this'
        }, self.encryption_key)
        
        # Only store encrypted version
        db.charity_log.insert(encrypted_entry)
        
        # Show user confirmation WITHOUT details
        return {
            'message': 'Charity recorded privately between you and Allah.',
            'hadith': 'The Prophet ﷺ praised those who give so secretly their left hand doesn\'t know what their right hand gave. (Bukhari & Muslim)',
            'dua': 'May Allah shade you under His throne on the Day of Judgment.'
        }
    
    def charity_summary(self, user):
        """
        Show aggregate only - never specific recipients/amounts in UI
        """
        decrypted_entries = decrypt_charity_log(user.charity_log, user.encryption_key)
        
        return {
            'total_this_year': sum(entry.amount for entry in decrypted_entries),
            'number_of_gifts': len(decrypted_entries),
            'average_gift': total / len(decrypted_entries),
            'message': 'Your charity is between you and Allah. We show only totals.',
            'no_leaderboards': True,  # NEVER create charity competition features
            'no_social_sharing': True  # NEVER allow "I gave £X" posts
        }
**Critical Design Principle**
- NO charity leaderboards (creates riya)
- NO social sharing of charity amounts (violates hadith spirit)
- NO public recognition (defeats the "left hand doesn't know" principle)
- Only show user their own aggregate statistics privately
- Encourage: "Give more privately than you give publicly"
**User Facing Reminder**
"The Prophet ﷺ said the most sincere charity is given so secretly even your left hand doesn't know. Mizaan protects your charity privacy - it's between you and Allah."


### Islamic Spending Categories Framework

**Daruriyyat (الضروريات) - Essentials**  
**Definition**
Necessities without which life cannot function or would face severe hardship. The five essential preservation areas (maqasid al-shariah):
1. Life (nafs)
2. Religion (din)
3. Intelellect (aql)
4. Lineage/Family (nasl)
5. Property (mal)
**Classical Scholars**
Imam Al-Shatibi in "Al-Muwafaqat" and Imam Al-Ghazali in "Al-Mustasfa"
**Examples in Modern Context**
DARURIYYAT_CATEGORIES = {
    'food': {
        'description': 'Basic nutrition to sustain life',
        'examples': [
            'Groceries for daily meals',
            'Essential ingredients (rice, bread, vegetables, protein)',
            'Basic halal meat',
            'Water and milk'
        ],
        'NOT_included': [
            'Restaurant meals (unless no kitchen access)',
            'Imported delicacies',
            'Luxury/gourmet foods'
        ],
        'reasonable_percentage': '10-20% of income'
    },
    
    'housing': {
        'description': 'Shelter providing safety and dignity',
        'examples': [
            'Rent or mortgage for modest home',
            'Basic utilities (water, electricity, heating)',
            'Essential repairs (broken heating, leaking roof)',
            'Home insurance'
        ],
        'NOT_included': [
            'Luxury apartment in premium area',
            'Aesthetic renovations',
            'Swimming pool, home cinema'
        ],
        'reasonable_percentage': '25-35% of income'
    },
    
    'clothing': {
        'description': 'Covering 'awrah and protection from elements',
        'examples': [
            'Basic modest clothing (jilbab, thobe, trousers, shirts)',
            'Seasonal clothing (winter coat, summer clothes)',
            'Work attire (if required for employment)',
            'Children\'s growing clothes'
        ],
        'NOT_included': [
            'Designer brands',
            'Excessive quantities (10th shirt when you have 20)',
            'Fashion-driven purchases'
        ],
        'reasonable_percentage': '3-7% of income'
    },
    
    'healthcare': {
        'description': 'Preservation of life and health',
        'examples': [
            'Doctor visits and treatments',
            'Necessary medications',
            'Health insurance',
            'Emergency medical care',
            'Mental health treatment (increasingly recognized)'
        ],
        'NOT_included': [
            'Purely cosmetic procedures',
            'Alternative medicine without evidence'
        ],
        'reasonable_percentage': '5-10% of income (varies by country healthcare system)'
    },
    
    'education': {
        'description': 'Preservation of intellect and ability to earn',
        'examples': [
            'School fees for children',
            'Islamic education for family',
            'Skills training for employment',
            'Literacy and basic numeracy'
        ],
        'NOT_included': [
            'Elite private schools when good state schools available',
            'Excessive extra-curriculars'
        ],
        'reasonable_percentage': '5-15% of income (if children in school)'
    },
    
    'transportation': {
        'description': 'Ability to reach work, essentials, and masjid',
        'examples': [
            'Public transport for work commute',
            'Modest car if no public transport',
            'Fuel for essential travel',
            'Car insurance and basic maintenance'
        ],
        'NOT_included': [
            'Luxury vehicles',
            'Unnecessary car upgrades',
            'Excessive taxi usage when public transport available'
        ],
        'reasonable_percentage': '10-15% of income'
    },
    
    'basic_communication': {
        'description': 'Staying connected for work/family/emergencies',
        'examples': [
            'Mobile phone with basic plan',
            'Internet access (increasingly essential for work/school)',
            'Basic laptop/computer for work or children\'s education'
        ],
        'NOT_included': [
            'Latest iPhone every year',
            'Multiple devices unnecessarily',
            'Excessive data plans for entertainment'
        ],
        'reasonable_percentage': '2-5% of income'
    },
        'religious_obligations': {
            'description': 'Fulfilling Islamic duties',
            'examples': [
                'Zakat (2.5% mandatory)',
                'Fidyah for missed fasts (if unable)',
                'Hajj savings (once in lifetime if able)',
                'Basic Islamic books/resources',
                'Masjid contributions for community services'
            ],
            'NOT_included': [
                'Excessive decorative Qurans (one functional copy is essential)',
                'Luxury umrah packages when basic suffices'
            ],
            'reasonable_percentage': 'Minimum 2.5% (zakat), more is encouraged'
        }
}
**Implementation Logic**  
def categorize_as_daruriyyat(expense):
    """
    Determine if expense qualifies as essential (daruriyyat)
    """
    
    # Essential food check
    if expense.category == 'food':
        if expense.location == 'grocery_store' and expense.amount < (user.income * 0.20):
            return True
        elif expense.location == 'restaurant' and user.has_no_kitchen:
            return True
        else:
            return False  # Restaurant meals generally hajiyyat or higher
    
    # Essential housing check
    if expense.category == 'housing':
        if expense.subcategory in ['rent', 'mortgage', 'utilities', 'essential_repairs']:
            # Check if housing cost is reasonable (not luxury)
            if expense.monthly_housing_total < (user.income * 0.35):
                return True
        return False
    
    # Essential clothing check
    if expense.category == 'clothing':
        if expense.brand not in LUXURY_BRANDS and expense.purpose == 'necessity':
            return True
        return False
    
    # Healthcare always essential if medically necessary
    if expense.category == 'healthcare':
        if expense.subcategory in ['doctor', 'medication', 'insurance', 'emergency']:
            return True
        elif expense.subcategory == 'cosmetic' and not expense.medically_necessary:
            return False
    
    # Default: if unsure, mark as hajiyyat (needed) not daruriyyat
    return False


**Hajiyyat (الحاجيات) - Needs** 
**Definition** 
Things that remove hardship and difficulty but are not strictly essential for survival. Life can continue without them, but with significant discomfort or reduced quality.
**Classical Framework:**
Imam Al-Shatibi describes hajiyyat as "that which is needed to remove difficulty, though its absence doesn't threaten the five essentials."
**Examples in Modern Context**
HAJIYYAT_CATEGORIES = {
    'improved_food': {
        'description': 'Better quality or variety beyond bare sustenance',
        'examples': [
            'Occasional restaurant meals (halal, modest)',
            'Variety in diet (fruits, different proteins)',
            'Higher quality ingredients for health',
            'Eating out for social/family bonding'
        ],
        'NOT_included': [
            'Fine dining regularly',
            'Imported luxuries',
            'Excessive takeaway'
        ],
        'reasonable_percentage': '5-10% beyond essential food budget'
    },
    
    'comfortable_housing': {
        'description': 'Home improvements for comfort, not survival',
        'examples': [
            'Comfortable furniture (sofa, beds)',
            'Adequate space per family member',
            'Decent neighborhood (safe, access to masjid)',
            'Basic appliances (washing machine, fridge)',
            'Air conditioning in hot climates',
            'Heating beyond minimum in cold climates'
        ],
        'NOT_included': [
            'Premium location for status',
            'Excessive rooms',
            'Luxury fixtures'
        ]
    },
    
    'quality_clothing': {
        'description': 'Well-made, decent clothing beyond bare minimum',
        'examples': [
            'Good quality modest clothing that lasts',
            'Professional attire for work',
            'Formal Islamic wear (thobe, abaya of good fabric)',
            'Comfortable shoes',
            'Seasonal appropriate clothing'
        ],
        'NOT_included': [
            'Designer labels for prestige',
            'Excessive wardrobe',
            'Fashion trends'
        ]
    },
    
    'transportation_comfort': {
        'description': 'Reliable, comfortable transport beyond bare minimum',
        'examples': [
            'Reliable used car (if public transport inadequate)',
            'Car with air conditioning (in hot climate)',
            'Safe vehicle for family',
            'Bike or scooter for convenience'
        ],
        'NOT_included': [
            'New car when used car suffices',
            'Luxury brands (BMW, Mercedes for status)',
            'Multiple cars for one person'
        ]
    },
    
    'halal_entertainment': {
        'description': 'Lawful recreation and family bonding',
        'examples': [
            'Family outings to park, beach',
            'Halal entertainment (Islamic lectures, nature trips)',
            'Sports and exercise facilities',
            'Books and educational materials beyond essentials',
            'Moderate travel (visiting family, umrah)'
        ],
        'NOT_included': [
            'Excessive streaming subscriptions',
            'Constant cinema visits',
            'Luxury holidays'
        ],
        'reasonable_percentage': '5-10% of income'
    },
    
    'communication_convenience': {
        'description': 'Better communication tools for ease',
        'examples': [
            'Smartphone with good features (not just basic)',
            'Family phone plan',
            'Computer for each family member who needs it',
            'Reliable internet speed for work/education'
        ],
        'NOT_included': [
            'Latest flagship phones',
            'Multiple devices per person',
            'Premium unlimited plans when basic suffices'
        ]
    },
    
    'gifts_and_social': {
        'description': 'Maintaining family ties and social bonds',
        'examples': [
            'Eid gifts for children',
            'Wedding gifts for family/friends (modest)',
            'Hosting guests (Islamic encouragement)',
            'Sadaqah beyond zakat',
            'Contributing to community events'
        ],
        'NOT_included': [
            'Extravagant wedding gifts to impress',
            'Keeping up with others\' gift standards',
            'Hosting beyond means'
        ],
        'reasonable_percentage': '3-8% of income'
    }
}

**Implementation Logic**
def categorize_as_hajiyyat(expense):
    """
    Expenses that remove hardship but aren't strictly essential
    """
    
    # Food beyond basic sustenance
    if expense.category == 'food':
        if expense.location == 'restaurant' and expense.frequency < 8 per month:  # Occasional, not excessive
            if expense.amount < (user.income * 0.01):  # Modest spending
                return True
    
    # Comfortable but not luxury housing
    if expense.category == 'housing':
        if expense.subcategory in ['furniture', 'appliances', 'comfort_upgrades']:
            if expense.total_housing_percent < 0.40:  # Still reasonable portion of income
                return True
    
    # Quality clothing without brand obsession
    if expense.category == 'clothing':
        if expense.quality_tier == 'good' and expense.brand not in LUXURY_BRANDS:
            if expense.purpose in ['professional', 'durability', 'comfort']:
                return True
    
    # Halal entertainment in moderation
    if expense.category == 'entertainment':
        if expense.is_halal and expense.monthly_entertainment_total < (user.income * 0.10):
            return True
    
    # Social obligations and gifts
    if expense.category == 'gifts':
        if expense.amount < (user.income * 0.02) and expense.purpose in ['eid', 'wedding', 'family_tie']:
            return True
    
    return False

**Tahsiniyyat (التحسينات) - Improvements/Embellishments**  
**Definition**
Things that beautify life, enhance dignity, and add refinement but are neither essential nor needed. They represent excellence (ihsan) and enjoyment of Allah's blessings with gratitude.
**Quranic Basis**
"Say, 'Who has forbidden the adornment of Allah which He has produced for His servants and the good [lawful] things of provision?'" (Quran 7:32)
Allah permits enjoyment of good things, but with conditions:

- Must be halal
- After fulfilling obligations
- Without extravagance (israf)
- With gratitude, not arrogance
**Examples**
TAHSINIYYAT_CATEGORIES = {
    'aesthetic_improvements': {
        'description': 'Beautifying one\'s life while staying within balance',
        'examples': [
            'Decorating home tastefully',
            'Quality furniture for aesthetic pleasure',
            'Art, calligraphy (halal)',
            'Garden or plants',
            'Nice scent/perfume (encouraged in Islam)'
        ],
        'conditions': [
            'After daruriyyat and hajiyyat met',
            'Within overall balanced spending',
            'Not for showing off (riya)',
            'With gratitude to Allah'
        ],
        'reasonable_percentage': '2-5% of income'
    },
    
    'higher_quality_experiences': {
        'description': 'Elevated experiences beyond necessary comfort',
        'examples': [
            'Nicer restaurant for special occasions',
            'Quality umrah package (comfortable, not luxury)',
            'Educational travel',
            'Premium halal food items (organic, artisan)',
            'High-quality Islamic books and resources'
        ],
        'conditions': [
            'Occasional, not regular',
            'Doesn\'t create debt',
            'Proportionate to income'
        ]
    },
    
    'refined_clothing': {
        'description': 'Well-made, beautiful clothing without brand worship',
        'examples': [
            'Tailored modest clothing',
            'Fine fabrics (silk for women, quality cotton)',
            'Beautiful hijabs or thobes',
            'Handcrafted items'
        ],
        'NOT_allowed': [
            'Clothing for pride or showing off',
            'Luxury brands worn for status',
            'Excessive quantities'
        ],
        'hadith': 'The Prophet ﷺ said: "Allah is beautiful and loves beauty, but He hates arrogance." (Muslim)'
    },
    
    'charitable_excellence': {
        'description': 'Giving beyond obligations beautifully',
        'examples': [
            'Sadaqah beyond zakat (encouraged)',
            'Sponsoring orphans',
            'Building wells, masjids',
            'Supporting Islamic education',
            'Helping family members in need'
        ],
        'note': 'This is the BEST form of tahsiniyyat - beautifying life through generosity'
    },
    
    'personal_development': {
        'description': 'Investing in growth and skills beyond necessities',
        'examples': [
            'Advanced Islamic studies courses',
            'Professional skill development',
            'Learning Arabic',
            'Fitness and wellness (halal)',
            'Books and seminars'
        ]
    }
}
**Critical Distinctions**
# Tahsiniyyat (Allowed)
- Beautiful modest clothing
- Comfortable umrah trip
- Nice halal restaurant occasionally
- Quality home decor
- Generous charity
# Israf (Forbidden)
- Designer brand for status
- 5-star luxury umrah
- Fine dining regularly
- Mansion for prestige
- No charity, all self
**Implementation Logic**
def categorize_as_tahsiniyyat(expense, user_obligations_met):
    """
    Embellishments allowed ONLY if obligations met and within balance
    """
    
    # PRE-CONDITION: Check obligations met
    if not user_obligations_met:
        return {
            'is_tahsiniyyat': False,
            'reason': 'Tahsiniyyat not allowed when obligations (daruriyyat/hajiyyat/charity) unmet',
            'guidance': 'Quran 17:26 commands giving to relatives and poor BEFORE indulging'
        }
    
    # Aesthetic home improvements
    if expense.category == 'home_decor':
        if expense.total_tahsiniyyat_this_month < (user.income * 0.05):
            return {
                'is_tahsiniyyat': True,
                'note': 'Beautifying home is permissible with gratitude',
                'reminder': 'Say Alhamdulillah for Allah\'s blessings'
            }
    
    # Special experiences
    if expense.category == 'dining' and expense.price_tier == 'upscale':
        if expense.frequency < 2 per month and expense.purpose == 'special_occasion':
            return {'is_tahsiniyyat': True}
    
    # Quality religious items
    if expense.category == 'islamic_goods':
        if expense.quality == 'high' and expense.purpose in ['learning', 'worship']:
            return {
                'is_tahsiniyyat': True,
                'note': 'Investing in quality Islamic education is praiseworthy'
            }
    
    # Generous charity (best tahsiniyyat)
    if expense.category == 'charity' and expense.amount > (user.income * 0.025):
        return {
            'is_tahsiniyyat': True,
            'excellence': 'This is the highest form of tahsiniyyat!',
            'hadith': 'The Prophet ﷺ was most generous. (Bukhari)'
        }
    
    return {'is_tahsiniyyat': False}

**Israf (الإسراف) - Wastefulness/Excess**  
**Definition**
Extravagance, excess, and wastefulness - spending beyond reasonable limits or on wrong things. This is explicitly forbidden in multiple Quranic verses.
**Quranic Prohibtions**
"...and do not commit excess. Indeed, He does not like those who commit excess." (Quran 6:141)
"Indeed, the wasteful are brothers of the devils..." (Quran 17:27)
"And [they are] those who, when they spend, do not do so excessively..." (Quran 25:67)
**Classical Definitions**
Spending on what is not needed, OR
Spending more than necessary on what IS needed"

Ibn Abbas (RA): "Eat what you wish and wear what you wish, as long as two things are avoided: extravagance (israf) and pride (makhila)."
**Modern Manifestations(Quran Culture)**
ISRAF_INDICATORS = {
    'luxury_brand_obsession': {
        'description': 'Buying brands for status, not function',
        'examples': [
            '£2,000 handbag when £50 one functions equally',
            'Designer logo clothing for prestige',
            'Luxury car purely for status',
            'Brand-name everything for children'
        ],
        'quranic_connection': 'Story of Qarun (28:76-81) - wealth became source of pride',
        'severity': 'HIGH'
    },
    
    'impulse_buying': {
        'description': 'Purchasing without thought or need',
        'examples': [
            'Black Friday shopping sprees',
            'Online shopping when bored',
            'Buying duplicates of what you own',
            'One-click purchasing without consideration'
        ],
        'hadith': 'The Prophet ﷺ said: "Richness is not having many possessions, but richness is being content." (Bukhari)',
        'severity': 'MEDIUM'
    },
    
    'fast_fashion': {
        'description': 'Constant clothing purchases following trends',
        'examples': [
            'Buying new clothes every season',
            'Wardrobe of 100+ items barely worn',
            'Discarding functional clothing for "style"',
            'Children\'s clothes for appearance, not need'
        ],
        'environmental_note': 'Islam emphasizes not wasting resources',
        'severity': 'MEDIUM'
    },
    
    'food_waste': {
        'description': 'Wasting food through excess or disposal',
        'examples': [
            'Ordering more food than can be eaten',
            'Throwing away edible food regularly',
            'Buffet overfilling plates',
            'Excessive grocery shopping leading to waste'
        ],
        'hadith': 'The Prophet ﷺ never criticized food. (Bukhari) - Implication: food is sacred, don\'t waste',
        'severity': 'HIGH'
    },
    
    'social_media_influence': {
        'description': 'Spending to match online influencers',
        'examples': [
            'Buying products because influencer promoted',
            'Keeping up with "modest fashion" trends expensively',
            'Upgrading devices to match social circle',
            'Lifestyle inflation driven by Instagram'
        ],
        'modern_qarun': 'Qarun displayed wealth publicly (28:79) - modern equivalent is social media showing off',
        'severity': 'HIGH'
    },
    
    'subscription_accumulation': {
        'description': 'Multiple overlapping subscriptions unused',
        'examples': [
            '5 streaming services barely watched',
            'Gym membership never used',
            'Software subscriptions forgotten',
            'Magazine/app subscriptions unread'
        ],
        'note': 'Waste through negligence',
        'severity': 'LOW to MEDIUM'
    },
    
    'upgrade_obsession': {
        'description': 'Replacing functional items unnecessarily',
        'examples': [
            'New phone every year when current works',
            'New car every 2-3 years',
            'Furniture replacement for style, not function',
            'Gadget accumulation (3 tablets, 2 laptops for one person)'
        ],
        'severity': 'MEDIUM to HIGH'
    },
    
    'wedding_extravagance': {
        'description': 'Excessive wedding spending',
        'examples': [
            '£50,000+ wedding when couple has no savings',
            'Showing off to guests',
            'Elaborate decor and wasteful food',
            'Going into debt for wedding'
        ],
        'hadith': 'The Prophet ﷺ said: "The best wedding is that upon which the least expense is incurred." (Bayhaqi)',
        'cultural_pressure': 'Many Muslims face family pressure - but Quran supersedes culture',
        'severity': 'VERY HIGH'
    }
}
**Implementation - Israf Detection Algorithm**
class IsrafDetector:
    """
    Sophisticated detection of wasteful spending patterns
    """
    
    def analyze_expense(self, expense, user_context):
        """
        Multi-factor analysis to detect israf
        """
        
        flags = []
        severity = 'LOW'
        
        # Factor 1: Luxury brand when alternatives exist
        if expense.brand in LUXURY_BRANDS:
            cheaper_alternative = find_functional_equivalent(expense.item)
            price_difference = expense.amount - cheaper_alternative.price
            
            if price_difference > (user_context.daily_income):
                flags.append({
                    'type': 'luxury_brand',
                    'message': f'You paid £{price_difference} extra for brand name.',
                    'question': 'Did the brand add function, or just status?',
                    'ayah': 'Al-An\'am 6:141 - Allah does not like those who commit excess'
                })
                severity = 'HIGH'
        
        # Factor 2: Impulse buying (purchased within 24 hours of first view)
        if expense.time_since_first_consideration < timedelta(hours=24):
            if expense.amount > (user_context.income * 0.01):
                flags.append({
                    'type': 'impulse',
                    'message': 'This appears to be an impulse purchase.',
                    'guidance': 'The Prophet ﷺ encouraged thoughtfulness. Wait 24-48 hours before large purchases.',
                    'action': 'Implement "48-hour rule" for purchases over £50'
                })
                severity = max(severity, 'MEDIUM')
        
        # Factor 3: Duplicate/unnecessary purchase
        similar_items = user_context.existing_items.filter(category=expense.category)
        if len(similar_items) > 5:
            flags.append({
                'type': 'duplicate',
                'message': f'You already own {len(similar_items)} items in this category.',
                'question': 'Do you truly need another?',
                'hadith': 'Richness is contentment, not possessions. (Bukhari)'
            })
            severity = max(severity, 'MEDIUM')
        
        # Factor 4: Disproportionate to income
        if expense.amount > (user_context.weekly_income):
            if expense.category not in ['housing', 'healthcare', 'essential']:
                flags.append({
                    'type': 'disproportionate',
                    'message': f'This expense is more than your weekly income.',
                    'concern': 'Israf can be spending appropriately earned money inappropriately.',
                    'guidance': 'Consider if this reflects Quranic balance (25:67)'
                })
                severity = max(severity, 'HIGH')
        
        # Factor 5: Neglecting obligations while indulging
        if user_context.charity_percentage < 0.025:  # Below zakat minimum
            if expense.category in ['luxury', 'entertainment', 'fashion']:
                flags.append({
                    'type': 'misplaced_priorities',
                    'message': 'You\'re spending on luxuries while neglecting zakat.',
                    'ayah': 'Quran 17:26 - Give relatives/poor their due BEFORE indulging',
                    'severity': 'CRITICAL',
                    'action': 'Fulfill obligations before luxuries'
                })
                severity = 'CRITICAL'
        
        # Factor 6: Wasteful food spending
        if expense.category == 'food':
            if expense.location == 'restaurant':
                monthly_restaurant_expenses = calculate_monthly_total(user_context, 'restaurant')
                if monthly_restaurant_expenses > (user_context.income * 0.15):
                    flags.append({
                        'type': 'excessive_dining_out',
                        'message': f'You\'ve spent £{monthly_restaurant_expenses} on restaurants this month.',
                        'percentage': f'{(monthly_restaurant_expenses/user_context.income)*100:.1f}% of income',
                        'guidance': 'Home cooking is both economical and often healthier'
                    })
                    severity = max(severity, 'MEDIUM')
        
        # Generate response
        if flags:
            return {
                'is_israf': True,
                'severity': severity,
                'flags': flags,
                'overall_message': self.generate_message(severity),
                'suggested_actions': self.suggest_corrections(flags, user_context)
            }
        else:
            return {'is_israf': False}
    
    def generate_message(self, severity):
        """
        Appropriate message based on severity
        """
        messages = {
            'LOW': {
                'tone': 'gentle reminder',
                'message': 'Consider if this purchase reflects Quranic moderation.'
            },
            'MEDIUM': {
                'tone': 'concern',
                'message': 'This spending pattern shows signs of excess (israf).',
                'action': 'Review your priorities and spending habits.'
            },
            'HIGH': {
                'tone': 'serious warning',
                'message': 'This is potentially wasteful spending that Allah dislikes.',
                'ayah': 'Quran 6:141 - "He does not like those who commit excess."',
                'action': 'Make tawbah and adjust your spending.'
            },
            'CRITICAL': {
                'tone': 'urgent',
                'message': 'You are indulging while neglecting Islamic obligations.',
                'ayah': 'Quran 17:26-27 - Give to deserving before indulging, or you become "brother of devils"',
                'action': 'IMMEDIATELY fulfill obligations (zakat, family support) before any luxury spending.'
            }
        }
        return messages.get(severity)

**Complete Category Decision Tree**
def categorize_expense_islamically(expense, user_context):
    """
    Master function: Categorize expense into Islamic framework
    Returns: daruriyyat, hajiyyat, tahsiniyyat, or israf
    """
    
    # FIRST: Check for israf (excess/waste)
    # This overrides all other categories
    israf_check = IsrafDetector().analyze_expense(expense, user_context)
    if israf_check['is_israf'] and israf_check['severity'] in ['HIGH', 'CRITICAL']:
        return {
            'category': 'israf',
            'subcategory': israf_check['flags'][0]['type'],
            'severity': israf_check['severity'],
            'message': israf_check['overall_message'],
            'quranic_warning': True,
            'needs_review': True
        }
    
    # SECOND: Check if daruriyyat (essential)
    if categorize_as_daruriyyat(expense):
        return {
            'category': 'daruriyyat',
            'message': 'Essential spending - necessary for life',
            'icon': '🛡️',
            'color': 'green',
            'priority': 1
        }
    
    # THIRD: Check if hajiyyat (needed for comfort)
    if categorize_as_hajiyyat(expense):
        return {
            'category': 'hajiyyat',
            'message': 'Needed for comfort - removes hardship',
            'icon': '✅',
            'color': 'blue',
            'priority': 2
        }
    
    # FOURTH: Check if tahsiniyyat (permissible improvement)
    # But ONLY if obligations met
    obligations_met = check_obligations_fulfilled(user_context)
    
    if categorize_as_tahsiniyyat(expense, obligations_met)['is_tahsiniyyat']:
        return {
            'category': 'tahsiniyyat',
            'message': 'Permissible embellishment - enjoy with gratitude',
            'icon': '🌟',
            'color': 'yellow',
            'priority': 3,
            'reminder': 'Say Alhamdulillah for Allah\'s blessings'
        }
    
    # FIFTH: If tahsiniyyat attempted but obligations NOT met
    if not obligations_met:
        return {
            'category': 'misplaced_tahsiniyyat',
            'warning': 'You are spending on improvements while obligations unmet',
            'ayah': 'Quran 17:26 - Give to relatives and poor BEFORE indulging',
            'action': 'Fulfill daruriyyat, hajiyyat, and charity obligations first',
            'severity': 'MEDIUM'
        }
    
    # DEFAULT: Unclear - ask user to clarify
    return {
        'category': 'uncategorized',
        'message': 'Please categorize this expense',
        'options': ['Essential', 'Needed', 'Improvement', 'Wasteful']
    }

**User Interface - Category Visualization**
def monthly_spending_breakdown_islamic(user):
    """
    Visual breakdown of spending by Islamic categories
    """
    
    expenses = user.expenses_this_month
    categorized = [categorize_expense_islamically(exp, user) for exp in expenses]
    
    # Calculate totals by category
    daruriyyat_total = sum([e.amount for e in categorized if e['category'] == 'daruriyyat'])
    hajiyyat_total = sum([e.amount for e in categorized if e['category'] == 'hajiyyat'])
    tahsiniyyat_total = sum([e.amount for e in categorized if e['category'] == 'tahsiniyyat'])
    israf_total = sum([e.amount for e in categorized if e['category'] == 'israf'])
    
    total_spending = sum([daruriyyat_total, hajiyyat_total, tahsiniyyat_total, israf_total])
    
    return {
        'title': 'Your Spending Through Islamic Lens',
        'hadith': 'The Prophet ﷺ said: "The best of matters are moderate." (Bayhaqi)',
        
        'breakdown': {
            'daruriyyat': {
                'amount': f'£{daruriyyat_total:,.2f}',
                'percentage': f'{(daruriyyat_total/total_spending)*100:.1f}%',
                'status': 'Essential - Well spent',
                'color': 'green',
                'icon': '🛡️'
            },
            'hajiyyat': {
                'amount': f'£{hajiyyat_total:,.2f}',
                'percentage': f'{(hajiyyat_total/total_spending)*100:.1f}%',
                'status': 'Needed - Removes hardship',
                'color': 'blue',
                'icon': '✅'
            },
            'tahsiniyyat': {
                'amount': f'£{tahsiniyyat_total:,.2f}',
                'percentage': f'{(tahsiniyyat_total/total_spending)*100:.1f}%',
                'status': 'Improvement - Enjoy with gratitude',
                'color': 'yellow',
                'icon': '🌟'
            },
            'israf': {
                'amount': f'£{israf_total:,.2f}',
                'percentage': f'{(israf_total/total_spending)*100:.1f}%',
                'status': '⚠️ WASTEFUL - Review & reduce',
                'color': 'red',
                'icon': '🚫',
                'action': 'Click to see wasteful transactions'
            }
        },
        
        'balance_score': calculate_balance_score(daruriyyat_total, hajiyyat_total, tahsiniyyat_total, israf_total),
        
        'guidance': generate_monthly_guidance(categorized),
        
        'quranic_reflection': 'Are you spending in the middle way (25:67)?'
    }


---

## PART 2: ZAKAT CALCULATION (Mizaan Foundation)

### Quranic Obligation

**Primary Verses:**  
**Verse 1: Walk Among Its Slopes (Al-Mulk 67:15):**  
Arabic:
هُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ ذَلُولًا فَٱمْشُوا۟ فِى مَنَاكِبِهَا وَكُلُوا۟ مِن رِّزْقِهِۦ ۖ وَإِلَيْهِ ٱلنُّشُورُ
**Context**  
Revealed in Makkah, this verse emphasizes Allah's bounty in making the earth accessible for human enterprise. The command to "walk" (imshū) is active - not passive waiting. "Manakib" (slopes/sides) suggests exploring different paths and opportunities.
**Application to Rizq Platform**  
- Active seeking encouraged: "Walk" = take initiative in earning
- Earth made tame (dhallūlan): Allah removed obstacles, but humans must effort
- "Eat of His provision": Earning is how we access Allah's rizq
- Resurrection reminder: Accountability for HOW we earned
**Key Insight for Platform**  
This verse counters the misunderstanding that "tawakkul" (trust in Allah) means passive waiting. True tawakkul is:

1. Making effort (walking the earth)
2. Trusting Allah for results
3. Recognizing all provision ultimately comes from Him
**Implementation Suggestion**  
def rizq_platform_welcome_message():
    """
    Frame job seeking as Islamic act of obedience
    """
    return {
        'greeting': 'Assalamu alaykum! Welcome to Rizq.',
        'quranic_frame': 'Allah commands: "Walk among the earth\'s slopes and eat of His provision." (67:15)',
        'reframe': {
            'from': 'Job hunting is stressful, secular activity',
            'to': 'Seeking halal income is worship - you are obeying Allah\'s command to "walk the earth"'
        },
        'mission': 'Rizq helps you obey this command by connecting you with verified halal opportunities.',
        'tawakkul_reminder': 'Make effort, then trust Allah for results. Both are required.',
        'dua': 'O Allah, make my seeking easy and my provision blessed.'
    }
**User-Facing Motivation**  
"When you search for halal income on Rizq, you're not just job hunting - you're literally obeying Quran 67:15. Allah commanded you to walk the earth seeking His provision. Every application you submit is an act of worship when done with Islamic intention."
 

### Nisab Thresholds

**Gold Nisab:**  
- Weight: 85 grams
- Current Price: £[Research will provide]
- Threshold in GBP: £[Calculate: 85 × price]
- Source: [API source from research]
- Last Updated: 9 January 2025

**Silver Nisab:**  
- Weight: 595 grams
- Current Price: £[Research will provide]
- Threshold in GBP: £[Calculate: 595 × price]
- Source: [API source from research]
- Last Updated: 9 January 2025

**Scholarly Recommendation:**  
[Which nisab to use and why - from research]

### Zakatable Assets

**What Counts:**  
[Will populate with research - cash, savings, gold, silver, business inventory, etc.]

**What Doesn't Count:**  
[Will populate with research - personal use items, primary residence, etc.]

### Calculation Methodology

**Rate:** 2.5% (one-fortieth)  
**Evidence:** [Hadith sources from research]

**Lunar Year Requirement (Hawl):**  
[Explanation from research - why lunar year, how to track]

**Implementation in Code:**
```python
# Pseudocode structure (will refine with research guidance)
def calculate_zakat(zakatable_wealth, nisab_threshold):
    """
    Calculate zakat due based on Islamic principles.
    
    Args:
        zakatable_wealth: Total eligible wealth (cash, savings, gold, etc.)
        nisab_threshold: Current nisab (85g gold or 595g silver equivalent)
    
    Returns:
        Zakat due amount (2.5% if above nisab, 0 if below)
    """
    if zakatable_wealth >= nisab_threshold:
        return zakatable_wealth * 0.025
    return 0
```

---

## PART 3: EARNING AND PROVISION (Rizq Foundation)

### Quranic Command to Seek Provision

**Verse 1:** Surah Al-Mulk 67:15  
**Translation:** "It is He who made the earth tame for you - so walk among its slopes and eat of His provision..."  
**Application:** [From research]

**Verse 2:** Al-Jumu'a 62:10
Arabic:
فَإِذَا قُضِيَتِ ٱلصَّلَوٰةُ فَٱنتَشِرُوا۟ فِى ٱلْأَرْضِ وَٱبْتَغُوا۟ مِن فَضْلِ ٱللَّهِ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًا لَّعَلَّكُمْ تُفْلِحُونَ
**Translation:** 
"And when the prayer has been concluded, disperse within the land and seek from the bounty of Allah, and remember Allah often that you may succeed."
**Context:**
Revealed in Madinah regarding Jumu'ah (Friday prayer). After obligatory congregational prayer, Muslims are commanded - not just permitted - to return to their work and business. This verse establishes that seeking livelihood is part of a complete Islamic life, not separate from worship.
**Application:**
- Command to seek bounty: "Ibtaghū" (ابْتَغُوا) = actively pursue
- After prayer, return to work: Islam integrates worship and work
- "Fadl Allah" (فَضْلِ ٱللَّهِ): Bounty/surplus - suggests Allah wants you to earn MORE than bare minimum
- Remember Allah while working: Dhikr during work makes it worship
**Scholarly Commentary:**
- Imam Al-Qurtubi: "This verse proves that seeking livelihood after fulfilling religious obligations is not only permissible but commanded. It refutes those who claim that complete devotion means abandoning work."
- Ibn Kathir: "Allah commanded dispersing through the land for trade and business after Jumu'ah, showing that work is part of Islamic life, not contradictory to it."
**Implemetation Logic:**
def integrate_work_and_worship(user_job_search):
    """
    Help users see work as part of complete Islamic life
    """
    
    return {
        'quranic_principle': 'After prayer, Allah commands: "Disperse and seek bounty" (62:10)',
        
        'reframe_work': {
            'misconception': 'Work is "dunya" (worldly), separate from deen (religion)',
            'truth': 'Quran 62:10 commands work AFTER prayer - they\'re connected, not opposed',
            'implication': 'Your 9-5 job can be worship if: (1) Income is halal, (2) Done with good intention, (3) You remember Allah during work'
        },
        
        'daily_intention': {
            'morning_dua': 'Before leaving for work, say: "O Allah, I seek Your bounty as You commanded. Make my work pleasing to You and my income blessed."',
            'during_work': 'Remember Allah throughout the day (tasbih, brief dua)',
            'end_of_day': 'Thank Allah for provision: "Alhamdulillah for today\'s rizq"'
        },
        
        'job_search_as_ibadah': {
            'message': 'Every job application is obedience to Quran 62:10',
            'encouragement': 'Allah commanded you to seek His bounty. You\'re doing exactly that.',
            'tawakkul': 'Apply, then trust Allah. Results are His to give.'
        }
    }
**Feature Idea: "Dhikr During Work" Reminders:**
def work_hour_dhikr_reminders(user):
    """
    Send gentle dhikr reminders during work hours
    Implements "remember Allah often" from 62:10
    """
    
    if user.is_work_hours:
        reminders = [
            {
                'time': '10:00 AM',
                'dhikr': 'SubhanAllah (Glory be to Allah)',
                'note': 'Brief remembrance while working = obedience to Quran 62:10'
            },
            {
                'time': '2:00 PM',
                'dhikr': 'Alhamdulillah (Praise be to Allah)',
                'note': 'Thank Allah for provision of work'
            },
            {
                'time': '4:00 PM',
                'dhikr': 'Allahu Akbar (Allah is Greatest)',
                'note': 'Your work is worship when you remember Him'
            }
        ]
        
        return {
            'feature': 'Dhikr During Work',
            'quranic_basis': 'Quran 62:10 - "Remember Allah often while seeking His bounty"',
            'reminders': reminders,
            'toggle': 'user can enable/disable',
            'frequency': 'customizable (every hour, twice daily, etc.)'
        }
**Translation:**
**Translation:**

**Verse 3:** An-Nisa 4:32
 Arabic:
وَلَا تَتَمَنَّوْا۟ مَا فَضَّلَ ٱللَّهُ بِهِۦ بَعْضَكُمْ عَلَىٰ بَعْضٍ ۚ لِّلرِّجَالِ نَصِيبٌ مِّمَّا ٱكْتَسَبُوا۟ ۖ وَلِلنِّسَآءِ نَصِيبٌ مِّمَّا ٱكْتَسَبْنَ ۚ وَسْـَٔلُوا۟ ٱللَّهَ مِن فَضْلِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ بِكُلِّ شَىْءٍ عَلِيمًا
**Translation:**
"And do not wish for that by which Allah has made some of you exceed others. For men is a share of what they have earned, and for women is a share of what they have earned. And ask Allah of His bounty. Indeed Allah is ever, of all things, Knowing."
**Context:**
Context:
Revealed in Madinah addressing envy and comparison. Some people wished for what others had (wealth, status, talents). Allah redirects focus: don't envy others, ask Allah for YOUR provision, and work for it ("what they have earned" - iktasabū).
**Application:**
Prohibition of envy: Don't compare your income/job to others
Men and women both earn: "For women a share of what they earned" - establishes women's right to work and earn
Individual provision paths: Each person has their own rizq journey
"Ask Allah of His bounty": Make dua AND work (the verse says "earned")
**Critical Modern Application:**
- Problem: Social media creates CONSTANT comparison:
1. "My friend earns £80k, I only earn £35k"
2. "Everyone on LinkedIn seems more successful"
3. "Why is my job search taking so long while others get offers quickly?"

- Quranic Solution (4:32):
1. Stop comparing - "Do not wish for what Allah gave others"
2. Focus on your effort - "For men/women a share of what THEY EARNED"
3. Make dua for your own provision - "Ask Allah of His bounty"
4. Trust Allah's timing - "Allah is Knowing" (of what's best for you)
**Implementation Logic:**
class ComparisonDetoxFeature:
    """
    Help users avoid destructive comparison culture
    Implements Quran 4:32's guidance
    """
    
    def __init__(self, user):
        self.user = user
    
    def detect_comparison_anxiety(self):
        """
        Identify when user is falling into comparison trap
        """
        
        indicators = []
        
        # User constantly checking others' salaries
        if self.user.salary_comparison_searches > 10 per month:
            indicators.append('excessive_salary_comparison')
        
        # User discouraged by job search duration
        if self.user.applications_sent > 50 and self.user.offers_received == 0:
            if self.user.mood_indicators == 'discouraged':
                indicators.append('prolonged_job_search_discouragement')
        
        # User comparing their role to peers
        if self.user.linkedin_browsing_time > timedelta(hours=2) per day:
            indicators.append('social_media_comparison')
        
        if indicators:
            return {
                'comparison_anxiety_detected': True,
                'indicators': indicators,
                'intervention': self.provide_quranic_intervention()
            }
    
    def provide_quranic_intervention(self):
        """
        Quranic reframe when comparison anxiety detected
        """
        return {
            'ayah': 'An-Nisa 4:32',
            'message': 'Allah says: Do not wish for what He gave others. Each person has their own share of what they EARNED.',
            
            'reframes': {
                'from': 'Why is my job search taking longer than others?',
                'to': 'Allah\'s timing is perfect. My provision will come when HE knows it\'s best for me.'
            },
            
            'action_items': [
                {
                    'action': 'Stop comparing',
                    'how': 'Limit LinkedIn browsing to 15 min/day. Unfollow accounts that trigger envy.',
                    'quranic_basis': '4:32 - "Do not wish for what Allah gave others"'
                },
                {
                    'action': 'Focus on YOUR effort',
                    'how': 'Improve your CV, learn new skills, apply consistently.',
                    'quranic_basis': '4:32 - "For each a share of what THEY EARNED" - focus on your own work'
                },
                {
                    'action': 'Make dua daily',
                    'how': 'After Fajr, make sincere dua for halal provision.',
                    'quranic_basis': '4:32 - "Ask Allah of His bounty"'
                },
                {
                    'action': 'Trust Allah\'s wisdom',
                    'how': 'Remember: Allah is "Knowing" - He knows what job, salary, timing is best for you.',
                    'quranic_basis': '4:32 - "Indeed Allah is Knowing"'
                }
            ],
            
            'success_stories': load_anonymous_success_stories(),
            'note': 'Many successful people had long job searches. Allah\'s plan is perfect.'
        }
**Feature: "Your Rizq Journey" - Personalized Path Tracker:**
def personalized_rizq_journey(user):
    """
    Counter comparison by emphasizing individual journey
    """
    return {
        'title': 'Your Unique Rizq Journey',
        'ayah': 'Quran 4:32 - "For each a share of what THEY earned"',
        
        'your_journey': {
            'applications_sent': user.applications_sent,
            'interviews_completed': user.interviews_completed,
            'skills_improved': user.skills_learned,
            'days_seeking': user.job_search_duration_days,
            'dua_consistency': user.daily_dua_streak
        },
        
        'reminder': 'Don\'t compare your Day 30 with someone else\'s Day 300. Trust YOUR timeline.',
        
        'encouragement': {
            'message': 'You\'re doing the work (earning your share). Allah will give results in His perfect timing.',
            'prophet_example': 'Prophet Musa (AS) worked as a shepherd for years before his grand mission. Allah was preparing him.',
            'dua': 'O Allah, I\'ve done my part. I trust Your timing. Send my provision when You know it\'s best.'
        }
    }


**Verse 4:** Al-Baqarah 2:198 
Arabic:
لَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَبْتَغُوا۟ فَضْلًا مِّن رَّبِّكُمْ
**Translation:**
"There is no blame upon you for seeking bounty from your Lord [during Hajj]."
**Context:**
Revealed in Madinah regarding Hajj. Before Islam, Arabs had trade fairs during Hajj season but felt guilty mixing "spiritual" pilgrimage with "worldly" commerce. Allah clarifies: seeking lawful provision during Hajj is permissible - there's no separation between spiritual and economic life.
**Application:**
- No sacred/secular divide: Commerce is not "un-spiritual"
- "Fadl min Rabbikum" (فَضْلًا مِّن رَّبِّكُمْ): "Bounty from your Lord" - even business transactions are from Allah
- Permission during Hajj: If trade is allowed during most sacred act (Hajj), it's certainly encouraged in daily life
- Historical context: Makkah was trade hub - Ka'bah at center of commerce AND worship
**Scholarly Insight:**
- Imam Al-Tabari: "This verse removes the misconception that spirituality requires abandoning livelihood. Allah permitted trade during Hajj to show that earning halal income is part of Islamic life, not contradictory to it."
- Ibn Abbas (RA): Explained that this verse refers to the trade caravans and business conducted during Hajj season, confirming Islam's positive view of ethical commerce.
**Implementation Suggestion:**
def reframe_business_as_worship(user):
    """
    Help Muslim entrepreneurs/workers see their work as spiritually valid
    """
    
    return {
        'misconception': 'Many Muslims feel guilty about focusing on career/business, as if it\'s "not Islamic enough"',
        
        'quranic_correction': {
            'ayah': 'Al-Baqarah 2:198',
            'message': 'Allah permits seeking bounty even during HAJJ - the most sacred act!',
            'implication': 'If business is allowed during Hajj, your daily work is absolutely acceptable to Allah (as long as it\'s halal)'
        },
        
        'reframe': {
            'business_is_ibadah': 'When you earn halal income with good intention, your business IS worship',
            'prophet_example': 'Many Prophets were businessmen: Ibrahim, Yusuf, Shu\'ayb, and our Prophet Muhammad ﷺ was a merchant',
            'companion_example': 'Abdur-Rahman ibn Awf (RA) was one of the wealthiest Companions. The Prophet ﷺ praised him.'
        },
        
        'conditions_for_business_as_worship': [
            '1. Halal industry (verify with Rizq platform)',
            '2. Honest dealings (no cheating, lying, or exploitation)',
            '3. Fair treatment of employees/partners',
            '4. Fulfill obligations (zakat, charity, family support)',
            '5. Right intention: earning to support family, help ummah, not just hoarding'
        ],
        
        'for_entrepreneurs': {
            'message': 'Building a halal business is a spiritual act',
            'ayah': '2:198 - Allah permits seeking bounty',
            'action': 'Make dua before business meetings. See customers as amanah (trust). Remember Allah in profit and loss.'
        }
    }
**Feature: Business Ethics Certification:**
def islamic_business_ethics_badge(business_account):
    """
    Businesses on Rizq platform can earn ethics badge
    Shows they operate per Islamic principles
    """
    
    criteria = {
        'honest_advertising': 'No misleading claims about products/services',
        'fair_pricing': 'No price gouging or exploitation',
        'employee_treatment': 'Fair wages, safe conditions, respect',
        'prompt_payment': 'Pay workers/suppliers on time (hadith: pay worker before sweat dries)',
        'quality_products': 'No selling defective goods knowingly',
        'environmental_responsibility': 'No wasteful or harmful practices',
        'charity_contribution': 'Regular sadaqah/zakat from business profits'
    }
    
    if business_meets_all_criteria(business_account, criteria):
        return {
            'badge': 'Islamic Business Ethics Certified ✓',
            'displayed_on_profile': True,
            'message': 'This business operates according to Quranic principles (2:198) - seeking bounty with integrity',
            'trust_indicator': 'Job seekers can trust this employer\'s commitment to Islamic values'
        }


**Verse 5:** Al-Baqarah 2:212
"Beautified for those who disbelieve is the life of this world, and they ridicule those who believe. But those who fear Allah are above them on the Day of Resurrection. And Allah gives provision to whom He wills without account."
**Context:**
Revealed in Madinah when wealthy Quraysh disbelievers mocked poor Muslim migrants. Allah reassures believers: worldly wealth doesn't indicate Allah's favor, and He provides "without account" (bi-ghayri hisab) - limitlessly - to whom He wills.
**Application:**
- "Without account" (بِغَيْرِ حِسَابٍ): Allah's provision has no limit
- Don't be deceived by wealth of wrongdoers: Success isn't just material
- Taqwa (God-consciousness) matters more than wealth: But halal wealth WITH taqwa is excellent
- Allah chooses whom to provide: Trust His wisdom in your provision
**Critical Insight for Job Seekers:**
# Scarcity Mindset vs. Abundance Mindset:
Many job seekers operate from scarcity:

- "There aren't enough good jobs"
- "The market is too competitive"
- "I'll never find halal income in my field"

# Quranic Abundance Mindset (2:212):

- "Allah provides without limit" (bi-ghayri hisab)
- His provision is not constrained by "market conditions"
- Make effort (tying camel), then trust Allah's limitless provision
**Implementation:**
def abundance_mindset_training(user):
    """
    Shift from scarcity to Islamic abundance mindset
    Based on Quran 2:212 - "Allah provides without account"
    """
    
    return {
        'scarcity_mindset_indicators': [
            'Feeling there are "not enough" good jobs',
            'Anxiety that someone else getting a job means less opportunity for you',
            'Settling for haram income because "halal options are limited"',
            'Believing your skills aren\'t valuable enough'
        ],
        
        'quranic_abundance_reframe': {
            'ayah': 'Al-Baqarah 2:212',
            'key_phrase': 'Allah provides WITHOUT ACCOUNT (limitlessly)',
            
            'new_beliefs': [
                'Allah\'s provision has no limit - there IS halal rizq for you',
                'Someone else\'s success doesn\'t reduce your provision (Allah provides "without account")',
                'The "job market" doesn\'t constrain Allah - He creates opportunities',
                'Your skills are valuable because Allah gave them to you for a purpose'
            ]
        },
        
        'practical_shifts': {
            'from_scarcity': 'Anxiously competing against others',
            'to_abundance': 'Confidently seeking YOUR unique provision',
            
            'from_scarcity': 'Settling for first offer (even if questionable)',
            'to_abundance': 'Trusting Allah to provide the RIGHT opportunity',
            
            'from_scarcity': 'Believing halal options are too limited',
            'to_abundance': 'Knowing Allah can create halal provision from anywhere'
        },
        
        'dua_for_abundance': 'O Allah, You provide without limit. I trust Your limitless provision. Send me halal rizq from sources I cannot imagine.',
        
        'success_story_feature': load_stories_of_unexpected_provision(),
        'note': 'Many users found provision from completely unexpected sources. Allah\'s creativity is limitless.'
    }
**Feature: "Provision Miracles" - User Testimonials:**
def provision_miracles_section(user):
    """
    Share anonymized stories of unexpected provision
    Reinforces "Allah provides without account"
    """
    
    stories = [
        {
            'title': 'Job Offer from Unexpected Place',
            'story': 'Applied to 50 companies, got rejected. Made dua. A small company I never heard of reached out through Rizq. Best job I ever had.',
            'ayah': 'Quran 2:212 - Allah provides without account',
            'lesson': 'Allah\'s provision comes from places you don\'t expect'
        },
        {
            'title': 'Salary Higher Than Expected',
            'story': 'Expected £30k offer. Company offered £42k without negotiation. Allah\'s generosity exceeded my imagination.',
            'ayah': 'Quran 2:212 - Allah provides limitlessly',
            'lesson': 'Don\'t limit Allah with your expectations'
        },
        {
            'title': 'Lost Job, Found Better One',
            'story': 'Got laid off, terrified. Within 2 weeks, better role with better pay. Allah was upgrading my rizq.',
            'ayah': 'Quran 2:212 - He provides to whom He wills',
            'lesson': 'Sometimes Allah removes provision to give you better'
        }
    ]
    
    return {
        'section_title': 'Provision Miracles: When Allah Provides "Without Account"',
        'purpose': 'Build faith in Allah\'s limitless provision',
        'stories': stories,
        'user_can_submit': True,
        'anonymity': 'All stories anonymous to prevent riya (showing off)'
    }



## PART 4: DIGNITY OF LABOR (Rizq Foundation)

### Hadith on Working with One's Hands

**Hadith 1:** No Food Better Than What You Earn With Your Hands
**Fulll Text** 
"Nobody has ever eaten a better meal than that which one has earned by working with one's own hands. The Prophet of Allah, Dawud (David), used to eat from the earnings of his manual labor."
Sahih al-Bukhari 2072
Authentication: Sahih (Authentic)
Narrator: Al-Miqdam ibn Ma'dikarib (RA)
**Context:**
The Prophet ﷺ praised Prophet Dawud (AS), who was a king but still worked as a blacksmith making armor with his own hands. This establishes the dignity of manual labor and earning through one's own effort, regardless of status.
**Application:**
- Manual labor is honorable: Islam doesn't distinguish "blue collar" vs "white collar" - all honest work is dignified
- Self-reliance is praised: Earning yourself is better than depending on charity or others
- Prophet Dawud's example: Even kings should work
- "Working with hands": While literal here, scholars extend to any self-earned income

# Modern Application - Fighting Job Snobbery:
Problem: Modern society creates hierarchy of jobs:

- "Prestigious" jobs (doctor, lawyer, engineer)
- "Ordinary" jobs (retail, delivery, construction)
- Many Muslims feel ashamed of "lower status" jobs
**Islamic Teaching:**
This hadith demolishes job snobbery. If a PROPHET worked with his hands in manual labor, no job is beneath a Muslim's dignity.
**Implementation:**
def dignify_all_halal_work(job_listing):
    """
    Ensure Rizq platform treats ALL halal jobs with equal dignity
    Combat societal job hierarchy
    """
    
    # DO NOT categorize jobs as "prestige" vs "ordinary"
    # Instead, emphasize halal nature and effort
    
    job_display = {
        'title': job_listing.title,
        'company': job_listing.company,
        'salary': job_listing.salary,
        
        # Equal dignity message for ALL jobs
        'islamic_frame': 'The Prophet ﷺ said: "No food is better than what you earn with your own hands." (Bukhari)',
        
        'dignity_statement': 'This is halal work. Earning through your effort is honored in Islam, regardless of job type.',
        
        # NO "prestige" badges or hierarchy indicators
        # Every halal job gets same respectful presentation
    }
    
    # Special encouragement for jobs society undervalues
    if job_listing.type in ['manual_labor', 'service_industry', 'retail']:
        job_display['additional_encouragement'] = {
            'message': 'Prophet Dawud (AS) worked with his hands despite being a king. You are following prophetic example.',
            'hadith': 'Bukhari 2072',
            'reminder': 'Allah sees your intention and effort, not society\'s job rankings.'
        }
    
    return job_display
**Feature: Reject "Job Prestige" Filters:**
def no_prestige_filters():
    """
    Rizq platform refuses to implement "prestige" or "status" filters
    All halal work is treated with equal dignity
    """
    
    # Standard job filters (allowed)
    allowed_filters = [
        'industry',
        'location',
        'salary_range',
        'full_time_vs_part_time',
        'remote_vs_onsite',
        'halal_certification_level'
    ]
    
    # Prohibited filters (reinforce hierarchy)
    prohibited_filters = [
        'prestige_level',
        'job_status',
        'company_ranking',
        'social_perception'
    ]
    
    return {
        'philosophy': 'Islam dignifies ALL halal work equally. We refuse to rank jobs by societal prestige.',
        'hadith_basis': 'Prophet ﷺ praised Prophet Dawud\'s manual labor (Bukhari 2072)',
        'message_to_users': 'Filter by your needs (location, salary, field), but know that every halal job on Rizq is dignified work.'
    }

### The Upper Hand vs. Lower Hand

**Hadith on giving being better than receiving:**  
**Hadith 2:** The Hand That Gives is Better Than the Hand That Receives
**Full Text:** 
"The upper hand is better than the lower hand. The upper hand is the one that gives, and the lower hand is the one that receives."
**Source:** Sahih al-Bukhari 1429, Sahih Muslim 1033
**Authentication:** Sahih (Authentic) - Agreed upon
**Narrator:** Hakim ibn Hizam (RA)
**Context:**
The Prophet ﷺ taught that self-sufficiency (earning and giving) is superior to dependency (receiving charity). While receiving charity when truly in need is permissible, striving to be in the position to GIVE is the Islamic ideal.
**Application:**
- Empowerment over dependency: Platform's goal is moving users from "lower hand" (receiving) to "upper hand" (giving)
- Charity is good, but self-sufficiency is better: Rizq helps users reach self-reliance
- Giving includes family support: Not just formal charity - providing for family is "upper hand"
- Motivation for job seekers: Your goal isn't just a paycheck, it's becoming a GIVER
**Implementation:**
def empowerment_journey_tracker(user):
    """
    Track user's journey from dependency toward self-sufficiency
    Based on hadith: "Upper hand (giving) is better than lower hand (receiving)"
    """
    
    return {
        'title': 'Your Journey to the Upper Hand',
        'hadith': 'The Prophet ﷺ said: "The upper hand (that gives) is better than the lower hand (that receives)." (Bukhari & Muslim)',
        
        'journey_stages': {
            'stage_1': {
                'name': 'Seeking Self-Sufficiency',
                'description': 'You\'re searching for halal income to support yourself/family',
                'current_status': 'Lower hand (receiving help)',
                'goal': 'Upper hand (self-sufficient)',
                'encouragement': 'Every application you send is a step toward the upper hand. Keep striving!',
                'dua': 'O Allah, make me self-sufficient through halal provision.'
            },
            'stage_2': {
            'name': 'Self-Sufficiency Achieved',
            'description': 'You have halal income covering your basic needs',
            'status': 'No longer dependent on others - Alhamdulillah!',
            'goal': 'Begin giving to others',
            'encouragement': 'You\'ve reached the upper hand! Now you can start helping others.',
            'next_milestone': 'Give regular sadaqah, even small amounts'
            },
            
            'stage_3': {
                'name': 'The Upper Hand - Giver',
                'description': 'You provide for yourself AND give to others',
                'status': 'Upper hand - as praised by the Prophet ﷺ',
                'celebration': 'Masha\'Allah! You\'ve achieved the prophetic ideal.',
                'continued_growth': 'Increase charity as Allah increases your provision',
                'hadith': 'The Prophet ﷺ said: "Charity does not decrease wealth." (Muslim)'
            }
            },
            
            'user_current_stage': determine_user_stage(user),
            
            'action_items': generate_stage_specific_actions(user),
            
            'inspiration': {
                'companion_example': 'Abdur-Rahman ibn Awf (RA) came to Madinah with nothing. He asked for work, not charity. Eventually became wealthy and gave massive sadaqah.',
                'lesson': 'The goal is transformation from receiver to giver. You\'re on that path.'
            }
}


### Excellence in Work

**Hadith on ihsan/perfection in work:**  

**Hadith 3:** Start with Yourself, Then Your Dependents
**Full Text:** "Start with yourself, then with those who are your dependents."
**Source:**
 Sahih Muslim 997
Authentication: Sahih (Authentic)
Narrator: Jabir ibn Abdullah (RA)
**Full Context:**
A man came to the Prophet ﷺ with a piece of gold he wanted to give as charity. The Prophet ﷺ refused it and said: "Start with yourself and give charity to yourself. If anything is left over, then to your family. If anything is left over after your family, then to your relatives. If anything is left over after your relatives, then this way and that way (to others)."
**Application:**
Hierarchy of financial responsibility:

- Yourself (self-sufficiency first)
- Your dependents (spouse, children, parents)
- Extended family
- General charity

- You cannot give what you don't have: Secure your own provision before extensive charity
- Supporting family IS charity: Providing for wife/children is sadaqah, not "just" obligation
- Balance: Not selfishness, but wisdom - you're most responsible for those closest
**Modern Misunderstandings:**
Problem: Some Muslims feel guilty for:

- Spending on themselves (food, clothing, shelter)
- Prioritizing family needs before general charity
- Building emergency savings before giving extensively
**Hadith Correction:**
The Prophet ﷺ himself taught: start with YOURSELF, then dependents, then others. This is the Islamic order of priorities.
**Implementation:**
def financial_priorities_guidance(user):
    """
    Help users understand Islamic hierarchy of financial responsibilities
    Based on hadith: "Start with yourself, then your dependents" (Muslim 997)
    """
    
    return {
        'hadith': 'The Prophet ﷺ said: "Start with yourself, then your dependents." (Muslim)',
        
        'islamic_financial_priorities': {
            'priority_1': {
                'who': 'Yourself',
                'what': 'Basic needs (food, shelter, clothing, healthcare)',
                'why': 'You cannot help others if you collapse from neglecting yourself',
                'example': 'Eating nutritious food, having safe housing, necessary medicine',
                'NOT': 'This does NOT mean luxury for yourself while family suffers'
            },
            
            'priority_2': {
                'who': 'Your dependents (spouse, children, elderly parents)',
                'what': 'Their basic needs + reasonable comfort',
                'why': 'You are MOST responsible for those under your care',
                'example': 'Children\'s food, education, clothing. Spouse\'s needs. Parents\' care.',
                'hadith': 'The Prophet ﷺ said: "It is sufficient sin for a man to neglect those whom he maintains." (Abu Dawud)'
            },
            
            'priority_3': {
                'who': 'Extended family (siblings, relatives in need)',
                'what': 'Help according to your capacity',
                'why': 'Maintaining family ties is emphasized in Islam',
                'example': 'Helping unemployed brother, supporting widowed aunt',
                'balance': 'After YOUR family is secure, help extended family'
            },
            
            'priority_4': {
                'who': 'General charity (masjid, orphans, ummah causes)',
                'what': 'Give from surplus, not from family\'s needs',
                'why': 'Charity is beautiful, but not at expense of your dependents',
                'example': 'After all above are met, give generously to worthy causes',
                'zakat_note': 'Zakat (2.5%) is obligation at all levels, but EXTRA charity follows this hierarchy'
            }
        },
        
        'practical_application': {
            'job_seeker': 'Focus on finding work to support yourself + family FIRST. This is your primary obligation.',
            'employed_with_family': 'Ensure family\'s needs are met before extensive charity. Supporting them IS charity.',
            'employed_with_surplus': 'Alhamdulillah! Now you can give more generously to wider causes.',
            'guilty_about_spending_on_self': 'The Prophet ﷺ said START with yourself. Basic self-care is not selfish, it\'s Islamic.'
        },
        
        'balance_reminder': {
            'not_extreme_selfishness': 'This doesn\'t mean hoarding wealth for luxury while others starve',
            'not_extreme_self_denial': 'This doesn\'t mean giving everything away and leaving family destitute',
            'the_middle_path': 'Secure yourself + dependents at reasonable level, THEN give generously from surplus'
        }
    }
**Feature: "Responsibility Checker"**
def check_financial_responsibilities_fulfilled(user):
    """
    Before encouraging large charity, check if user's primary obligations met
    """
    
    responsibilities = {
        'self_care': {
            'question': 'Are YOUR basic needs met? (food, shelter, clothing, health)',
            'user_answer': user.self_assessment.basic_needs_met,
            'priority': 1
        },
        
        'dependents_care': {
            'question': 'Are your DEPENDENTS\' needs met? (spouse, children, parents you support)',
            'user_answer': user.self_assessment.dependents_needs_met,
            'priority': 2
        },
        
        'debt_freedom': {
            'question': 'Are you free from urgent debts?',
            'user_answer': user.self_assessment.no_urgent_debt,
            'priority': 2.5,
            'note': 'Paying off debt can take precedence over extra charity'
        },
        
        'emergency_fund': {
            'question': 'Do you have 3-6 months emergency savings?',
            'user_answer': user.self_assessment.has_emergency_fund,
            'priority': 3,
            'note': 'Having buffer prevents future dependency on charity (reaching "upper hand")'
        }
    }
    
    # If priorities 1-2 NOT met, gentle redirection
    if not responsibilities['self_care']['user_answer'] or not responsibilities['dependents_care']['user_answer']:
        return {
            'guidance': 'Focus on fulfilling your primary obligations first',
            'hadith': 'The Prophet ﷺ said: "Start with yourself, then your dependents." (Muslim)',
            'action': 'Prioritize finding stable income to meet these needs',
            'charity_note': 'Give your obligatory zakat, but extra charity can wait until primary responsibilities met',
            'no_guilt': 'This is not selfishness - this is following prophetic guidance on priorities.'
        }
    
    # If priorities met, encourage generous giving
    else:
        return {
            'celebration': 'Masha\'Allah! Your primary obligations are fulfilled.',
            'next_level': 'You are now in position to give generously to wider causes',
            'hadith': 'The Prophet ﷺ: After self + dependents, give "this way and that way" (broadly)',
            'suggestions': [
                'Increase regular sadaqah',
                'Sponsor orphan education',
                'Support Islamic institutions',
                'Help employed users on Rizq mentor job seekers'
            ]
        }


**Hadith 4:** Seeking Halal Income is Obligatory
**Full Text:**
"Seeking halal (lawful) earnings is an obligation after the obligations.
**Source**
Al-Bayhaqi in Shu'ab al-Iman 4/334, Al-Tabarani in Al-Mu'jam Al-Awsat
**Authentication**
Weak chain (Da'if), BUT the MEANING is supported by authentic texts
Note: While this exact wording is not Sahih, scholars accept its meaning based on:
- Quranic verses commanding earning (67:15, 62:10)
- Authentic hadiths praising self-earned income
- Scholarly consensus (ijma') that seeking halal income is highly encouraged
**Scholarly Consensus:**
- Imam Al-Ghazali: "Seeking halal provision is obligatory to the extent that it's needed to fulfill other obligations (feeding family, paying zakat, etc.)."
- Ibn Taymiyyah: "Working to earn halal income can be fard (obligatory), mandub (recommended), or mubah (permissible) depending on one's circumstances and needs."
**Application**
Seeking halal income is religiously significant: Not just "making money," it's fulfilling Islamic responsibility
Quality matters: HALAL income, not just "any" income
Connects to other obligations: You can't pay zakat without wealth, can't support family without income
Active seeking required: Not passive waiting, but effort ("seeking")
**Implementation**
def frame_job_search_as_religious_duty(user):
    """
    Reframe job searching from burden to Islamic obligation
    """
    
    return {
        'reframe': {
            'secular_view': 'Job hunting is stressful necessity of modern life',
            'islamic_view': 'Seeking halal income is religious responsibility - you\'re fulfilling duty to Allah'
        },
        
        'scholarly_teaching': {
            'principle': 'Seeking halal income is obligation after primary obligations',
            'explanation': 'You cannot fulfill other Islamic duties (zakat, family support, hajj) without income',
            'implication': 'Your job search is NOT separate from your deen - it\'s PART of your deen'
        },
        
        'motivation_boost': {
            'when_discouraged': {
                'feeling': 'This job search is hopeless/exhausting',
                'reframe': 'You are fulfilling Islamic obligation by seeking halal income. Allah sees your effort.',
                'dua': 'O Allah, I am obeying Your command to seek provision. Make this path easy for me.'
            },
            
            'when_rejected': {
                'feeling': 'Another rejection - I\'m worthless',
                'reframe': 'Rejection is part of the test. You\'re still fulfilling your duty by seeking. Allah controls results.',
                'prophet_example': 'Prophet Nuh (AS) called people to Islam for 950 years with minimal response. He still fulfilled his duty.'
            },
            
            'when_tempted_by_haram_income': {
                'temptation': 'Haram job pays more/is easier to get',
                'reminder': 'The obligation is seeking HALAL income. Haram income doesn\'t fulfill the duty - it violates it.',
                'hadith': 'The Prophet ﷺ: "Allah is pure and accepts only that which is pure." (Muslim)'
            }
        },
        
        'daily_intention_setting': {
            'morning': 'Before job searching, say: "Bismillah. I seek halal provision in obedience to Allah."',
            'during_search': 'Remember: every application is an act of worship when done with right intention',
            'evening': 'Reflect: I fulfilled my obligation today by seeking. Results are with Allah.'
        }
    }
**Feature: Job Search as Ibadah Tracker:**
def job_search_as_worship_tracker(user):
    """
    Gamify job search as acts of worship (with right intention)
    Makes the process feel spiritually meaningful, not just secular grind
    """
    
    return {
        'title': 'Your Job Search Ibadah Tracker',
        'teaching': 'Seeking halal income is obligation after primary obligations. Your effort is worship.',
        
        'daily_actions_as_ibadah': {
            'applications_sent': {
                'count': user.applications_today,
                'spiritual_frame': 'Acts of obedience to Allah\'s command to seek provision',
                'dua_after_each': 'Allahumma yassir wa la tu\'assir (O Allah, make it easy, not difficult)'
            },
            
            'cv_improved': {
                'action': 'Updated CV or learned new skill',
                'spiritual_frame': 'Preparing yourself is part of seeking - tying the camel',
                'hadith': 'Trust in Allah, but tie your camel (authentic meaning, though wording varies)'
            },
            
            'networking': {
                'action': 'Reached out to contacts, attended events',
                'spiritual_frame': 'Using means Allah provided (connections) to seek provision',
                'quranic': 'Quran 62:10 - "Disperse through the land seeking bounty"'
            },
            
            'dua_consistency': {
                'action': 'Made dua for halal provision',
                'spiritual_frame': 'Asking Allah while making effort = complete tawakkul',
                'quranic': 'Quran 4:32 - "Ask Allah of His bounty"'
            }
        },
        
        'weekly_summary': {
            'total_acts_of_seeking': calculate_weekly_job_search_activities(user),
            'message': f'You performed {total} acts of seeking halal provision this week. This is ibadah!',
            'encouragement': 'You\'re fulfilling your Islamic responsibility. Keep going.',
            'reminder': 'Results are with Allah. Your job is effort. His job is results.'
        },
        
        'motivation_when_no_results': {
            'principle': 'Reward is for effort, not just outcome',
            'example': 'Prophet Nuh (AS) preached 950 years with few believers. Allah rewarded his EFFORT.',
            'your_situation': 'Even if offers haven\'t come yet, your seeking effort is rewarded by Allah.',
            'continue': 'Keep making effort. Trust Allah\'s timing.'
        }
    }
**Hadith 5: Seeking Knowledge and Earning Both Valued**
**Full Text**
"Seeking knowledge is an obligation upon every Muslim."
**Source**
Sunan Ibn Majah 224
Authentication: Hasan (Good) according to Al-Albani
**Related Teaching**
The Prophet ﷺ praised both religious knowledge AND worldly skills/trades. Many Companions were skilled in various professions: blacksmiths, merchants, farmers, physicians.
**Application**
- Knowledge = employability: Gaining skills is Islamic investment
- Continuous learning encouraged: Islam values growth and development
- Worldly skills not "less Islamic": Carpentry, coding, teaching, medicine - all valuable
- Link knowledge to provision: "Seeking knowledge" includes skills that enable halal earning
**Implementation**
def skills_development_as_islamic_investment(user):
    """
    Frame professional development as Islamic obligation
    "Seeking knowledge" includes skills for halal provision
    """
    
    return {
        'hadith': 'The Prophet ﷺ said: "Seeking knowledge is obligation upon every Muslim." (Ibn Majah)',
        
        'types_of_beneficial_knowledge': {
            'religious_knowledge': {
                'examples': 'Quran, hadith, fiqh, aqeedah',
                'purpose': 'Worship Allah correctly',
                'obligation_level': 'Fard (obligatory) - basics for every Muslim'
            },
            
            'worldly_knowledge_for_provision': {
                'examples': 'Professional skills, trades, technology, business',
                'purpose': 'Earn halal income, serve community, fulfill responsibilities',
                'obligation_level': 'Fard kifayah (collective obligation) - ummah needs skilled professionals',
                'individual_level': 'Highly encouraged (mandub) - especially if needed for self-sufficiency'
            }
        },
        
        'integrated_approach': {
            'not_either_or': 'You don\'t choose between religious knowledge OR professional skills',
            'both_required': 'Learn deen to worship correctly. Learn skills to earn halal provision.',
            'prophet_example': 'Prophet Muhammad ﷺ was shepherd AND merchant AND military commander - multiple skills',
            'companion_examples': [
                'Umar ibn Al-Khattab (RA): businessman',
                'Ammar ibn Yasir (RA): builder',
                'Salman Al-Farsi (RA): expert in warfare engineering',
                'All were scholars AND skilled professionals'
            ]
        },
        
        'rizq_platform_support': {
            'free_courses': 'Rizq provides free skills training (coding, digital marketing, etc.)',
            'islamic_framing': 'These courses are helping you fulfill "seeking knowledge" while pursuing halal provision',
            'certificates': 'Earn credentials to increase employability',
            'mentorship': 'Learn from experienced Muslims in your field'
        }
    }
**Feature: "Seeking Knowledge for Rizq" - Free Skills Courses:**
def rizq_learning_academy(user):
    """
    Free courses to make Muslims employable in halal industries
    Framed as Islamic obligation to seek beneficial knowledge
    """
    
    courses = {
        'digital_skills': {
            'courses': ['Web Development', 'Digital Marketing', 'Data Analysis', 'UI/UX Design'],
            'why_offered': 'High demand in halal industries, remote work possible',
            'islamic_frame': 'Seeking knowledge to enable halal provision',
            'hadith': 'Ibn Majah 224 - Seeking knowledge is obligation'
        },
        
        'business_skills': {
            'courses': ['Islamic Business Ethics', 'Halal Entrepreneurship', 'Bookkeeping', 'Customer Service'],
            'why_offered': 'Enable Muslims to start halal businesses',
            'islamic_frame': 'Learning to trade ethically as Prophet Muhammad ﷺ did',
            'quranic': 'Quran 2:198 - Seeking bounty is permissible'
        },
        
        'professional_development': {
            'courses': ['CV Writing', 'Interview Skills', 'LinkedIn Optimization', 'Networking'],
            'why_offered': 'Practical skills for job market success',
            'islamic_frame': 'Preparing yourself is part of "tying the camel"',
            'wisdom': 'Trust Allah, but use the means He provided'
        },
        
        'language_skills': {
            'courses': ['English for Professionals', 'Business Communication', 'Arabic (for understanding Islamic sources)'],
            'why_offered': 'Communication skills increase employability',
            'dual_benefit': 'English helps career. Arabic helps understand Quran.'
        }
    }
    
    return {
        'title': 'Rizq Learning Academy: Seeking Knowledge for Provision',
        'motto': 'The Prophet ﷺ commanded seeking knowledge. We help you seek knowledge that enables halal provision.',
        
        'all_courses_free': True,
        'why_free': 'Removing barriers to halal employment is sadaqah jariyah. Your success is our mission.',
        
        'courses': courses,
        
        'completion_benefits': {
            'certificate': 'Rizq Learning Academy certificate (recognized by partner employers)',
            'profile_badge': 'Display on Rizq profile - employers see your commitment to growth',
            'priority_matching': 'Get priority consideration for relevant jobs',
            'mentorship': 'Connect with mentor in your field'
        },
        
        'user_testimonial': '"I had no tech skills. Took Rizq\'s web development course. Got hired 2 months after completing. Changed my life." - Anonymous, Birmingham'
    }


## PART 5: HALAL INCOME CRITERIA (Rizq Foundation)

### Clearly Haram Industries

**Quranic/Hadith Evidence:**  
[Will populate from research]

**List:**
- Riba-based businesses (banking, conventional finance)
- Alcohol production/distribution
- Gambling operations
- Pork products
- Entertainment involving haram

### Questionable Industries (Scholarly Differences)

**Category:** Alcohol Production, Sale, or Service
**Quranic Evidence:** 
"O you who have believed, indeed, intoxicants, gambling, [sacrificing on] stone alters [to other than Allah], and divining arrows are but defilement from the work of Satan, so avoid it that you may be successful." (Quran 5:90)
**Hadith Evidence:** 
"Allah has cursed alcohol, its drinker, its server, its seller, its buyer, its presser, the one for whom it is pressed, the one who conveys it, and the one to whom it is conveyed." (Sunan Abu Dawud 3674, authenticated as Sahih)
**Ruling:** HARAM - Completely prohibited
**Includes**
- Breweries, distilleries, wineries
- Bars, pubs, nightclubs
- Liquor stores
- Restaurants where alcohol is primary business
- Alcohol delivery services
- Serving alcohol in any capacity (waiter, bartender)
**Grey areas**
Supermarkets that sell alcohol: Scholars differ

- Stricter opinion: Avoid if alcohol is significant portion
- Lenient opinion: Permissible if alcohol is minor item among groceries and you don't handle it directly
- Recommendation for Rizq: Mark as "questionable - consult scholar" if alcohol <10% of store's business
**Implementation:**
HARAM_INDUSTRIES = {
    'alcohol': {
        'prohibited_roles': [
            'Bartender',
            'Sommelier',
            'Brewery worker',
            'Liquor store employee',
            'Alcohol sales representative',
            'Wine taster',
            'Nightclub staff (where alcohol is primary)'
        ],
        'evidence': {
            'quran': '5:90 - Intoxicants are defilement from Satan',
            'hadith': 'Abu Dawud 3674 - Curse on all involved in alcohol chain',
            'ruling': 'Unanimous prohibition (ijma\') - all scholars agree'
        },
        'no_exceptions': True,
        'severity': 'CRITICAL'
    }
}

def check_alcohol_industry(job_listing):
    """
    Automatically reject jobs in alcohol industry
    """
    if job_listing.industry == 'alcohol' or 'alcohol' in job_listing.description.lower():
        return {
            'halal_status': 'HARAM',
            'reason': 'Alcohol industry - all involvement prohibited',
            'evidence': 'Quran 5:90, Hadith (Abu Dawud 3674)',
            'action': 'Job listing REMOVED from platform',
            'message_to_employer': 'Rizq platform does not list alcohol-related positions per Islamic prohibition.'
        }
**Category 2:** Gambling and Casinos
**Quranic Evidence:** 
Same as alcohol - Quran 5:90 groups gambling with intoxicants
**Hadith Evidence:**  
"Whoever says to his companion, 'Come, let us gamble,' should give charity (as expiation)." (Sahih al-Bukhari 6107) - Even inviting to gamble requires expiation
**Haram:** HARAM - Completely prohibited
**Includes**
- Casinos (any role: dealer, security, cleaning, IT)
- Online gambling platforms
- Sports betting companies
- Lottery ticket sales
- Gaming apps with gambling mechanics
- Poker tournaments, bingo halls
**Grey Areas**
Video game development: If game includes gambling-like mechanics (loot boxes, chance-based purchases)

- Recommendation: Avoid if gambling is core mechanic. Permissible if minor feature that can be ignored.
**Implementation**
HARAM_INDUSTRIES['gambling'] = {
    'prohibited_roles': [
        'Casino dealer',
        'Sports betting analyst',
        'Online gambling developer',
        'Lottery ticket vendor',
        'Poker tournament organizer',
        'Bingo hall staff'
    ],
    'evidence': {
        'quran': '5:90 - Gambling is Satan\'s work',
        'hadith': 'Bukhari 6107 - Even inviting to gamble requires expiation',
        'scholarly_consensus': 'All madhabs agree gambling is major sin'
    },
    'no_exceptions': True,
    'severity': 'CRITICAL',
    'note': 'Any role supporting gambling industry is prohibited, even if not directly gambling'
}
**Industry 3:** Pork Production and Sale
**Quranic Evidence:** "He has only forbidden to you dead animals, blood, the flesh of swine..." (Quran 2:173)
**Ruling:** HARAM - Pork is explicitly forbidden
Includes:
- Pig farming
- Pork processing plants
- Butcher shops specializing in pork
- Restaurants where pork is primary offering
Grey Areas:
- General grocery stores: Permissible if you don't handle pork directly and it's minor item
- Non-Muslim-owned restaurants: Permissible to work in kitchen if you don't cook/serve pork and there's separation
**Implementation**
HARAM_INDUSTRIES['pork'] = {
    'clearly_prohibited': [
        'Pig farming',
        'Pork processing',
        'Pork butcher',
        'BBQ restaurant (pork-focused)'
    ],
    'questionable': [
        'General grocery store (selling pork among other items)',
        'Restaurant with pork on menu (but you don\'t handle it)'
    ],
    'evidence': 'Quran 2:173 - Swine flesh is forbidden',
    'scholarly_guidance': {
        'stricter': 'Avoid any involvement with pork',
        'moderate': 'Permissible if: (1) You don\'t directly handle, (2) It\'s minor part of business, (3) Alternative employment difficult to find',
        'Rizq_default': 'Mark as "needs_verification" - user consults scholar based on specific role'
    }
}
**Industry 4** Interest-Based Financial Institutions
**Quranic Evididence** "Those who consume interest cannot stand [on the Day of Resurrection] except as one stands who is being beaten by Satan into insanity. That is because they say, 'Trade is [just] like interest.' But Allah has permitted trade and has forbidden interest." (Quran 2:275)
**Ruling** HARAM - Riba (interest/usury) is major sin
Includes:
- Conventional banks (interest-based lending/savings)
- Credit card companies (charging interest)
- Payday loan companies
- Interest-based investment firms
- Insurance companies (conventional, not takaful)
**CRITICAL GRAY AREA - This Affects Many Muslims:**
The Question: Can I work at a conventional bank in non-interest role (IT, HR, cleaning)?
Scholarly Opinions:

- Opinion 1 (Stricter - Permanent Council of Senior Scholars, Saudi Arabia):

All roles in interest-based banks are haram,
even if you don't directly handle interest

Rationale: You're supporting the institution that engages in riba
Evidence: Hadith curses those who witness/write interest transactions

- Opinion 2 (Moderate - European Council for Fatwa and Research):

Direct roles in interest (loan officer, investment advisor) are clearly haram
Indirect roles (IT, HR, security, cleaning) are permissible if:

No halal alternative employment available
Muslim population in non-Muslim country needs to survive
Role doesn't directly facilitate interest
Person actively seeks alternative employment


Rationale: Necessity (darurah) permits temporary exceptions
Conditions: This is temporary license, not ideal

- Opinion 3 (Lenient - Some Contemporary Scholars):

Any role in conventional bank is problematic but tolerated due to modern economic reality
Working there while searching for alternative is acceptable
Rationale: Banks are so integrated into modern economy, complete avoidance nearly impossible
**Rizq Platform Approach:**
def assess_banking_role(job_listing):
    """
    Banking jobs require nuanced verification
    """
    
    role_types = {
        'clearly_haram': [
            'Loan officer',
            'Investment advisor (interest-based products)',
            'Credit card sales',
            'Interest calculations',
            'Mortgage lending (conventional)'
        ],
        
        'questionable_indirect': [
            'IT support',
            'HR',
            'Facilities management',
            'Security',
            'Administrative roles',
            'Data entry (not interest-related)'
        ],
        
        'halal_alternative': [
            'Islamic banking roles',
            'Takaful (Islamic insurance)',
            'Shariah-compliant investment firms'
        ]
    }
    
    if job_listing.role in role_types['clearly_haram']:
        return {
            'halal_status': 'HARAM',
            'severity': 'CRITICAL',
            'evidence': 'Quran 2:275-279 - Allah declares war on those involved in riba',
            'action': 'Job listing REMOVED',
            'alternative': 'Search for Islamic banking roles instead'
        }
    
    elif job_listing.role in role_types['questionable_indirect']:
        return {
            'halal_status': 'QUESTIONABLE',
            'severity': 'MEDIUM',
            'warning': '⚠️ This role is in conventional (interest-based) banking',
            'scholarly_differences': {
                'stricter_opinion': 'Avoid all roles in interest-based institutions',
                'moderate_opinion': 'Indirect roles permissible if: (1) No alternative available, (2) You don\'t directly facilitate interest, (3) You actively seek halal alternative',
                'source': 'European Council for Fatwa and Research'
            },
            'user_decision': 'Consult a scholar based on your specific circumstances',
            'action_required': 'User must acknowledge they\'ve read scholarly opinions before applying',
            'better_alternative': 'We recommend Islamic banks. See 47 Islamic finance listings on Rizq.'
        }
    
    elif job_listing.role in role_types['halal_alternative']:
        return {
            'halal_status': 'HALAL',
            'badge': '✓ Shariah-Compliant Finance',
            'message': 'Islamic banking - halal alternative to conventional banks',
            'encouragement': 'Alhamdulillah! This is preferred option.'
        }
**Feature: Islamic Finance Alternative Suggestions**
def suggest_islamic_banking_alternatives(user_searching_conventional_bank_job):
    """
    When user searches conventional banking, proactively suggest Islamic alternatives
    """
    
    return {
        'intervention': {
            'message': 'We noticed you\'re viewing conventional banking roles. Did you know there are Islamic banking alternatives?',
            'tone': 'Helpful, not preachy',
            'data': {
                'islamic_banks_uk': [
                    'Al Rayan Bank',
                    'Gatehouse Bank',
                    'QIB UK',
                    'Bank of London and The Middle East (BLME)'
                ],
                'islamic_finance_firms': 'Various Shariah-compliant investment companies',
                'takaful_companies': 'Islamic insurance alternatives'
            }
        },
        
        'benefits_of_islamic_finance': {
            'halal_income': 'No involvement in riba - completely halal',
            'peace_of_mind': 'Work without scholarly disagreement',
            'support_islamic_economy': 'Help grow ethical finance sector',
            'same_professional_growth': 'Similar roles, salaries, and career progression'
        },
        
        'action': {
            'view_islamic_banking_jobs': f'{islamic_banking_job_count} Islamic finance roles available',
            'set_preference': 'Prioritize Islamic finance in future job matches',
            'still_view_conventional': 'User can still view conventional roles but with warning'
        },
        
        'hadith_reminder': 'The Prophet ﷺ said: "That which is halal is clear and that which is haram is clear." (Bukhari & Muslim) - Choose the clear halal path when possible.'
    }
**Industry 5** Conventional Insurance
**Ruling:** Majority of scholars: HARAM (due to gharar - excessive uncertainty - and riba elements)
**Alternative** Takaful (Islamic insurance based on mutual cooperation, not gambling on risk)
**Includes:**
- Life insurance companies (conventional)
- Health insurance (conventional with interest/gambling elements)
- Auto insurance (conventional)
- Insurance sales agents (conventional products)
**Exception**
 Some scholars permit conventional insurance in non-Muslim countries where:
- It's legally required (car insurance)
- No takaful alternative available
- It's necessity, not investment vehicle
**Implementation:**
HARAM_INDUSTRIES['conventional_insurance'] = {
    'prohibited': 'Conventional insurance (not takaful)',
    'evidence': {
        'scholarly_consensus': 'Majority view: conventional insurance involves gharar and riba',
        'source': 'Islamic Fiqh Academy (OIC) Resolution 9/2',
        'reasoning': 'Gambling on risk + interest-based investments'
    },
    'exceptions': 'Legally required insurance in non-Muslim countries (car insurance) permissible to purchase, but working in industry still problematic',
    'halal_alternative': 'Takaful (Islamic insurance)',
    'rizq_approach': 'Flag conventional insurance jobs, promote takaful companies'
}

**Industry** Adult Entertainment and Immoral Media
**Quranic Evidence:**
"And do not approach unlawful sexual intercourse. Indeed, it is ever an immorality and is evil as a way." (Quran 17:32)
**Ruling**
 HARAM - Anything facilitating or promoting zinā (fornication/adultery) is forbidden
**Includes**
- Adult film industry (any role)
- Strip clubs, escort services
- Pornography websites (development, hosting, marketing)
- Dating apps designed for casual hookups (not marriage)
- Modeling agencies promoting immodest content
- Magazine/media producing sexualized content
**Gray Areas**
- Mainstream media with occasional inappropriate content: Permissible if content is majority appropriate and you're not creating the haram elements
- Tech companies hosting user-generated content: Permissible if company makes reasonable effort to moderate and your role isn't promoting inappropriate content
**Implementation:**
HARAM_INDUSTRIES['adult_entertainment'] = {
    'prohibited_roles': 'Any involvement in adult entertainment industry',
    'evidence': 'Quran 17:32 - Do not approach unlawful sexual relations',
    'severity': 'CRITICAL',
    'no_exceptions': True,
    'note': 'This includes indirect roles (web hosting, payment processing, marketing) that specifically serve adult content'
}



### Questionable Industries (Scholarly Differences)

**Category 1:** Music Industry
**Scholarly Opinions:** Majority (Maliki, Shafi'i, Hanbali): Musical instruments generally haram (with exceptions for duff at weddings)
Hanafi: Similar prohibition
Minority: Some contemporary scholars permit non-intoxicating, moral music
**Evidence:** Prohibition side: Hadith about musical instruments being haram (Bukhari 5590, though scholars debate authenticity of the chain)
Permission side: Prophet ﷺ permitted duff (frame drum) at weddings
**Rizq Platform Approach**
QUESTIONABLE_INDUSTRIES = {
    'music_industry': {
        'scholarly_status': 'Difference of opinion',
        'majority_view': 'Musical instruments generally prohibited',
        'minority_view': 'Permissible if content is moral and doesn\'t promote haram',
        
        'roles_assessment': {
            'clearly_problematic': [
                'Music promoting immoral content (drugs, zinā, violence)',
                'Nightclub DJ',
                'Musician in bars/clubs'
            ],
            'debated': [
                'Sound engineer (neutral content)',
                'Music teacher (educational context)',
                'Islamic nasheed producer (vocals-only or with duff)'
            ]
        },
        
        'rizq_action': {
            'display_warning': True,
            'message': '⚠️ Scholars differ on music industry. Majority prohibit. Consult your scholar.',
            'user_choice': 'User decides based on their madhab/scholar',
            'better_alternative': 'Consider nasheed production (vocals-only Islamic content)'
        }
    }
}

**Category 2** Fashion and Modeling
**Issue:** Promoting immodesty, extravagance, and vanity
**Scholarly Assessment:**
Haram aspects:
- Immodest clothing promotion
- Mixed-gender environments with inappropriate interaction
- Encouraging extravagance and israf
- Body objectification

Potentially permissible:
- Modest Islamic fashion
- Gender-segregated modeling (women modeling for women in hijab fashion)
- Promoting reasonable, non-extravagant clothing
**Implementation:**
QUESTIONABLE_INDUSTRIES['fashion_modeling'] = {
    'default_status': 'Questionable',
    'factors_to_assess': {
        'modesty': 'Is clothing promoted modest per Islamic standards?',
        'segregation': 'Are events/photoshoots gender-segregated when appropriate?',
        'extravagance': 'Is brand promoting luxury/israf or reasonable clothing?',
        'objectification': 'Is focus on clothing or sexualization of models?'
    },
    
    'halal_version': {
        'example': 'Modest Islamic fashion brands',
        'conditions': [
            'Clothing covers awrah',
            'Female models only for female audiences',
            'Reasonable pricing (not extreme luxury)',
            'Purpose is modest beauty, not seduction'
        ],
        'companies': 'List Islamic modest fashion brands with jobs'
    }
}

**Cattegory 3:** Social Media and Tech Companies
**Issue:** Platforms host both halal and haram content
**Aseesment:**
Factors:
- Company's content moderation policy
P- ercentage of inappropriate content
- Your specific role (creating haram content vs. infrastructure)
- Company's effort to limit harm

Scholarly Guidance:
Generally Permissible If:
- Your role is neutral (software engineering, infrastructure)
- You're not directly creating/promoting haram content
- Company makes reasonable effort to moderate
- Platform serves legitimate purposes beyond haram uses

Problematic If:
- Company specifically promotes inappropriate content
- No content moderation
- Your role is marketing haram content
**Implementation:**
def assess_tech_company(company):
    """
    Tech companies need case-by-case assessment
    """
    
    factors = {
        'content_policy': company.has_strong_moderation_policy,
        'user_base_purpose': company.primary_use_case,  # Professional, educational, entertainment
        'role_neutrality': user_role_is_infrastructure_not_content,
        'company_values': company.publicly_supports_harmful_content
    }
    
    if company.name in ['Facebook', 'Google', 'Amazon', 'Microsoft']:
        return {
            'status': 'Generally Permissible',
            'reasoning': 'Large tech companies serve many legitimate purposes (education, business, communication)',
            'condition': 'Your specific role should not be creating/promoting haram content',
            'note': 'These platforms host some inappropriate content, but also massive amounts of beneficial content',
            'scholar_reference': 'Most contemporary scholars permit working at major tech companies in neutral roles'
        }
    
    elif company.specifically_adult_content:
        return {
            'status': 'HARAM',
            'reasoning': 'Platform specifically designed for inappropriate content'
        }
    
    else:
        return {
            'status': 'Needs Individual Assessment',
            'questions_to_ask': [
                'What is your specific role?',
                'What is platform\'s primary purpose?',
                'Does company have content moderation?',
                'Are you directly facilitating haram content?'
            ]
        }


### Modern Employment Types

**Freelancing & Gig Economy:**  
**Question:** Are freelancing and gig economy jobs Islamically permissible?
**Answer** : YES, with conditions
**Islamic Principles::** 
- Work is clearly defined (no gharar)
- Payment agreed upon upfront
- Both parties fulfill obligations
- Work itself is halal
**Freelancing Assessment:** 
def assess_freelance_work():
    """
    Freelancing is halal with proper contracts
    """
    
    return {
        'islamic_status': 'HALAL',
        'conditions': [
            'Clear contract defining deliverables',
            'Agreed-upon payment amount',
            'Specified deadline',
            'Mutual consent'
        ],
        
        'advantages_for_muslims': [
            'Flexibility for prayer times',
            'Work from home (easier for hijab-wearing sisters)',
            'Control over clients (can reject haram projects)',
            'Multiple income streams (diversification)'
        ],
        
        'islamic_guidelines': {
            'be_honest': 'Don\'t over-promise or deceive about skills',
            'deliver_quality': 'Excellence (ihsan) is Islamic',
            'meet_deadlines': 'Fulfilling contracts is obligation',
            'fair_pricing': 'Don\'t undercharge (harms industry) or overcharge (exploitation)'
        },
        
        'halal_freelance_platforms': [
            'Upwork (general, filter for halal projects)',
            'Fiverr (general, avoid haram gigs)',
            'Bahr.careers (Islamic freelancing platform)',
            'Rizq (we list freelance opportunities with halal verification)'
        ],
        
        'projects_to_avoid': [
            'Designing alcohol brand logos',
            'Writing content for dating apps',
            'Developing gambling websites',
            'Any work supporting haram industries'
        ]
    }
**Gig Economy:** 
def assess_gig_economy_work():
    """
    Gig economy jobs assessment
    """
    
    return {
        'generally_permissible': [
            {
                'job': 'Uber/Lyft Driver',
                'status': 'HALAL',
                'conditions': [
                    'Don\'t accept rides to/from bars/clubs (facilitating alcohol)',
                    'Maintain modesty in vehicle',
                    'Don\'t play inappropriate music',
                    'Drive safely (preserving life is obligation)'
                ],
                'note': 'Some drivers set app to avoid nightlife areas'
            },
            
            {
                'job': 'Deliveroo/UberEats',
                'status': 'HALAL with caution',
                'issue': 'You may deliver alcohol or pork',
                'scholarly_opinions': {
                    'stricter': 'Avoid if alcohol delivery is significant portion',
                    'moderate': 'Permissible if you can reject alcohol orders or they\'re minority of deliveries',
                    'practical': 'Many drivers don\'t have choice - permissible out of necessity'
                },
                'recommendation': 'If possible, opt out of alcohol deliveries in app settings'
            },
            
            {
                'job': 'Amazon Flex / Delivery',
                'status': 'HALAL',
                'note': 'General package delivery - no issues unless you know specific package contains haram item (rare)'
            },
            
            {
                'job': 'TaskRabbit / Handyman Services',
                'status': 'HALAL',
                'conditions': [
                    'Tasks themselves must be halal',
                    'Refuse jobs like setting up bar equipment',
                    'Maintain hijab/modesty in clients\' homes'
                ]
            }
        ],
        
        'general_guidance': {
            'flexibility': 'Gig economy allows Muslims to control what jobs they accept',
            'necessity_principle': 'If this is your only income option, scholars are more lenient',
            'actively_seek_better': 'Use gig work as temporary while seeking full-time halal employment',
            'dua': 'Make dua for halal provision that doesn\'t involve any doubt'
        }
    }
**Remote Work:** 
def assess_remote_work():
    """
    Remote work from Islamic perspective
    """
    
    return {
        'islamic_status': 'HALAL (and often advantageous)',
        
        'advantages_for_muslims': [
            'Prayer at proper times without workplace stress',
            'Easier for sisters to maintain hijab/modesty',
            'Avoid mixed-gender office environment (for those who prefer)',
            'Flexibility for Ramadan, Eid, Jumu\'ah',
            'Family time and work-life balance'
        ],
        
        'islamic_work_ethics_apply': [
            'Fulfill work hours honestly (don\'t slack off)',
            'Deliver quality work (ihsan)',
            'Be available during agreed hours',
            'Meet deadlines',
            'Honest communication with employer'
        ],
        
        'challenge': {
            'issue': 'Discipline and self-management',
            'solution': 'Structure day around prayer times, use salah as work breaks',
            'hadith': 'The Prophet ﷺ: "Allah loves that when one of you does something, he does it with excellence." (Bayhaqi)'
        },
        
        'ideal_remote_jobs_for_muslims': [
            'Software development',
            'Digital marketing',
            'Content writing (halal topics)',
            'Customer service',
            'Data entry/analysis',
            'Graphic design (halal projects)',
            'Online teaching'
        ]
    }


### Halal Verification Checklist for Platform

**Criteria from research translated into verification system:**  
- [ ] No riba involvement
- [ ] No haram products
- [ ] Fair wages and treatment
- [ ] Transparent contract terms
- [ ] [More from research]

---

#

## PART 7: CONTEMPORARY APPLICATIONS

### Charging for Islamic Software

**Question:** Is it halal to charge for apps that help with religious obligations?  
**Research Findings:** [From Research Claude]  
**Application to Mizaan/Rizq:** [Business model decisions based on findings]

### Freemium Model

**Islamic Perspective:** [From research]  
**Recommended Approach:** [Free core features for empowerment, paid advanced features]

### Data Privacy

**Islamic Ethics:** [From research - trust, honesty, protection of others' information]  
**Platform Policy:** [How user data is handled - no selling, minimal collection, etc.]

### Advertising

**Halal Advertising Criteria:** [From research]  
**Platform Stance:** [Ads vs. subscriptions decision with Islamic reasoning]

---

## PART 8: SCHOLARLY RESOURCES

### Classical Sources
- [Books/scholars from research]
- Imam Al-Ghazali: Ihya Ulum al-Din
- [Others from research]

### Contemporary Scholars on Islamic Finance
- [Names from research]
- Dr. Muhammad Akram Nadwi
- [Others from research]

### Fiqh Councils Consulted
- AAOIFI (Accounting and Auditing Organization for Islamic Financial Institutions)
- European Council for Fatwa and Research (ECFR)
- [Others from research]

### Recommended Reading
- [Books/resources from research]

### API Sources for Nisab Calculation
- [Gold/silver price APIs from research]
- Kitco.com API
- [Others from research]


## PART 9: CONTEMPORARY WORK ISSUES
Issue 1: Working for Non-Muslim Companies
Question: Is it permissible to work for non-Muslim-owned companies?
Answer: YES - Scholars unanimously permit this

Evidence:

Prophet Muhammad ﷺ worked for non-Muslim Khadijah (RA) before her conversion
Many Companions worked for non-Muslims in trade
Islam judges the WORK, not the owner's religion

Conditions:

The work itself must be halal
You're not forced to do haram acts
You can practice your religion (pray, hijab, etc.)

Implementation:
def assess_non_muslim_employer(employer):
    """
    Non-Muslim ownership is not disqualifying factor
    Focus on work itself and religious accommodation
    """
    
    return {
        'ruling': 'Permissible to work for non-Muslim company',
        'evidence': 'Prophet ﷺ worked for Khadijah before her Islam',
        
        'what_matters': [
            'Is the WORK halal? (not owner\'s religion)',
            'Can you practice Islam freely?',
            'Are you respected as Muslim employee?'
        ],
        
        'religious_accommodation_check': {
            'prayer_breaks': 'Can you take brief breaks for salah?',
            'friday_jummah': 'Can you attend Jumu\'ah (even if using lunch break)?',
            'hijab': 'Is hijab permitted? (UK law protects this)',
            'beard': 'Is beard permitted? (Islamic right for men)',
            'ramadan': 'Is fasting respected? (flexibility for iftar timing?)',
            'eid': 'Can you take Eid as holiday?'
        },
        
        'green_flags': [
            'Company explicitly welcomes diversity',
            'Has Muslim employees already',
            'Shows respect for religious practices',
            'No pressure to compromise Islamic values'
        ],
        
        'red_flags': [
            'Company discriminates against Muslims',
            'Forces participation in haram activities',
            'Mocks or disrespects Islam',
            'Prohibits prayer or hijab (illegal in UK)'
        ],
        
        'message_to_users': 'Working for non-Muslim company is absolutely halal. Focus on whether the WORK is halal and you\'re treated respectfully.'
    }

Issue 2: Mixed-Gender Workplaces
Question: Can I work in mixed-gender environment?
Answer: YES, with Islamic guidelines
Scholarly Consensus:

Mixed-gender work is permissible (necessity of modern economy)
Must maintain Islamic boundaries (no khalwah, no inappropriate interaction)
Men and women should interact professionally for work purposes

Guidelines:
def mixed_gender_workplace_guidelines():
    """
    Islamic etiquette for mixed workplaces
    """
    
    return {
        'permissibility': 'Scholars permit mixed-gender workplaces with Islamic boundaries',
        
        'evidence': [
            'Women in early Islam engaged in trade, nursing, teaching',
            'Sahabiyat (female Companions) worked in markets',
            'Prophet ﷺ himself employed women (Rufay dah bint Saad as nurse)'
        ],
        'islamic_boundaries': {
        'no_khalwah': {
            'rule': 'No seclusion (being alone) with non-mahram opposite gender',
            'application': 'Avoid closed-door one-on-one meetings. Keep door open or have third person present',
            'modern_note': 'Video calls with others present or door open also apply'
        },
        
        'lower_gaze': {
            'rule': 'Guard your gaze - don\'t stare at opposite gender',
            'application': 'Professional eye contact is fine, but avoid lingering looks',
            'quran': '24:30-31 - Tell believing men and women to lower their gaze'
        },
        
        'professional_interaction': {
            'rule': 'Interact for work purposes professionally',
            'allowed': 'Work discussions, meetings, emails, collaborations',
            'avoid': 'Personal conversations, flirting, unnecessary socializing'
        },
        
        'appropriate_dress': {
            'for_sisters': 'Hijab and modest clothing as per Islamic guidelines',
            'for_brothers': 'Cover awrah (navel to knee minimum), avoid tight/revealing clothes',
            'uk_law': 'Employers MUST accommodate hijab - it\'s protected religious right'
        },
        
        'avoid_unnecessary_touch': {
            'rule': 'No physical contact with non-mahram opposite gender',
            'handshake': 'Scholars differ - many say avoid, some permit if refusing causes harm',
            'alternative': 'Smile, nod, or place hand on heart as greeting',
            'explain_politely': '"I don\'t shake hands for religious reasons, but it\'s nice to meet you"'
        }
    },
    
    'practical_scenarios': {
        'meetings': {
            'situation': 'Mixed-gender team meetings',
            'guidance': 'Completely permissible - work-related discussion with multiple people',
            'maintain': 'Professional demeanor, modest dress, appropriate gaze'
        },
        
        'one_on_one_meeting': {
            'situation': 'Boss requests private meeting (opposite gender)',
            'guidance': 'Keep door open, request meeting in glass-walled room, or have colleague nearby',
            'if_unavoidable': 'Most scholars permit if genuinely for work and no inappropriate conversation/behavior'
        },
        
        'business_travel': {
            'situation': 'Work trip with opposite gender colleagues',
            'guidance': 'Separate hotel rooms (obvious), avoid being alone during travel',
            'meals': 'Group meals fine, avoid one-on-one dinners'
        },
        
        'office_social_events': {
            'situation': 'Company parties, happy hours',
            'guidance': [
                'Avoid events at bars/clubs (alcohol environment)',
                'Attend halal events (lunch, coffee, team activities)',
                'You can socialize with colleagues in group settings'
            ]
        }
    },
    
    'for_sisters_specifically': {
        'hijab_at_work': 'Your right - UK law protects it. Employer cannot discriminate.',
        'if_pressured': 'Contact ACAS or Muslim employment lawyers',
        'confidence': 'Wear hijab with confidence - it\'s identity and faith',
        'prophet_example': 'Prophet ﷺ\'s wives and daughters were role models in modesty'
    },
    
    'for_brothers_specifically': {
        'beard': 'Your right if part of religious practice. Employers must reasonably accommodate.',
        'professionalism': 'Maintain professional boundaries. You represent Islam to colleagues.',
        'avoid_assumptions': 'Don\'t assume you can\'t work with women - Islam permits professional interaction'
    }
    **Feature: Workplace Islam Scenarios - Q&A:**

def workplace_islam_qa():
    """
    Common questions Muslims face in mixed workplaces
    """
    
    return {
        'title': 'Navigating Mixed-Gender Workplace: Islamic Q&A',
        
        'questions': [
            {
                'q': 'My female boss wants to shake hands. What do I do?',
                'a': 'Politely decline with smile: "I don\'t shake hands for religious reasons, but lovely to meet you." Most people understand. If she\'s offended, calmly explain Islamic boundary. UK law protects your religious practice.',
                'scholar_note': 'Some scholars permit if refusal causes severe hardship (losing job), but better to explain politely first.'
            },
            
            {
                'q': 'I\'m the only hijabi in office. Feeling self-conscious.',
                'a': 'Your hijab is identity and obedience to Allah. Many hijabis report colleagues respect it once they see your professionalism. Let your work speak. You\'re representing Islam beautifully.',
                'encouragement': 'Sahabiyat wore hijab in markets and work. You\'re following their example.'
            },
            
            {
                'q': 'Colleague keeps flirting with me. How to handle Islamically?',
                'a': 'Set clear professional boundary: "I prefer to keep relationships at work strictly professional." If continues, this is harassment - report to HR. Islam doesn\'t require you to tolerate inappropriate behavior.',
                'uk_law': 'Sexual harassment is illegal. You have legal right to safe workplace.'
            },
            
            {
                'q': 'Boss scheduled important meeting during Jumu\'ah time.',
                'a': 'Explain: "I have religious obligation on Fridays 1-2pm. Can we move meeting to before/after?" Most employers accommodate. If refused, this may be religious discrimination (illegal in UK).',
                'prophet_example': 'Quran 62:9 - When call to Jumu\'ah is made, leave trade and go to prayer. Your obligation is clear.'
            },
            
            {
                'q': 'Company retreat includes alcohol and mixed swimming. Must I attend?',
                'a': 'Attend halal portions (team building, meals) but skip haram activities. Explain: "I can\'t participate in this activity for religious reasons, but I\'m happy to join the team for [halal alternative]." Offer alternatives.',
                'balance': 'Be part of team, but within Islamic boundaries.'
            },
            
            {
                'q': 'Working remotely. Colleague (opposite gender) wants to do video calls constantly. Appropriate?',
                'a': 'Video calls for work purposes are fine, but if they\'re excessive or personal in nature, set boundary. Keep conversations professional. If it feels like khalwah (seclusion) energy, suggest group calls instead.',
                'principle': 'Assess intention and content, not just format.'
            }
        ]
    }
}

Issue 3: Companies with Partial Haram Operations
Question: Can I work for a company that has SOME haram activities mixed with halal?
Example: Supermarket that sells alcohol and pork alongside groceries
Scholarly Opinions:
Opinion 1 (Stricter):

Avoid entirely if company has any haram revenue stream
Supporting the company indirectly supports haram

Opinion 2 (Moderate - Majority Contemporary View):

Permissible if:

Haram portion is MINOR (<5-10% of revenue)
Your role doesn't directly facilitate the haram portion
Halal alternatives are limited in your area
You actively seek fully halal employment



Opinion 3 (Lenient):

Permissible as long as YOUR SPECIFIC ROLE is not handling haram items
Company's overall operations don't affect permissibility of your halal role

Rizq Platform Approach:
def assess_mixed_operations_company(company, user_role):
    """
    Nuanced assessment of companies with mixed halal/haram operations
    """
    
    # Calculate haram revenue percentage
    haram_percentage = calculate_haram_revenue_percentage(company)
    
    # Check user's direct involvement
    direct_involvement = user_role_directly_handles_haram(user_role, company)
    
    if direct_involvement:
        return {
            'halal_status': 'HARAM',
            'reason': 'Your role directly handles haram items/services',
            'example': 'Bartender in restaurant that serves alcohol',
            'ruling': 'Direct involvement in haram is prohibited regardless of company\'s overall operations',
            'alternative': 'Seek role in same company that doesn\'t handle haram, or different company'
        }
    
    elif haram_percentage > 50:
        return {
            'halal_status': 'HARAM',
            'reason': 'Company\'s primary business is haram',
            'example': 'Restaurant where alcohol sales are majority of revenue',
            'ruling': 'Even indirect roles support primarily haram business',
            'alternative': 'Find company where halal is primary business'
        }
    
    elif haram_percentage > 10:
        return {
            'halal_status': 'QUESTIONABLE',
            'reason': f'{haram_percentage:.1f}% of company revenue from haram sources',
            'scholarly_differences': {
                'stricter': 'Avoid any company with haram revenue',
                'moderate': 'Permissible if <33% haram and your role is separate',
                'lenient': 'Permissible as long as YOUR role is halal'
            },
            'your_role': user_role.title,
            'role_assessment': 'Your role appears to be in halal portion of business',
            'recommendation': 'Consult scholar. Consider this temporary while seeking fully halal alternative.',
            'better_option': f'We have {count_fully_halal_alternatives(company.industry)} fully halal alternatives in your field'
        }
    
    elif haram_percentage > 0:
        return {
            'halal_status': 'PERMISSIBLE with minor concern',
            'reason': f'Only {haram_percentage:.1f}% of company revenue from haram (minor portion)',
            'scholarly_view': 'Most contemporary scholars permit when haram is truly minor and your role is separate',
            'conditions': [
                'Your role does not directly handle haram items',
                'You continue seeking fully halal alternatives',
                'You maintain Islamic boundaries in workplace'
            ],
            'example': 'Working as accountant for supermarket that sells <5% alcohol',
            'encouragement': 'This is permissible, though seeking 100% halal company is ideal'
        }
    
    else:
        return {
            'halal_status': 'HALAL ✓',
            'reason': 'Company operates entirely within halal parameters',
            'encouragement': 'Alhamdulillah! This is the ideal scenario.',
            'make_dua': 'May Allah increase such companies and opportunities'
        }
         
 Real Example - Tesco:
 def tesco_example():
    """
    Real-world example: Can Muslim work at Tesco?
    """
    
    return {
        'company': 'Tesco (UK Supermarket)',
        'haram_elements': 'Sells alcohol (~3-5% of revenue), pork products',
        'halal_elements': 'Groceries, halal meat, household items (95%+ of business)',
        
        'roles_assessment': {
            'checkout_cashier': {
                'status': 'QUESTIONABLE',
                'issue': 'Will scan alcohol/pork items',
                'scholarly_differences': {
                    'stricter': 'Avoid - you\'re facilitating haram purchase',
                    'moderate': 'Permissible if: (1) No alternative job available, (2) Alcohol is minor part of transactions, (3) You don\'t approve/encourage the purchase, just scan as duty',
                    'lenient': 'Permissible - you\'re not selling alcohol, just processing transaction like machine'
                },
                'rizq_recommendation': 'Mark as "consult scholar" - user decides based on their madhab and necessity'
            },
            
            'shelf_stocker': {
                'status': 'QUESTIONABLE',
                'issue': 'May stock alcohol/pork sections',
                'solution': 'Many Muslim employees request to stock other aisles only',
                'rizq_recommendation': 'Permissible if employer allows you to avoid alcohol/pork sections'
            },
            
            'warehouse_worker': {
                'status': 'QUESTIONABLE',
                'issue': 'May handle boxes containing alcohol/pork',
                'scholarly_view': 'More lenient than direct sales - you\'re moving boxes, not selling items',
                'rizq_recommendation': 'Generally permissible, though avoiding alcohol section is better'
            },
            
            'office_roles': {
                'examples': 'Accountant, IT, HR, Marketing',
                'status': 'PERMISSIBLE',
                'reasoning': 'Your role is in halal portion (general operations). You\'re not directly involved in alcohol/pork',
                'scholarly_consensus': 'Most scholars permit indirect roles in companies where haram is minor (<10%)',
                'rizq_recommendation': '✓ Halal - Your role is separate from haram elements'
            },
            
            'management': {
                'status': 'QUESTIONABLE',
                'issue': 'May oversee alcohol/pork departments',
                'assessment': 'Depends on specific responsibilities. If you manage alcohol section = problematic. If you manage produce section = fine.',
                'rizq_recommendation': 'Case-by-case assessment needed'
            }
        },
        
        'general_guidance': {
            'necessity_factor': 'If Tesco is your only realistic employment option, scholars are more lenient',
            'actively_seek_better': 'Work there if needed, but keep seeking fully halal employment',
            'request_accommodation': 'Many Muslim Tesco employees successfully request to avoid alcohol sections',
            'legal_protection': 'UK Equality Act protects your right to religious accommodation (within reason)'
        },
        
        'fully_halal_alternatives': [
            'Halal supermarkets',
            'Fully halal online retailers',
            'Islamic bookstores',
            'Muslim-owned businesses'
        ]
    }

Issue 4: Student Loans and Interest
Question: I need student loan to study. Is this haram? If I take it, can I work to pay it back?
Scholarly Opinions:
Majority (Permanent Council, Saudi Scholars):

Student loans with interest are haram
Avoid at all costs
Seek scholarships, work-study, family support instead

European Council for Fatwa and Research:

Interest is haram in principle
However, in non-Muslim countries where:

Higher education is nearly impossible without loans
Degree significantly improves earning capacity
No realistic interest-free alternative


Then student loans are permitted under principle of necessity (darurah)
Conditions: Take minimum needed, pay back quickly, seek halal alternatives

Rizq Platform Guidance:
def student_loan_guidance():
    """
    Guidance on student loans for Muslims
    """
    
    return {
        'islamic_ruling': 'Interest is haram in principle',
        'quran': '2:275 - Allah has permitted trade and forbidden interest',
        
        'necessity_exemption': {
            'european_council_fatwa': 'Student loans permitted under necessity (darurah) if:',
            'conditions': [
                'Education is essential for career',
                'No interest-free alternative available',
                'No family support possible',
                'Degree will lead to significantly better halal employment',
                'You take minimum amount needed',
                'You intend to pay back as quickly as possible'
            ],
            'note': 'This is rukhsah (exemption), not ideal. Ideal is interest-free.'
        },
        
        'better_alternatives': {
            'scholarships': 'Apply extensively - many don\'t require payback',
            'grants': 'Government and university grants (free money)',
            'work_study': 'Part-time work while studying',
            'family_loans': 'Interest-free loan from family/community',
            'islamic_microfinance': 'Some Islamic organizations offer interest-free education loans',
            'cheaper_education': 'Community college then transfer, online degrees, apprenticeships'
        },
        
        'if_you_already_have_student_loan': {
            'working_to_pay_it_back': {
                'status': 'PERMISSIBLE',
                'reasoning': 'The haram was taking the loan. Paying it back through halal work is obligation.',
                'priority': 'Pay it back as fast as possible to be free from riba',
                'dont_overthink': 'Focus energy on halal earning and rapid payoff, not guilt'
            },
            
            'repayment_strategy': [
                'Prioritize loan payoff over non-essential spending',
                'Make extra payments when possible',
                'Avoid consolidation if it extends term/increases interest',
                'Make dua for Allah to help you become debt-free'
            ],
            
            'spiritual_approach': {
                'tawbah': 'If you took loan without knowing ruling, make tawbah (repentance)',
                'sadaqah': 'Give extra charity to purify wealth',
                'dua': 'O Allah, free me from this debt and make my provision purely halal',
                'future': 'Commit to avoiding interest-based transactions in future'
            }
        }
    }

Issue 5: Ethical Dilemmas - When Employer Asks You to Do Haram
Scenario: Your halal-sector employer asks you to lie to client, manipulate data, or compromise ethics
Islamic Ruling: Obedience to creation cannot involve disobedience to the Creator
Hadith:
"There is no obedience to anyone if it involves disobedience to Allah. Obedience is only in what is right and good." (Sahih al-Bukhari 7257)
Implementation:
def handle_unethical_request(request_from_employer):
    """
    Islamic guidance when employer asks you to compromise ethics
    """
    
    return {
        'principle': 'No obedience to creation in disobedience to Creator',
        'hadith': 'Bukhari 7257',
        
        'prohibited_requests': [
            'Lying to clients/customers',
            'Falsifying documents/data',
            'Fraud or embezzlement',
            'Harassment or discrimination',
            'Covering up wrongdoing',
            'Cheating or deceptive practices',
            'Breaking laws'
        ],
        
        'response_levels': {
            'level_1_polite_refusal': {
                'when': 'First request or minor issue',
                'how': '"I\'m not comfortable with this approach. Can we find an ethical alternative?"',
                'tone': 'Professional, not preachy',
                'offer_alternative': 'Suggest halal way to achieve same goal'
            },
            
            'level_2_firm_refusal': {
                'when': 'Repeated requests or serious ethical breach',
                'how': '"I cannot do this as it violates my ethical/religious principles. I\'m happy to find another solution, but I cannot participate in this."',
                'document': 'Keep written record of refusal (email)',
                'legal': 'UK law protects whistleblowers'
            },
            
            'level_3_escalation': {
                'when': 'Employer retaliates or insists',
                'how': 'Report to HR, legal department, or external regulators',
                'protection': 'UK law prohibits retaliation against whistleblowers',
                'islamic_principle': 'Preventing wrongdoing is obligation'
            },
            
            'level_4_resignation': {
                'when': 'Company culture is systematically unethical',
                'how': 'Resign with dignity. Don\'t compromise deen for dunya.',
                'hadith': 'Prophet ﷺ: "Leave what makes you doubt for what does not make you doubt." (Tirmidhi)',
                'trust_allah': 'Allah will provide better opportunity when you choose His path',
                'rizq_platform': 'We\'ll help you find ethical employer'
            }
        },
        
        'financial_concern': {
            'worry': 'But I need this job for income!',
            'islamic_response': [
                'Allah is Ar-Razzaq (The Provider) - He will provide when you choose halal',
                'Compromising deen for dunya is never worth it',
                'Barakah in halal income, even if less. No barakah in haram, even if more',
                'Hadith: "Whoever gives up something for sake of Allah, Allah will compensate him with something better." (Ahmad)'
            ],
            'practical': 'Start job search immediately. Don\'t wait until situation is unbearable.'
        },
        
        'success_stories': [
            {
                'scenario': 'Asked to lie to client about product capabilities',
                'choice': 'Refused. Suggested honest approach.',
                'outcome': 'Client respected honesty. Eventually promoted for integrity.',
                'lesson': 'Doing right thing often leads to worldly success too'
            },
            {
                'scenario': 'Boss wanted to falsify expense reports',
                'choice': 'Refused. Reported to compliance.',
                'outcome': 'Boss was fired. Company thanked employee for whistleblowing.',
                'lesson': 'Standing for truth protects you and others'
            },
            {
                'scenario': 'Employer culture systematically unethical',
                'choice': 'Resigned despite financial worry.',
                'outcome': 'Found better company through Rizq within 6 weeks. Higher salary, ethical environment.',
                'lesson': 'Allah replaced haram income with better halal income'
            }
        ]
    }

## METHODOLOGY NOTES

### Source Hierarchy

1. **Quran** (direct divine revelation)
2. **Authentic Hadith** (Sahih > Hasan > Da'if)
3. **Scholarly Consensus (Ijma')**
4. **Analogical Reasoning (Qiyas)** for modern issues
5. **Contemporary Fatawa** from recognized councils

### When Opinions Differ

- Present majority view clearly
- Note significant alternative opinions
- Explain evidence for each position
- Choose most cautious/beneficial approach for users
- Disclose differences transparently

### Validation Process

- All research from Research Specialist reviewed
- Cross-referenced with multiple sources
- Contemporary applications verified with fiqh councils
- Local imam consultation for final validation [planned]
- Continuous updates as new research emerges

---

## REFLECTION

This is not just a reference document. Every algorithm, every feature, every user message in Mizaan and Rizq must trace back to authentic Islamic scholarship documented here.

**This research transforms:**
- Expense categorization → Implementation of Quranic balance command (25:67)
- Zakat calculation → Fulfillment of obligatory pillar of Islam
- Job listings → Facilitation of dignified halal provision (67:15)
- Empowerment focus → Application of Islamic charity philosophy
- Business model → Alignment with Islamic economic ethics

**We're not building apps. We're implementing divine guidance in code.**

---

CONCLUSION: Rizq Platform's Unique Value Proposition

def rizq_platform_differentiation():
    """
    What makes Rizq different from other job platforms
    """
    
    return {
        'title': 'Why Rizq? Islamic Job Platform That Understands You',
        
        'unique_features': {
            'halal_verification': {
                'feature': 'Every job listing verified for Islamic permissibility',
                'how': 'We don\'t just post any job. Each listing assessed against Quran, Sunnah, scholarly consensus.',
                'categories': 'Jobs marked as: ✓ Halal, ⚠️ Questionable (consult scholar), or ✗ Haram (removed)',
                'peace_of_mind': 'You don\'t have to guess. We\'ve done the research.'
            },
            
            'islamic_framing': {
                'feature': 'Job search framed as Islamic obligation and worship',
                'motivation': 'When rejections come, remember: you\'re obeying Allah\'s command to seek provision (67:15)',
                'dua_reminders': 'Daily dua prompts for halal rizq',
                'quranic_encouragement': 'Ayat and hadith reminders throughout your journey'
            },
            
            'ethical_employers_only': {
                'feature': 'Only companies committed to ethical treatment listed',
                'verification': 'We check: payment reliability, workplace dignity, religious accommodation',
                'muslim_reviews': 'See what Muslim employees say about working there',
                'hadith_standard': 'Employers must meet prophetic standard: "Workers are your brothers"'
            },
            
            'comparison_detox': {
                'feature': 'NO toxic comparison culture',
                'no_leaderboards': 'We don\'t rank users or create competition',
                'no_salary_showing_off': 'Your provision is between you and Allah',
                'quranic_basis': 'Quran 4:32 - Don\'t wish for what Allah gave others'
            },
            
            'empowerment_focus': {
                'feature': 'Goal is moving you from "lower hand" to "upper hand"',
                'free_training': 'Skills courses to increase employability',
                'mentorship': 'Successful Muslims mentor job seekers',
                'entrepreneurship': 'Support for halal business startups',
                'hadith': 'Upper hand (giving) is better than lower hand (receiving)'
            },
            
            'community_not_competition': {
                'feature': 'Other Muslims are your brothers/sisters, not competitors',
                'referrals': 'Employed users refer job seekers to their companies',
                'testimonials': 'Success stories to inspire, not trigger envy',
                'dua_for_each_other': 'Make dua for fellow Muslims\' success',
                'hadith': 'None of you believes until he loves for his brother what he loves for himself'
            }
        },
        
        'vs_other_platforms': {
            'linkedin': {
                'their_model': 'Professional networking, heavy social comparison, no religious consideration',
                'missing': 'Halal job verification, Islamic motivation, ethical screening',
                'triggers': 'Comparison anxiety, imposter syndrome, "everyone else is succeeding"'
            },
            
            'indeed': {
                'their_model': 'Job aggregator, neutral on ethics',
                'missing': 'Halal verification, employer ethics screening, religious accommodation info',
                'issue': 'You have to manually filter out haram jobs'
            },
            
            'rizq': {
                'our_model': 'Islamic job platform - every feature serves Allah and serves you',
                'guarantees': [
                    '✓ Every job is halal-verified',
                    '✓ Every employer is ethically screened',
                    '✓ Your job search is framed as worship',
                    '✓ Your provision journey is supported with dua and guidance',
                    '✓ Your success helps the next Muslim (empowerment cycle)'
                ],
                'mission': 'Connecting Muslims with halal rizq while protecting their faith',
                'vision': 'Ummah where every Muslim has dignified, halal employment'
            }
        },
        
        'call_to_action': {
            'job_seekers': 'Join Rizq. Seek provision the halal way, with Islamic support.',
            'employers': 'List your jobs. Attract talented Muslims who value ethics and excellence.',
            'employed_muslims': 'Mentor job seekers. Refer them to your company. Be the "upper hand" helping others rise.',
            'investors': 'Support a platform that serves Allah and serves the ummah.',
            'everyone': 'Make dua for Rizq\'s success. May Allah make it means of halal provision for millions.'
        }
    }

PART 3: CROSS-CUTTING RESEARCH
Economic Justice, Technology Ethics & Business Models

9. ECONOMIC JUSTICE PRINCIPLES IN ISLAM
9.1 Fair Measurement and Pricing
Quranic Foundation: Surah Al-Mutaffifin (83:1-3)
Arabic:
وَيْلٌ لِّلْمُطَفِّفِينَ ‎﴿١﴾‏ ٱلَّذِينَ إِذَا ٱكْتَالُوا۟ عَلَى ٱلنَّاسِ يَسْتَوْفُونَ ‎﴿٢﴾‏ وَإِذَا كَالُوهُمْ أَو وَّزَنُوهُمْ يُخْسِرُونَ ‎﴿٣﴾
Translation (Sahih International):
"Woe to those who give less [than due], who, when they take a measure from people, take in full. But if they give by measure or by weight to them, they cause loss."
Context:
Revealed in Makkah addressing Arab merchants who would use two different measurement standards: accurate when receiving goods, but short-changing when selling. This is one of the strongest condemnations in the Quran - the entire surah is named after this sin.
Additional Evidence:
Surah Al-An'am 6:152:
"And give full measure and weight in justice..."
Surah Al-Isra 17:35:
"And give full measure when you measure, and weigh with an even balance. That is the best [way] and best in result."
Hadith:
"The Prophet ﷺ passed by a pile of food in the market. He put his hand inside it and felt moisture [indicating the seller had hidden poor quality goods beneath good ones]. He said, 'What is this, O owner of the food?' He said, 'O Messenger of Allah, it was struck by rain.' He said, 'Why did you not put it on top of the food so that people could see it? Whoever cheats is not one of us.'" (Sahih Muslim 102)
Application to Modern Business:
For Mizaan (Spending Tracker):
class FairPricingDetector:
    """
    Help users identify when they're being cheated
    Implements Quran 83:1-3's condemnation of unfair measurement
    """
    
    def detect_unfair_pricing(self, purchase):
        """
        Alert users to potential price manipulation
        """
        
        red_flags = []
        
        # 1. Hidden fees (modern equivalent of hiding wet grain)
        if purchase.has_hidden_fees:
            actual_cost = purchase.advertised_price + purchase.hidden_fees
            hidden_percentage = (purchase.hidden_fees / actual_cost) * 100
            
            if hidden_percentage > 10:
                red_flags.append({
                    'type': 'hidden_fees',
                    'severity': 'HIGH',
                    'message': f'Advertised as £{purchase.advertised_price}, but total is £{actual_cost}',
                    'islamic_issue': 'This resembles the deception condemned in Quran 83:1-3',
                    'ayah': 'Quran 83:1-3 - Woe to those who give less than due',
                    'action': 'Avoid businesses that hide costs. Support transparent merchants.'
                })
        
        # 2. Shrinkflation (giving less for same price)
        if purchase.product_has_shrinkflation_history:
            red_flags.append({
                'type': 'shrinkflation',
                'message': f'This product was {purchase.old_size} but is now {purchase.new_size} at same price',
                'islamic_issue': 'Reducing quantity while maintaining price is form of "giving less" (83:1)',
                'transparency': 'Halal if clearly labeled. Haram if hidden.',
                'action': 'Check product sizes. Calculate price per unit.'
            })
        
        # 3. Bait and switch
        if purchase.is_bait_and_switch:
            red_flags.append({
                'type': 'bait_and_switch',
                'severity': 'CRITICAL',
                'message': 'Advertised item unavailable, pushed toward expensive alternative',
                'islamic_issue': 'Deceptive trade practice. Prophet ﷺ: "Whoever cheats is not one of us"',
                'action': 'Report to Trading Standards (UK) and avoid this merchant'
            })
        
        # 4. False urgency (fake scarcity)
        if purchase.has_false_urgency_tactics:
            red_flags.append({
                'type': 'false_urgency',
                'message': '"Only 2 left!" or "Sale ends in 1 hour!" but always says this',
                'islamic_issue': 'Lying to pressure customers violates Islamic honesty',
                'hadith': 'Muslim 102 - Whoever cheats is not one of us',
                'action': 'Don\'t be pressured. Legitimate sales don\'t need psychological manipulation.'
            })
        
        if red_flags:
            return {
                'unfair_pricing_detected': True,
                'flags': red_flags,
                'quranic_principle': 'Give full measure and weight in justice (6:152)',
                'user_rights': 'UK Consumer Rights Act 2015 protects you from unfair practices',
                'islamic_encouragement': 'Supporting honest merchants is supporting Islamic values',
                'alternative_suggestion': find_honest_merchants(purchase.category)
            }


For Rizq (Income Platform):
class FairPricingForBusinesses:
    """
    Guidance for Muslim entrepreneurs on ethical pricing
    Implements Quranic justice in business
    """
    
    def ethical_pricing_guidelines(self):
        """
        Help Muslim business owners price fairly
        """
        
        return {
            'quranic_principles': [
                'Give full measure and weight (Quran 6:152)',
                'Do not defraud people of their things (Quran 11:85)',
                'The Prophet ﷺ: "Whoever cheats is not one of us" (Muslim 102)'
            ],
            
            'halal_pricing_practices': {
                'transparency': {
                    'principle': 'All costs should be clear upfront',
                    'examples': [
                        '✓ Clear pricing on website/store',
                        '✓ No hidden fees',
                        '✓ Shipping costs stated before checkout',
                        '✓ Subscription renewals clearly disclosed'
                    ],
                    'avoid': [
                        '✗ Burying fees in fine print',
                        '✗ Revealing total cost only at final step',
                        '✗ Auto-renewal without clear notice'
                    ]
                },
                
                'honest_representation': {
                    'principle': 'Product/service must match description',
                    'examples': [
                        '✓ Accurate product photos',
                        '✓ Honest description of features',
                        '✓ Disclose defects or limitations',
                        '✓ Accurate delivery timeframes'
                    ],
                    'prophet_example': 'Prophet ﷺ exposed the merchant hiding wet grain under dry'
                },
                
                'fair_markup': {
                    'principle': 'Profit is halal, exploitation is haram',
                    'scholarly_guidance': {
                        'reasonable_profit': '10-30% markup is normal in most industries',
                        'exploitation': 'Price gouging during crisis is haram',
                        'monopoly_abuse': 'Charging excessive prices due to monopoly violates justice'
                    },
                    'examples': {
                        'halal': 'Selling product at £50 when cost is £35 (43% markup - reasonable)',
                        'questionable': 'Selling product at £200 when cost is £35 (571% markup - unless luxury brand with legitimate value-add)',
                        'haram': 'Selling water for £10/bottle during natural disaster (exploitation of necessity)'
                    }
                },
                
                'no_deceptive_tactics': {
                    'prohibited': [
                        'Fake countdown timers',
                        'False scarcity ("Only 2 left!" when there are 200)',
                        'Fake reviews or testimonials',
                        'Bait and switch advertising',
                        'Hidden auto-renewals',
                        'Misleading "free trial" that charges without clear notice'
                    ],
                    'islamic_issue': 'All forms of deception violate "Whoever cheats is not one of us"'
                }
            },
            
            'modern_digital_issues': {
                'subscription_traps': {
                    'issue': 'Easy to sign up, deliberately hard to cancel',
                    'islamic_ruling': 'Making cancellation difficult is form of trapping customer - haram',
                    'halal_approach': 'Cancellation should be as easy as sign-up (one click)'
                },
                
                'dark_patterns': {
                    'issue': 'UI designed to trick users (pre-checked boxes, confusing wording)',
                    'islamic_ruling': 'Psychological manipulation to extract money is deception',
                    'halal_approach': 'Clear, honest UI that empowers customer choice'
                },
                
                'shrinkflation': {
                    'issue': 'Reducing product size while maintaining price',
                    'islamic_ruling': 'Halal if clearly disclosed, haram if hidden',
                    'example': 'Chocolate bar was 200g, now 180g at same price. Must clearly show new weight.'
                }
            },
            
            'price_discrimination': {
                'issue': 'Charging different customers different prices',
                'scholarly_views': {
                    'permissible': [
                        'Volume discounts (reward bulk buying)',
                        'Early bird pricing (reward commitment)',
                        'Student/senior discounts (helping those with less means)',
                        'Loyalty rewards (thank repeat customers)'
                    ],
                    'questionable': [
                        'Dynamic pricing based on customer\'s ability to pay (algorithmic price discrimination)',
                        'Charging more in poor neighborhoods (exploitation)'
                    ],
                    'prohibited': [
                        'Racial/religious discrimination in pricing',
                        'Exploiting customer ignorance or vulnerability'
                    ]
                }
            }
        }
9.2 Prohibition of Exploitation
Quranic Foundation:
Surah Hud 11:85:
"And O my people, give full measure and weight in justice and do not deprive the people of their due and do not commit abuse on the earth, spreading corruption."
Hadith Evidence:
The Prophet ﷺ said:
"Do not be envious of one another; do not artificially inflate prices against one another; do not hate one another; do not turn one's back on each other; and do not undercut one another in business transactions. Be, O servants of Allah, brothers." (Sahih Muslim 2564)
Islamic Prohibition of Price Manipulation:
Hadith on Price Controls:
A man came to the Prophet ﷺ during a time when prices were high and said: "O Messenger of Allah, prices have gone up, so fix prices for us." The Prophet ﷺ said: "Allah is the One Who fixes prices, Who withholds, Who gives lavishly, and Who provides, and I hope that when I meet Him, none of you will have a claim against me for an injustice regarding blood or property." (Sunan Abu Dawud 3451, authenticated as Sahih)
Scholarly Understanding:

Free market pricing is default Islamic position
EXCEPT when merchants collude to artificially inflate prices = haram
EXCEPT during crisis when necessities are being hoarded = government may intervene

Application to Modern Economics:
class ProhibitionOfExploitation:
    """
    Islamic prohibitions against economic exploitation
    """
    
    def __init__(self):
        self.prohibited_practices = self.define_prohibited_practices()
    
    def define_prohibited_practices(self):
        """
        Economic practices Islam explicitly prohibits
        """
        
        return {
            'price_fixing': {
                'definition': 'Competitors colluding to set artificially high prices',
                'islamic_ruling': 'HARAM',
                'evidence': 'Muslim 2564 - Do not artificially inflate prices',
                'modern_example': 'Oil companies agreeing to keep gas prices high',
                'legal_status': 'Illegal in most countries (UK Competition Act 1998)',
                'severity': 'Major sin - harms entire community'
            },
            
            'monopolistic_abuse': {
                'definition': 'Exploiting monopoly position to charge excessive prices',
                'islamic_ruling': 'HARAM',
                'evidence': 'Depriving people of their due (11:85)',
                'modern_example': 'Only pharmacy in town charging £50 for medication that costs £5 elsewhere',
                'scholarly_note': 'Monopoly itself isn\'t haram, but exploiting it to harm people is',
                'government_role': 'Islamic state may regulate to prevent exploitation'
            },
            
            'crisis_profiteering': {
                'definition': 'Price gouging during emergencies (natural disasters, pandemics)',
                'islamic_ruling': 'HARAM',
                'evidence': 'Do not commit abuse on earth (11:85)',
                'modern_example': 'Selling bottled water for £20 during flood when cost is £1',
                'severity': 'Exploiting people\'s desperate need - major sin',
                'legal_status': 'Many countries have anti-gouging laws'
            },
            
            'hoarding_necessities': {
                'definition': 'Withholding essential goods to create artificial scarcity and raise prices',
                'islamic_ruling': 'HARAM',
                'hadith': 'The Prophet ﷺ: "Whoever hoards is a sinner." (Muslim 1605)',
                'context': 'Hoarding food during famine to drive up prices',
                'modern_example': 'Buying all hand sanitizer during pandemic to resell at markup',
                'note': 'Normal inventory management is fine. Hoarding to manipulate market is sin.'
            },
            
            'deceptive_advertising': {
                'definition': 'Misleading customers about product quality, features, or benefits',
                'islamic_ruling': 'HARAM',
                'evidence': 'Muslim 102 - Whoever cheats is not one of us',
                'modern_examples': [
                    'Weight loss products with fake before/after photos',
                    'Investment schemes promising unrealistic returns',
                    'Products claiming false health benefits'
                ],
                'digital_age': 'Influencer ads without disclosure = deception'
            },
            
            'predatory_lending': {
                'definition': 'Lending with terms designed to trap borrower in debt',
                'islamic_ruling': 'HARAM (combines riba + exploitation)',
                'modern_example': 'Payday loans with 1000%+ APR targeting desperate people',
                'quranic': 'Quran 2:279 - Allah declares war on those involved in riba',
                'severity': 'Among the worst economic sins in Islam'
            },
            
            'wage_theft': {
                'definition': 'Not paying workers agreed wages or delaying payment',
                'islamic_ruling': 'HARAM - Major sin',
                'hadith': 'The Prophet ﷺ: "Give the worker his wages before his sweat dries." (Ibn Majah 2443)',
                'modern_examples': [
                    'Not paying overtime',
                    'Withholding final paycheck',
                    'Paying below minimum wage',
                    'Misclassifying employees as contractors to avoid benefits'
                ],
                'judgment_day': 'The Prophet ﷺ: "Allah says: \'I will be opponent to three on Day of Judgment, and one of them is a man who hires a worker and does not give him his wages.\'" (Bukhari 2227)'
            },
            
            'planned_obsolescence': {
                'definition': 'Deliberately designing products to fail so customers must repurchase',
                'islamic_ruling': 'Questionable to Haram (scholarly debate)',
                'issue': 'Wastes resources, forces unnecessary spending',
                'quran': '6:141 - Do not commit excess (waste)',
                'examples': [
                    'Phone batteries designed to degrade quickly',
                    'Appliances with programmed failure dates',
                    'Software updates that slow old devices'
                ],
                'scholarly_view': 'Moderate obsolescence (technology advancement) is permissible. Deliberate sabotage to force repurchase is exploitation.'
            }
        }
    
    def detect_exploitation(self, business_practice):
        """
        Flag potentially exploitative practices
        """
        
        for practice_type, details in self.prohibited_practices.items():
            if business_practice matches details['definition']:
                return {
                    'exploitation_detected': True,
                    'type': practice_type,
                    'islamic_ruling': details['islamic_ruling'],
                    'evidence': details['evidence'],
                    'severity': details.get('severity', 'Prohibited'),
                    'action': 'Avoid this business. Report if illegal.',
                    'alternative': 'Support ethical businesses that follow Islamic justice'
                }

For Mizaan Users (Consumers):
def protect_consumers_from_exploitation(user):
    """
    Educate Mizaan users to recognize and avoid exploitation
    """
    
    return {
        'title': 'Protecting Yourself from Economic Exploitation (Islamic Guidance)',
        
        'red_flags': {
            'too_good_to_be_true': {
                'warning': '"Get rich quick" schemes, "guaranteed" returns, "limited time" pressure',
                'islamic_principle': 'Halal wealth comes through honest effort, not shortcuts',
                'prophet_wisdom': 'The Prophet ﷺ warned against gharar (excessive uncertainty/gambling)',
                'action': 'If it sounds too good to be true, it probably is. Avoid.'
            },
            
            'high_pressure_tactics': {
                'warning': '"Buy now or miss out forever!", "Last chance!", aggressive salespeople',
                'islamic_principle': 'Ethical trade gives customer time to think',
                'hadith': 'The Prophet ﷺ allowed khiyar (option to cancel) for 3 days in some sales',
                'action': 'Never make major purchases under pressure. Walk away and think.'
            },
            
            'hidden_costs': {
                'warning': 'Advertised price much lower than final cost',
                'islamic_issue': 'Violates Quranic transparency (giving less than due)',
                'action': 'Ask for total cost upfront including all fees. If refused, walk away.'
            },
            
            'crisis_gouging': {
                'warning': 'Extreme price increases during emergencies',
                'example': 'Hand sanitizer for £50 during pandemic',
                'islamic_ruling': 'Haram exploitation of desperate people',
                'action': 'Report to Trading Standards. Support ethical sellers.'
            }
        },
        
        'consumer_rights_islam': {
            'right_to_return': 'Prophet ﷺ allowed khiyar (option period) for buyers to reconsider',
            'right_to_know': 'Seller must disclose defects (hiding defects = cheating)',
            'right_to_fair_price': 'No exploitation or price manipulation',
            'right_to_honest_measurement': 'Quran 83:1-3 - Give full measure',
            'uk_law_aligns': 'UK Consumer Rights Act 2015 protects these rights (aligns with Islamic principles)'
        },
        
        'support_ethical_businesses': {
            'message': 'Your spending is a vote for the type of economy you want',
            'islamic_encouragement': 'Support businesses that follow Quranic ethics',
            'boycott_exploitation': 'Avoiding exploitative businesses is form of enjoining good and forbidding evil',
            'prophet_example': 'The Prophet ﷺ exposed the cheating merchant in the market (Muslim 102) - he took action against exploitation'
        }
    }

    9.3 Transparency in Transactions
Quranic Foundation: Surah Al-Baqarah 2:282-283 (Longest Verse in Quran)
Key Points from Ayat al-Dayn (The Verse of Debt):
"O you who have believed, when you contract a debt for a specified term, write it down. And let a scribe write [it] between you in justice... And bring to witness two witnesses from among your men..."
This verse establishes:

Written contracts for financial transactions
Witnesses to prevent disputes
Clear terms and timeframes
Protection for both parties

Application to Modern Business:
class TransparencyInTransactions:
    """
    Implementing Quranic transparency standards in modern business
    """
    
    def __init__(self):
        self.transparency_requirements = self.define_requirements()
    
    def define_requirements(self):
        """
        What does Islamic transparency mean in practice?
        """
        
        return {
            'written_agreements': {
                'quranic_basis': '2:282 - When you contract debt, write it down',
                'modern_application': [
                    'Employment contracts in writing',
                    'Service agreements clearly documented',
                    'Purchase receipts provided',
                    'Subscription terms in plain language',
                    'Refund policies clearly stated'
                ],
                'digital_age': 'Email confirmations, digital receipts, terms of service pages all fulfill this',
                'protection': 'Writing prevents disputes and protects both parties'
            },
            
            'clear_terms': {
                'quranic_basis': '2:282 - Debt for specified term (clear timeframe)',
                'requirements': [
                    'Price explicitly stated',
                    'Payment schedule clear',
                    'Delivery timeframe specified',
                    'Cancellation policy explained',
                    'Obligations of both parties defined'
                ],
                'prohibited': [
                    'Vague "pay what you want"',
                    'Unclear delivery dates',
                    'Hidden clauses in fine print',
                    '"Terms subject to change without notice"'
                ]
            },
            
            'no_hidden_clauses': {
                'islamic_principle': 'Contracts must be mutually understood, no trickery',
                'modern_issues': {
                    'fine_print': {
                        'issue': 'Important terms buried in tiny text',
                        'islamic_ruling': 'Violates transparency if used to deceive',
                        'halal_approach': 'Key terms should be prominently displayed'
                    },
                    'legalese': {
                        'issue': 'Contracts written in language average person can\'t understand',
                        'islamic_principle': 'Both parties must understand agreement',
                        'solution': 'Provide plain-language summary alongside legal document'
                    },
                    'auto_renewal': {
                        'issue': 'Subscription renews without clear notice',
                        'islamic_ruling': 'Each party must clearly consent to transaction',
                        'halal_approach': 'Send clear reminder before renewal with easy opt-out'
                    }
                }
            },
            
            'disclosure_of_defects': {
                'hadith': 'The Prophet ﷺ: "The two parties in a transaction have the option to cancel so long as they have not separated. If they were honest and clear, they will be blessed in their transaction." (Bukhari 2079)',
                'requirement': 'Seller must disclose any defects or limitations',
                'modern_examples': [
                    '✓ Car dealer: "This car has 100,000 miles and needs brake work"',
                    '✓ Software: "This version has known bugs in X feature"',
                    '✓ House: "Basement has moisture issues"',
                    '✗ Hiding defects and hoping buyer doesn\'t notice = cheating'
                ],
                'used_goods': 'Especially important for used items - disclose wear, damage, missing parts'
            },
            
            'honest_timelines': {
                'principle': 'Do not promise what you cannot deliver',
                'examples': {
                    'delivery_dates': 'Only promise delivery if genuinely achievable. "2-3 weeks" better than "1 week" if unsure.',
                    'project_completion': 'Give realistic timeline, not optimistic one to win contract',
                    'customer_service': 'If callback time is 48 hours, say 48 hours, not "we\'ll get back to you soon"'
                },
                'better_to_under_promise': 'Exceeding expectations is praiseworthy. Missing promised deadline is breach of trust.'
            }
        }
    
    def assess_contract_transparency(self, contract):
        """
        Evaluate if contract meets Islamic transparency standards
        """
        
        transparency_score = {}
        
        # Check 1: Is it written?
        transparency_score['written'] = {
            'required': True,
            'status': contract.is_written,
            'quranic': '2:282 - Write it down'
        }
        
        # Check 2: Are terms clear?
        transparency_score['clear_terms'] = {
            'price_explicit': contract.price_is_explicit,
            'payment_schedule_clear': contract.payment_schedule_defined,
            'duration_specified': contract.has_end_date_or_cancellation_terms,
            'obligations_defined': contract.lists_both_parties_obligations
        }
        
        # Check 3: Plain language?
        transparency_score['understandable'] = {
            'readability_score': calculate_readability(contract.text),
            'plain_language_summary': contract.has_plain_summary,
            'islamic_principle': 'Both parties must understand what they\'re agreeing to'
        }
        
        # Check 4: No hidden surprises?
        transparency_score['no_hidden_terms'] = {
            'auto_renewal_disclosed': contract.auto_renewal_clearly_stated,
            'fees_all_listed': contract.all_fees_in_main_document,
            'cancellation_policy_clear': contract.easy_to_find_cancellation_terms
        }
        
        # Calculate overall transparency
        total_requirements = count_transparency_requirements()
        requirements_met = count_requirements_met(transparency_score)
        
        if requirements_met / total_requirements > 0.90:
            return {
                'transparency_level': 'HIGH - Meets Islamic Standards ✓',
                'score': transparency_score,
                'message': 'This contract follows Quranic transparency principles',
                'safe_to_sign': True
            }
        elif requirements_met / total_requirements > 0.70:
            return {
                'transparency_level': 'MODERATE - Some Issues',
                'score': transparency_score,
                'issues': identify_issues(transparency_score),
                'action': 'Request clarification on unclear points before signing',
                'islamic_guidance': 'Quran 2:282 requires clear terms - ask questions until you understand fully'
            }
        else:
            return {
                'transparency_level': 'LOW - Does Not Meet Islamic Standards ✗',
                'score': transparency_score,
                'issues': identify_issues(transparency_score),
                'warning': 'This contract lacks Islamic transparency',
                'action': 'Do NOT sign until terms are made clear. You have right to understand fully.',
                'hadith': 'Bukhari 2079 - Honesty and clarity bring blessing. Lack of clarity is red flag.'
            }

Contract Template: Islamic Business Agreement
def generate_islamic_contract_template():
    """
    Model contract that meets Quranic transparency standards
    Can be used for employment, services, sales, etc.
    """
    
    return {
        'title': 'ISLAMIC BUSINESS AGREEMENT TEMPLATE',
        'quranic_basis': 'Based on Surah Al-Baqarah 2:282-283',
        
        'template_structure': {
            'section_1_parties': {
                'content': 'Clearly identify both parties with full names and contact information',
                'islamic_principle': 'Know who you\'re contracting with'
            },
            
            'section_2_subject': {
                'content': 'Describe exactly what is being sold/provided/agreed upon',
                'example': 'Party A agrees to provide web development services consisting of: [specific deliverables]',
                'detail_level': 'Specific enough that both parties understand exactly what\'s included/excluded'
            },
            
            'section_3_price': {
                'content': 'State total price in clear numbers and currency',
                'example': 'Total Price: £5,000 GBP',
                'transparency': 'Include any additional fees, or explicitly state "No additional fees"',
                'quranic': 'Give full measure - no hidden costs'
            },
            
            'section_4_payment_terms': {
                'content': 'When and how payment will be made',
                'example': '£2,000 due upon contract signing, £2,000 upon project midpoint, £1,000 upon completion',
                'hadith_compliance': 'Payment schedule agreed upfront = no disputes later'
            },
            
            'section_5_timeline': {
                'content': 'Clear start and end dates, or specific duration',
                'example': 'Project Start: 1 January 2025, Expected Completion: 31 March 2025',
                'quranic': '2:282 - Debt for specified term (timeframe must be clear)'
            },
            
            'section_6_obligations': {
                'party_a_must': 'List what Party A is responsible for',
                'party_b_must': 'List what Party B is responsible for',
                'clarity': 'Prevents disputes about "whose job was that?"'
            },
            
            'section_7_quality_standards': {
                'content': 'What quality/standards are expected',
                'example': 'Website must function on Chrome, Firefox, Safari; mobile-responsive',
                'islamic_principle': 'Excellence (ihsan) in work + clear expectations'
            },
            
            'section_8_cancellation': {
                'content': 'How either party can cancel and what penalties/refunds apply',
                'example': 'Either party may cancel with 14 days notice. Refund of unused portion.',
                'transparency': 'No surprise cancellation fees'
            },
            
            'section_9_dispute_resolution': {
                'content': 'How disputes will be handled',
                'islamic_option': 'Disputes will be resolved through mediation by Islamic arbitration',
                'uk_law_option': 'Or through UK legal system',
                'prophet_example': 'Prophet ﷺ encouraged settling disputes amicably before litigation'
            },
            
            'section_10_signatures': {
                'content': 'Both parties sign and date',
                'witness_option': 'Quranic ideal: Two witnesses present (2:282)',
                'modern': 'Digital signatures valid, but witnesses still recommended for major contracts'
            }
        },
        
        'plain_language_summary': {
            'requirement': 'Before the legal contract, include 1-page summary in everyday language',
            'why': 'Ensures both parties truly understand, especially if one party not legally sophisticated',
            'example': 'PLAIN ENGLISH: Party A will build you a website. You pay £5,000 in three installments. Website will be done by March 31. If you\'re not happy, we\'ll revise twice. You can cancel anytime with 14 days notice and get refund for work not done.'
        },
        
        'prohibited_clauses': {
            'examples_of_haram_clauses': [
                '✗ "We can change terms at any time without notice"',
                '✗ "All fees are non-refundable regardless of circumstances"',
                '✗ "We are not responsible for anything ever" (total liability waiver)',
                '✗ "You waive your right to sue" (in some jurisdictions)','✗ "Price subject to change" (without clear parameters)'
],
'why_prohibited': 'These create gharar (excessive uncertainty) and violate mutual consent',
'islamic_principle': 'Both parties must enter contract with clear understanding and fair terms'
},

'recommended_additions': {
        'basmala': 'Begin contract with "Bismillah ar-Rahman ar-Rahim" (In the name of Allah)',
        'intention_statement': '"Both parties enter this agreement seeking halal provision and Allah\'s blessing"',
        'honesty_clause': '"Both parties commit to honesty and transparency per Islamic principles"',
        'dua': 'End with: "May Allah bless this transaction and make it beneficial for both parties"'
    },
    
    'digital_age_adaptations': {
        'email_contracts': 'Email exchanges can constitute written agreement if terms are clear',
        'clickwrap_agreements': 'Online "I agree" buttons are valid IF terms are genuinely accessible and clear',
        'blockchain_contracts': 'Smart contracts permissible if transparent and meet all Islamic conditions',
        'video_agreements': 'Video recording of verbal agreement can serve as documentation'
    }
}
---

## 10. CONTEMPORARY FIQH ON TECHNOLOGY & BUSINESS MODELS

### 10.1 Is Charging for Islamic Software/Content Halal?

**The Question:**
Can I charge money for Islamic apps, Quran software, or Islamic educational content? Isn't religious knowledge supposed to be free?

**Scholarly Analysis:**

**Two Types of Islamic Content:**

**Type 1: Pure Islamic Knowledge (Quran, Hadith, Fiqh)**
**Type 2: Technology/Service That Delivers Islamic Knowledge**
def islamic_software_permissibility():
    """
    Detailed analysis of charging for Islamic digital products
    """
    
    return {
        'core_principle': 'Religious knowledge itself must remain accessible. Technology to deliver it can be monetized.',
        
        'knowledge_vs_service': {
            'quran_text': {
                'ruling': 'Must be freely available',
                'evidence': 'Quran is word of Allah - cannot be restricted by pay wall',
'application': 'Basic Quran text should always have free option',
'example': 'Quran.com provides free text ✓'
},
'quran_app_with_features': {
            'ruling': 'CAN charge for enhanced features',
            'reasoning': 'You\'re not charging for Quran itself, but for the development work, features, and service',
            'permissible_paid_features': [
                'Advanced search functionality',
                'Offline access',
                'Audio recitations by famous reciters',
                'Tafsir (commentary) by scholars',
                'Note-taking and bookmarking',
                'Ad-free experience',
                'Cloud sync across devices',
                'Beautiful typography and design'
            ],
            'key_distinction': 'Basic Quran text remains free, premium features are paid',
            'example': 'Quran.com has free version + Quran.com Pro (paid) ✓'
        },
        
        'hadith_collections': {
            'ruling': 'Same as Quran - text should be accessible, service can be monetized',
            'free_requirement': 'Basic searchable hadith collections should exist free',
            'paid_version_ok': 'Enhanced features, authentication checking, scholarly commentary can be paid',
            'example': 'Sunnah.com (free) exists, so paid hadith apps are permissible ✓'
        },
        
        'islamic_education_content': {
            'ruling': 'Scholars CAN charge for their teaching',
            'evidence': [
                'Scholars throughout history were paid for teaching',
                'Prophet ﷺ said teaching Quran in exchange for payment is permissible (Bukhari 5737)',
                'Teachers need to earn living to dedicate time to knowledge'
            ],
            'free_knowledge_requirement': 'Basic knowledge should be available free somewhere (fulfilled by YouTube, free lectures, etc.)',
            'paid_courses_permissible': 'Structured courses, personalized teaching, premium content = permissible to charge',
            'examples': {
                'halal': 'Bayyinah TV (paid courses), SeekersGuidance (paid + free), AlMaghrib Institute (paid seminars)',
                'justification': 'Free Islamic content exists widely. Paid premium content supports scholars\' livelihoods.'
            }
        }
    },
    
    'scholarly_consensus': {
        'classical_position': 'Scholars throughout history received stipends from governments or community to teach',
        'modern_application': 'In absence of government support, scholars can charge for services',
        'key_principle': 'Knowledge of Islam should never be completely inaccessible due to cost',
        'solution': 'Freemium model - free basic access, paid premium features/content'
    },
    
    'specific_scenarios': {
        'quran_memorization_app': {
            'product': 'App that helps users memorize Quran with spaced repetition, tracking, tests',
            'ruling': 'PERMISSIBLE to charge',
            'reasoning': 'You\'re charging for the educational tool, not the Quran itself',
            'condition': 'Quran text itself should be viewable for free (app just adds learning features)',
            'similar_to': 'Hiring a Quran teacher - you pay for teaching service, not the Quran'
        },
        
        'prayer_times_app': {
            'product': 'App calculating prayer times with notifications',
            'ruling': 'PERMISSIBLE to charge',
            'reasoning': 'Prayer times calculations require development work. You\'re not charging for obligation of prayer itself.',
            'free_alternatives_exist': 'Many free prayer time apps, so paid ones offer premium experience',
            'halal_revenue_models': 'One-time purchase, subscription, or ads all permissible'
        },
        
        'islamic_books_digital': {
            'product': 'Selling digital versions of Islamic books',
            'ruling': 'PERMISSIBLE',
            'reasoning': 'Scholars and publishers can charge for their work',
            'condition': 'If book contains pure Quran/hadith text, those portions should be accessible elsewhere free',
            'modern_standard': 'Scholars publish books (physical/digital) for income - universally accepted'
        },
        
        'tafsir_app': {
            'product': 'Comprehensive Quran commentary by scholars',
            'ruling': 'PERMISSIBLE to charge',
            'reasoning': 'Tafsir is scholars\' intellectual work and research. Can be monetized.',
            'free_requirement': 'Basic Quran text without commentary should be free somewhere',
            'example': 'Buying Tafsir Ibn Kathir book = buying scholar\'s work, not Quran itself'
        },
        
        'dua_collection_app': {
            'product': 'Authenticated dua collection with audio, translations, occasions',
            'ruling': 'PERMISSIBLE to charge',
            'reasoning': 'You\'re charging for collection, organization, translation, audio work',
            'note': 'Basic duas should be available free somewhere (many are on websites)',
            'added_value': 'Audio recordings, beautiful design, organization = your work = can charge'
        },
        
        'hajj_guide_app': {
            'product': 'Comprehensive Hajj/Umrah guide with maps, step-by-step instructions, AR features',
            'ruling': 'PERMISSIBLE to charge',
            'reasoning': 'Educational tool providing service. Hajj knowledge is free online; you\'re charging for convenience and features.',
            'similar_to': 'Hajj tour operators charge for their service while Hajj itself is free at Haram'
        }
    },
    
    'revenue_model_assessment': {
        'one_time_purchase': {
            'example': 'Pay £9.99 once, own app forever',
            'islamic_ruling': 'PERMISSIBLE',
            'transparency': 'Clearly state it\'s one-time (no hidden subscriptions)'
        },
        
        'subscription': {
            'example': 'Pay £4.99/month for premium features',
            'islamic_ruling': 'PERMISSIBLE',
            'conditions': [
                'Terms clearly stated',
                'Easy cancellation (not trap users)',
                'Provide real ongoing value (not just unlocking features once)'
            ],
            'best_practice': 'Remind before renewal, allow one-click cancellation'
        },
        
        'freemium': {
            'example': 'Free basic version, paid premium version',
            'islamic_ruling': 'IDEAL MODEL ✓',
            'why_ideal': 'Ensures basic Islamic knowledge accessible to all, while allowing monetization for enhanced service',
            'prophet_example': 'Prophet ﷺ taught everyone freely, but also accepted gifts/support',
            'modern_examples': 'Quran.com (free + Pro), Bayyinah TV (free YouTube + paid premium)'
        },
        
        'ads': {
            'example': 'Free app with advertisements',
            'islamic_ruling': 'PERMISSIBLE with conditions',
            'conditions': [
                'Ads must be halal (no alcohol, gambling, inappropriate content)',
                'Ads should not disrupt worship (e.g., not during Quran recitation)',
                'User should have option to pay to remove ads'
            ],
            'concerns': 'Some scholars dislike ads in Quran apps as disrespectful, but majority permit if halal ads'
        },
        
        'donations': {
            'example': 'Free app, ask for voluntary donations',
            'islamic_ruling': 'EXCELLENT MODEL ✓',
            'why_excellent': 'Combines free access with community support',
            'challenge': 'Often insufficient to sustain development',
            'solution': 'Donations + optional premium features'
        },
        
        'sponsorships': {
            'example': 'Islamic organizations sponsor app for community',
            'islamic_ruling': 'EXCELLENT if sponsors don\'t control content',
            'historical_parallel': 'Classical scholars sponsored by rulers/wealthy Muslims',
            'modern_application': 'Masajid or Islamic foundations can sponsor free apps for ummah'
        }
    },
    
    'prohibited_practices': {
        'paywall_basic_quran': {
            'example': 'Cannot read Quran text at all without paying',
            'ruling': 'HARAM',
            'reason': 'Restricting access to Allah\'s word',
            'solution': 'Always offer free basic Quran text access'
        },
        
        'charging_for_fard_knowledge': {
            'example': 'Charging for knowledge of how to pray (fard ayn)',
            'ruling': 'HARAM',
            'reason': 'Basic obligatory knowledge must be freely accessible',
            'modern_reality': 'This IS freely available (YouTube, websites, masjids), so paid courses on prayer are permissible as premium/detailed options'
        },
        
        'deceptive_free_trials': {
            'example': '"Free" app that charges without clear warning',
            'ruling': 'HARAM (deception)',
            'islamic_principle': 'Transparency required in all transactions',
            'solution': 'Clearly state trial duration and when charging begins'
        },
        
        'price_exploitation': {
            'example': 'Charging £100/month for basic Quran app',
            'ruling': 'Haram (exploitation)',
            'principle': 'Fair pricing is Islamic requirement',
            'guideline': 'Price should reflect actual value and development cost, not exploit religious need'
        }
    },
    
    'mizaan_rizq_specific': {
        'are_our_platforms_halal_to_monetize': {
            'mizaan_spending_tracker': {
                'product': 'App helping Muslims track spending with Islamic categories, zakat calculator',
                'ruling': 'PERMISSIBLE to charge ✓',
                'reasoning': [
                    'You\'re providing financial technology tool',
                    'Islamic categories/zakat features are your development work',
                    'Free basic budgeting tools exist elsewhere',
                    'Premium features = premium price is fair'
                ],
                'recommended_model': 'Freemium - free basic tracking, paid premium features (advanced analytics, zakat auto-calculation, etc.)',
                'not_charging_for': 'Islamic knowledge itself',
                'charging_for': 'Technology, convenience, advanced features, ongoing development'
            },
            
            'rizq_job_platform': {
                'product': 'Platform connecting Muslims with halal jobs',
                'ruling': 'PERMISSIBLE to charge ✓',
                'charging_whom': 'Can charge employers (job posting fees) and/or job seekers (premium features)',
                'reasoning': [
                    'You\'re providing valuable service (halal verification, matching)',
                    'Platform maintenance requires funding',
                    'Free job boards exist (Indeed, LinkedIn)',
                    'Your added value is Islamic vetting = worth paying for'
                ],
                'recommended_model': {
                    'for_job_seekers': 'Free basic access, paid premium (featured profile, skills courses, priority matching)',
                    'for_employers': 'Pay per job listing or subscription for multiple listings',
                    'for_both': 'Option for Islamic organizations to sponsor free access for community members'
                },
                'ethical_considerations': [
                    'Don\'t make basic job search inaccessible to poor Muslims',
                    'Consider sliding scale or sponsorships for those in need',
                    'Free access for refugees, students, unemployed (verify status)'
                ]
            }
        }
    },
    
    'final_guidelines': {
        'primary_principle': 'Islamic knowledge must remain accessible. Tools to access it can be monetized.',
        'transparency': 'Clearly communicate what\'s free vs. paid',
        'fairness': 'Price fairly, don\'t exploit religious need',
        'charity_consideration': 'Consider providing free access to students, scholars, those in need',
        'barakah': 'Make intention to serve Allah and ummah, not just profit. Allah will place barakah in business.',
        'sadaqah_jariyah': 'Can make platform sadaqah jariyah by having "sponsor a user" option where wealthy pay for others'
    }
} 

---

### 10.2 Freemium vs. Subscription Models - Islamic Analysis

def freemium_vs_subscription_islamic_analysis():
    """
    Comparing business models from Islamic ethics perspective
    """
    
    return {
        'freemium_model': {
            'definition': 'Free basic version + paid premium version',
            'structure': 'Core functionality free, advanced features paid',
            
            'islamic_assessment': {
                'ruling': 'IDEAL MODEL for Islamic apps ✓',
                'strengths': [
                    'Ensures accessibility - poor Muslims can still use basic version',
                    'Follows Islamic principle of "no one turned away from knowledge"',
                    'Fair - those who can pay support those who can\'t',
                    'Similar to classical Islamic model: public lectures free, private tutoring paid'
                ],
                'examples': {
                    'quran_com': 'Free Quran text, paid Pro version with advanced features',
                    'muslim_pro': 'Free basic app, paid premium features',
                    'seekers_guidance': 'Free articles and some courses, paid premium courses'
                },
                'prophet_model': 'Prophet ﷺ taught everyone, but accepted support from wealthy companions who then supported the poor'
            },
            
            'implementation_guidelines': {
                'what_should_be_free': [
                    'Core religious functionality (Quran text, basic prayer times, basic knowledge)',
                    'Essential features for practicing Islam',
                    'Enough value that user can benefit without paying'
                ],
                'what_can_be_premium': [
                    'Advanced features (analytics, insights, personalization)',
                    'Convenience features (offline access, cloud sync)',
                    'Enhanced experience (ad-free, beautiful themes)',
                    'Premium content (detailed courses, scholar Q&A)',
                    'Priority support'
                ],
                'balance': 'Free version should be genuinely useful, not crippled "demo"'
            },
            
            'pricing_ethics': {
                'reasonable_premium_price': '£2-10/month or £20-100/year for apps',
                'student_discount': 'Consider offering discounts for students',
                'family_plans': 'Islamic families are encouraged - offer family pricing',
                'hardship_discount': 'Consider "pay what you can" for those in financial difficulty',
                'lifetime_option': 'Offer one-time purchase option for those who prefer it'
            }
        },
        
        'subscription_model': {
            'definition': 'Recurring payment for ongoing access',
            'structure': 'Monthly or annual fee, access to all features',
            
            'islamic_assessment': {
                'ruling': 'PERMISSIBLE with conditions',
                'strengths': [
                    'Sustainable funding for ongoing development',
                    'Regular income allows better service',
                    'Users only pay when using (can cancel anytime)'
                ],
                'concerns': [
                    'Can create barrier for poor Muslims if no free option',
                    'Risk of "subscription trap" if cancellation difficult',
                    'Must provide ongoing value, not just unlock features once'
                ],
                'conditions_for_permissibility': [
                    'Must have free alternative or free tier',
                    'Terms clearly disclosed upfront',
                    'Easy cancellation (one-click, no phone calls required)',
                    'Reminder before renewal',
                    'Genuine ongoing value (updates, new content, support)'
                ]
            },
            
            'halal_subscription_practices': {
                'transparency': {
                    'requirement': 'User must clearly understand they\'re subscribing',
                    'bad_practice': 'Hidden auto-renewal after "free trial"',
                    'good_practice': 'Clear statement: "£4.99/month, renews monthly, cancel anytime"',
                    'reminder': 'Email 7 days before renewal: "Your subscription renews on X"'
                },
                
                'cancellation_ease': {
                    'hadith_principle': 'Prophet ﷺ allowed khiyar (option to cancel) - modern equivalent is easy cancellation',
                    'haram': 'Requiring phone call, making user navigate maze to cancel, or retention tactics that pressure',
                    'halal': 'One-click cancellation in account settings, no questions asked',
                    'best_practice': 'Cancel button same prominence as subscribe button'
                },
                
                'ongoing_value': {
                    'principle': 'If user pays monthly, provide monthly value',
                    'examples_of_value': [
                        'Regular content updates',
                        'New features added',
                        'Ongoing support access',
                        'Cloud storage/sync services',
                        'Community features'
                    ],
                    'not_acceptable': 'Charging monthly just to access features that were already built (no ongoing service)'
                },
                
                'pause_option': {
                    'good_practice': 'Allow users to pause subscription (e.g., during travel, Ramadan, financial difficulty)',
                    'islamic_principle': 'Flexibility and compassion in business dealings',
                    'example': 'Pause for 1-3 months, resume anytime'
                }
            }
        },
        
        'hybrid_model': {
            'definition': 'Multiple pricing tiers - free, basic paid, premium paid',
            'structure': 'Free (basic) → Paid tier 1 (£5/month) → Paid tier 2 (£10/month)',
            
            'islamic_assessment': {
                'ruling': 'PERMISSIBLE and often IDEAL',
                'why_ideal': 'Accommodates different financial situations',
                'example_structure': {
                    'free_tier': 'Basic Quran text, simple prayer times, ads',
                    'basic_paid': '£3/month - Ad-free, offline access, basic features',
                    'premium_paid': '£8/month - All features, priority support, advanced tools'
                }
            }
        },
        
        'alternative_models': {
            'pay_what_you_want': {
                'description': 'User chooses own price (can be £0)',
                'islamic_assessment': 'EXCELLENT from ethics standpoint',
                'challenge': 'Often insufficient revenue for sustainability',
                'best_for': 'Community-supported projects, Islamic non-profits',
                'example': 'Humble Bundle model - set minimum, users pay more if they want'
            },
            
            'tip_jar': {
                'description': 'Free app with voluntary donations',
                'islamic_ruling': 'EXCELLENT (similar to sadaqah)',
                'reality': 'Only 1-5% of users typically donate',
                'solution': 'Combine with optional premium features for sustainability'
            },
            
            'community_sponsored': {
                'description': 'Islamic organization pays for entire community to access free',
                'islamic_ruling': 'IDEAL ✓✓✓',
                'historical_model': 'Wealthy Muslims sponsored scholars; scholars taught community free',
                'modern_application': 'Masjid pays for Mizaan/Rizq access for all members',
                'implementation': 'Offer "community license" to Islamic organizations at bulk discount'
            }
        },
        
        'for_mizaan_rizq_recommendation': {
            'mizaan_spending_tracker': {
                'recommended_model': 'Freemium',
                'free_tier': [
                    'Basic expense tracking',
                    'Simple categorization',
                    'Manual zakat calculation',
                    'Monthly insights'
                ],
                'premium_tier': [
                    '£4.99/month or £49/year',
                    'Automatic Islamic categorization (daruriyyat, hajiyyat, etc.)',
                    'Automated zakat calculation with hawl tracking',
                    'Advanced analytics and insights',
                    'Israf detection AI',
                    'Export features',
                    'Priority support'
                ],
                'add_on': {
                    'community_license': 'Masjids can pay £199/year to provide premium access to all members',
                    'student_discount': '50% off for students',
                    'hardship': 'Free premium for those in financial difficulty (honor system)'
                }
            },
            
            'rizq_job_platform': {
                'recommended_model': 'Freemium for job seekers, paid for employers',
                'for_job_seekers': {
                    'free': [
                        'Browse all halal-verified jobs',
                        'Apply to unlimited jobs',
                        'Basic profile',
                        'Email alerts'
                    ],
                    'premium': [
                        '£9.99/month or £99/year',
                        'Featured profile (employers see you first)',
                        'Advanced job matching algorithm',
                        'Access to skills training courses',
                        'Resume review by mentor',
                        'Interview preparation resources',
                        'Priority consideration from employers'
                    ]
                },
                'for_employers': {
                    'pricing': '£99-299 per job listing (depending on visibility level)',
                    'or': '£999/year unlimited listings subscription',
                    'value': 'Halal verification service + access to motivated Muslim workforce',
                    'discount': 'Islamic non-profits post free or at 50% discount'
                },
                'sponsorship': {
                    'model': 'Wealthy Muslims or organizations can sponsor free premium access for unemployed Muslims',
                    'sadaqah_jariyah': 'Frame as ongoing charity - helping someone find halal income',
                    'implementation': '"Sponsor a job seeker" button - pay £100 to give premium access to 10 unemployed Muslims'
                }
            }
        }
    }

10.3 Advertising vs. Subscriptions - Which is More Islamic?
vdef ads_vs_subscriptions_islamic_analysis():
    """
    Comparing advertising-based vs subscription-based revenue models
    """
    
    return {
        'advertising_model': {
            'definition': 'Free app/service supported by showing ads to users',
            'how_it_works': 'Advertisers pay platform to show ads to users',
            
            'islamic_assessment': {
                'base_ruling': 'PERMISSIBLE with strict conditions',
                
                'conditions_for_permissibility': {
                    'halal_ads_only': {
                        'requirement': 'MUST filter out haram advertisements',
                        'prohibited_ads': [
                            'Alcohol',
                            'Gambling/lottery',
                            'Interest-based financial products (conventional loans, credit cards promoting debt)',
                            'Dating apps (designed for zinā)',
                            'Immodest clothing/imagery',
                            'Music/entertainment with haram elements',
                            'Pork products',
                            'Adult content'
                        ],
                        'challenge': 'Major ad networks (Google AdSense, Facebook Ads) don\'t offer "halal-only" filtering',
                        'solution': 'Use Islamic ad networks or manually approve ads'
                    },
                    
                    'respect_for_content': {
                        'principle': 'Ads should not interrupt worship or disrespect Islamic content',
                        'bad_practice': 'Ad plays during Quran recitation',
                        'good_practice': 'Ads only between features, never during Quran/prayer/dhikr',
                        'example': 'YouTube quran recitations with ads = many scholars dislike this'
                    },
                    
                    'no_manipulation': {
                        'principle': 'Ads should not manipulate or deceive users',
                        'prohibited': [
                            'Fake "download" buttons',
                            'Misleading ads that look like app content',
                            'Ads that auto-play with sound',
                            'Ads that hijack user experience'
                        ],
                        'hadith': 'Prophet ﷺ: "Whoever cheats is not one of us" - applies to deceptive ads'
                    },
                    
                    'user_control': {
                        'principle': 'Offer users option to pay to remove ads',
                        'reasoning': 'Don\'t force users to see ads if they prefer paid version',
                        'best_practice': 'Clear "Remove ads for £X" option'
                    }
                },
                
                'concerns_from_scholars': {
                    'commercialization_of_deen': {
                        'concern': 'Treating Islam as business opportunity, showing ads during worship feels disrespectful',
                        'response': 'If ads are halal and non-intrusive, it\'s permissible way to fund free access',
                        'balance': 'Subscription option for those who want completely ad-free experience'
                    },
                    
                    'data_collection': {
                        'concern': 'Ad networks track user behavior (privacy issue)',
                        'islamic_principle': 'Respecting privacy is Islamic obligation',
                        'solution': 'Use privacy-respecting ad networks, disclose data collection, give opt-out'
                    }
                },
                
                'verdict': 'Permissible but LESS PREFERRED than subscriptions due to:',
                'reasons': [
                    'Difficult to ensure all ads are 100% halal',
                    'Can feel disrespectful in religious context',
                    'Privacy concerns with ad tracking',
                    'User experience degradation'
                ]
            },
            
            'when_ads_are_acceptable': {
                'scenario_1': 'Non-religious app (like Rizq job platform) where ads feel less intrusive',
                'scenario_2': 'Strictly halal-vetted ads from Islamic businesses only',
                'scenario_3': 'As funding option alongside paid alternative (user chooses: see ads or pay)'
            }
        },
        
        'subscription_model': {
            'definition': 'Users pay recurring fee for ad-free, premium experience',
            
            'islamic_assessment': {
                'base_ruling': 'PREFERRED over advertising',
                
                'strengths': [
                    'Direct transaction (user pays for service) - very clear and halal',
                    'No risk of haram ads slipping through',
                    'Better user experience (no interruptions)',
                    'More respectful for religious content',
                    'Privacy-friendly (no ad tracking)',
                    'Aligns with Islamic business principle: honest trade, clear value exchange'
                ],
                
                'challenges': [
                    'Creates barrier for poor Muslims if no free option',
                    'Requires payment infrastructure',
                    'Ongoing commitment vs. one-time payment'
                ],
                
                'islamic_solutions': {
                    'freemium_hybrid': 'Free ad-supported version + paid ad-free version',
                    'hardship_discount': 'Subsidized access for students, unemployed, refugees',
                    'community_sponsorship': 'Wealthy Muslims sponsor subscriptions for others',
                    'sliding_scale': 'Pay what you can afford'
                }
            },
            
            'verdict': 'MORE ALIGNED with Islamic principles because:',
            'reasons': [
                'Transparent value exchange',
                'No risk of haram content exposure',
                'Respects dignity of Islamic content',
                'Better privacy protection',
                'Higher quality user experience'
            ]
        },
        
        'hybrid_approach': {
            'recommended_model': 'Free (with halal ads) + Paid (ad-free premium)',
            
            'structure': {
                'free_tier': {
                    'access': 'Core functionality',
                    'ads': 'Strictly halal-vetted ads, non-intrusive placement',
                    'limitations': 'Basic features only',
                    'purpose': 'Ensure accessibility for all Muslims'
                },
                
                'paid_tier': {
                    'price': 'Affordable (£3-10/month)',
                    'benefits': 'Ad-free + premium features',
                    'purpose': 'Sustainable revenue while respecting user experience'
                }
            },
            
            'best_practice': {
                'dont_force_ads': 'Make paid option clearly available from start',
                'halal_ads_only': 'Manually vet ad content or use Islamic ad networks',
                'respect_context': 'Never show ads during worship (Quran, prayer, dhikr)',
                'transparent': 'Clearly explain how ads fund free version'
            }
        },
        
        'alternative_revenue_models': {
            'one_time_purchase': {
                'description': 'Pay once, own forever',
                'islamic_assessment': 'EXCELLENT - clearest halal transaction',
                'challenge': 'Less revenue for ongoing development/servers',
                'best_for': 'Downloadable apps without cloud services'
            },
            
            'donations': {
                'description': 'Free service, voluntary donations',
                'islamic_assessment': 'IDEAL from ethics standpoint',
                'reality': 'Usually insufficient for sustainability',
                'solution': 'Combine with paid options for those who can afford'
            },
            
            'affiliate_marketing': {
                'description': 'Recommend halal products/services, earn commission',
                'islamic_assessment': 'PERMISSIBLE if products are halal and genuinely beneficial',
                'example': 'Islamic bookstore affiliate link in Quran app',
                'conditions': [
                    'Only recommend products you genuinely believe in',
                    'Disclose affiliate relationship',
                    'No deceptive recommendations',
                    'Product itself must be halal'
                ]
            },
            
            'institutional_licensing': {
                'description': 'Sell licenses to masajid, Islamic schools, organizations',
                'islamic_assessment': 'EXCELLENT ✓',
                'example': 'Masjid pays £500/year, all members get premium access free',
                'historical_parallel': 'Wealthy patrons supporting scholars who teach community',
                'scaling': 'One payment benefits many Muslims'
            }
        },
        
        'recommendation_for_mizaan_rizq': {
            'mizaan_spending_tracker': {
                'recommended': 'Freemium (NO ads)',
                'reasoning': [
                    'Financial app with sensitive data - ads feel intrusive',
                    'Islamic focus makes ads difficult to vet properly',
                    'Users willing to pay for financial tools',
                    'Subscription sustainable for ongoing development'
                ],
                'structure': {
                    'free': 'Basic expense tracking, simple categorization',
                    'paid': '£4.99/month - Advanced Islamic features, no ads ever'
                },
                'no_ads_ever': 'Even free tier should have no ads for dignity of Islamic content'
            },
            
            'rizq_job_platform': {
                'recommended': 'Freemium + B2B revenue (employers pay)',
                'reasoning': [
                    'Job seekers shouldn\'t face ads during stressful job search',
                    'Employers willing to pay to reach motivated Muslim talent',
                    'B2B model more sustainable than ads'
                ],
                'structure': {
                    'job_seekers': 'Free basic access, optional paid premium',
                    'employers': 'Pay per listing or subscription',
                    'no_ads': 'Platform stays clean and professional'
                }
            }
        },
        
        'final_principle': {
            'ideal': 'Direct payment (subscription/purchase) is most Islamic - clear value exchange',
            'acceptable': 'Halal ads as funding mechanism for free tier',
            'best_approach': 'Offer both - let users choose',
            'priority': 'Never compromise Islamic content integrity for revenue'
        }
    }

10.4 Data Privacy from Islamic Perspective
def data_privacy_islamic_perspective():
    """
    How Islam views user data collection, privacy, and digital rights
    """
    
    return {
        'islamic_foundations': {
            'privacy_is_sacred': {
                'quran': '"O you who believe, avoid much suspicion, for some suspicion is a sin. And do not spy on one another..." (49:12)',
                'principle': 'Islam protects privacy - even suspicion (let alone actual spying) is condemned',
                'application': 'User data is private. Collecting it requires valid reason and consent.'
            },
            
            'trust_is_amanah': {
                'concept': 'When user gives you their data, it's an amanah (trust)',
'hadith': '"Return the trust to those who entrusted you, and do not betray those who betrayed you." (Abu Dawud 3535)',
'application': 'User data is a trust. You must protect it and use it only as agreed.',
'breach': 'Misusing user data = betraying trust = major sin'
},
'consent_is_required': {
            'principle': 'Cannot use someone\'s property (including information) without permission',
            'quran': '"O you who believe, do not consume one another\'s wealth unjustly, but only [in lawful] business by mutual consent." (4:29)',
            'application': 'User must explicitly consent to data collection. Pre-checked boxes = no valid consent.',
            'informed_consent': 'User must understand what they\'re consenting to (not buried in 50-page policy)'
        }
    },
    
    'data_collection_ethics': {
        'what_you_can_collect': {
            'permissible_with_consent': [
                'Data necessary for service (name, email to create account)',
                'Data to improve service (usage analytics to fix bugs)',
                'Data user explicitly shares (profile information)',
                'Data for security (IP address to prevent fraud)'
            ],
            'conditions': [
                'Clear disclosure of what you collect',
                'Explicit consent (not buried in terms)',
                'Legitimate purpose for collection',
                'Minimal collection (only what\'s needed)'
            ]
        },
        
        'what_you_cannot_collect': {
            'prohibited_without_explicit_consent': [
                'Sensitive data (health, financial, religious practice details) without clear reason',
                'Location tracking beyond what service requires',
                'Contact list harvesting',
                'Microphone/camera access without explicit permission for specific feature',
                'Cross-app tracking'
            ],
            'never_permissible': [
                'Selling user data to third parties without explicit consent',
                'Using data for purposes beyond what user agreed to',
                'Collecting data deceptively (hidden trackers)',
                'Keylogging or spying on user activity outside your app'
            ]
        },
        
        'islamic_principle_of_necessity': {
            'rule': 'Only collect data that is truly necessary (daruri)',
            'example': {
                'necessary': 'Email address to send password reset',
                'unnecessary': 'Email address just to "build our email list"'
            },
            'prophet_teaching': 'Islam encourages minimalism in all things - apply to data collection'
        }
    },
    
    'transparency_requirements': {
        'privacy_policy': {
            'islamic_requirement': 'Must be clear and understandable (no gharar)',
            'prohibited': '50-page legal document no one reads',
            'required': [
                'Plain language summary at top',
                'Clearly state what data you collect',
                'Clearly state why you collect it',
                'Clearly state who you share it with',
                'Clearly state how user can delete their data'
            ],
            'best_practice': 'Layer approach - short summary with links to details'
        },
        
        'data_sharing_disclosure': {
            'requirement': 'If you share user data with third parties, disclose prominently',
            'examples': {
                'transparent': '"We use Google Analytics to understand how users interact with our app"',
                'deceptive': 'Burying data sharing in paragraph 47 of privacy policy'
            },
            'islamic_principle': 'User entrusted YOU with data. If you pass to others, user must know.'
        },
        
        'changes_to_policy': {
            'requirement': 'If privacy practices change, notify users clearly',
            'prohibited': '"We may update this policy at any time without notice"',
            'required': 'Email notification of material changes + option to delete account if user disagrees',
            'consent': 'For significant changes (new data collection, new third parties), request fresh consent'
        }
    },
    
    'user_rights': {
        'right_to_access': {
            'islamic_basis': 'Data is user\'s "property" - they have right to see what you have',
            'implementation': 'Provide "Download my data" feature',
            'timeframe': 'Within reasonable time (7-30 days)'
        },
        
        'right_to_deletion': {
            'islamic_basis': 'If user withdraws trust (amanah), you must return it (delete data)',
            'implementation': 'Clear "Delete my account" button',
            'complete_deletion': 'Must delete from all systems, including backups (within reasonable retention period)',
            'exceptions': 'Can retain data required by law (financial records, etc.)'
        },
        
        'right_to_correction': {
            'islamic_basis': 'Accuracy and honesty - user should be able to correct false information',
            'implementation': 'Allow users to edit their profile/data',
            'application': 'If you use data for decisions (credit scoring, job matching), user must be able to correct errors'
        },
        
        'right_to_portability': {
            'islamic_basis': 'User\'s data belongs to them, not you',
            'implementation': 'Provide data in standard format (JSON, CSV) so user can move to another service',
            'no_lock_in': 'Don\'t hold user data hostage to prevent them from leaving'
        }
    },
    
    'data_security': {
        'obligation_to_protect': {
            'islamic_basis': 'Amanah (trust) includes protecting what\'s been entrusted',
            'hadith': 'Prophet ﷺ: "A Muslim is the one from whose tongue and hands the Muslims are safe." (Bukhari 10)',
            'application': 'Keep user data safe from breaches',
            'requirements': [
                'Encryption (in transit and at rest)',
                'Access controls (only authorized staff)',
                'Regular security audits',
                'Prompt breach notification if compromised'
            ]
        },
        
        'employee_access': {
            'principle': 'Limit who can see user data',
            'islamic_basis': 'Quran 49:12 - "Do not spy" - even your own employees shouldn\'t snoop',
            'implementation': [
                'Role-based access (only those who need it)',
                'Audit logs (track who accessed what)',
                'Anonymization where possible',
                'Training on privacy ethics'
            ],
            'prohibited': 'Employees browsing user data out of curiosity'
        },
        
        'breach_response': {
            'islamic_obligation': 'If trust is breached, immediately inform and make amends',
            'requirements': [
                'Notify affected users promptly',
                'Explain what happened honestly',
                'State what data was compromised',
                'Explain steps you\'re taking to prevent future breaches',
                'Offer assistance (free credit monitoring if financial data breached)'
            ],
            'prohibited': 'Covering up breach or delaying notification'
        }
    },
    
    'special_considerations_for_islamic_apps': {
        'religious_practice_data': {
            'sensitivity': 'Data about user\'s prayers, Quran reading, religious habits is HIGHLY sensitive',
            'risk': 'In some countries, this data could be used to persecute Muslims',
            'requirements': [
                'Extra encryption',
                'No sharing with third parties ever',
                'No government backdoors',
                'Option for local-only storage (no cloud sync)',
                'Anonymous usage where possible'
            ],
            'example': 'Prayer time app should NOT need to know user identity to function'
        },
        
        'zakat_and_financial_data': {
            'sensitivity': 'User\'s wealth information is private (awrah in some contexts)',
            'hadith': 'Prophet ﷺ praised charity given so secretly "left hand doesn\'t know what right hand gave"',
            'requirements': [
                'Strong encryption',
                'No sharing with third parties',
                'Option to not store in cloud',
                'Clear data retention policy'
            ],
            'mizaan_specific': 'Mizaan must protect users\' spending data with highest security standards'
        },
        
        'job_seeking_data': {
            'sensitivity': 'CV, employment history, salary expectations are private',
            'requirements': [
                'User controls visibility',
                'Employers see only what user explicitly shares',
                'No selling data to recruiters',
                'Option for anonymous browsing'
            ],
            'rizq_specific': 'Rizq must never share user data with employers without explicit consent for each instance'
        }
    },
    
    'prohibited_practices': {
        'dark_patterns': {
            'examples': [
                'Making "Accept all cookies" button prominent, "Reject" button hidden',
                'Pre-checked consent boxes',
                'Confusing opt-out processes',
                'Nagging users repeatedly to accept tracking'
            ],
            'islamic_ruling': 'HARAM - This is deception (gharar) and extracting consent through manipulation',
            'prophet_teaching': 'Muslim 102 - "Whoever cheats is not one of us"'
        },
        
        'data_broker_sales': {
            'practice': 'Selling user data to data brokers/advertisers',
            'islamic_ruling': 'HARAM without explicit, informed consent',
            'reasoning': 'User gave YOU trust, not permission to sell their information',
            'exception': 'Only permissible if clearly disclosed and user explicitly opts in'
        },
        
        'tracking_across_apps': {
            'practice': 'Following user across different apps/websites',
            'islamic_assessment': 'Highly problematic - resembles "spying" condemned in Quran 49:12',
            'permissibility': 'Only if user explicitly consents and understands what it means',
            'best_practice': 'Don\'t do it, or make it opt-in with clear explanation'
        },
        
        'government_surveillance_cooperation': {
            'scenario': 'Government requests user data for surveillance',
            'islamic_perspective': {
                'protecting_user': 'You have duty to protect user\'s amanah',
                'legitimate_law_enforcement': 'If legal warrant for specific crime investigation, compliance may be necessary',
                'mass_surveillance': 'Cooperating with mass surveillance of Muslims = betraying trust',
                'recommendation': 'Challenge overbroad requests, fight for user privacy, only comply with specific valid warrants'
            },
            'transparency': 'Publish transparency reports showing government requests received'
        }
    },
    
    'best_practices_for_mizaan_rizq': {
        'mizaan_spending_tracker': {
            'data_sensitivity': 'HIGH - Financial data is very private',
            'recommendations': [
                'End-to-end encryption option',
                'Local-only storage option (no cloud sync)',
                'Zero-knowledge architecture (you can\'t see user data)',
                'No third-party analytics that see spending data',
                'Clear retention policy (delete data after X time of inactivity)',
                'Two-factor authentication to protect account'
            ],
            'privacy_policy': {
                'principle': 'Your money, your data, your control',
                'promises': [
                    'We never sell your data',
                    'We never share with third parties without your explicit consent',
                    'We can\'t see your actual spending details (encrypted)',
                    'You can export and delete your data anytime'
                ]
            }
        },
        
        'rizq_job_platform': {
            'data_sensitivity': 'HIGH - Employment data affects livelihood',
            'recommendations': [
                'User controls CV visibility (public, private, or only to selected employers)',
                'Anonymous browsing option',
                'No sharing candidate data with employers without explicit application',
                'No selling user data to recruiters/headhunters',
                'Employer ratings and reviews to protect job seekers',
                'Option to hide profile from current employer'
            ],
            'privacy_policy': {
                'principle': 'Your career, your control',
                'promises': [
                    'Employers only see your profile if you apply or make it public',
                    'We never sell your data',
                    'You control what\'s visible',
                    'Easy account deletion with complete data removal'
                ]
            }
        }
    },
    
    'gdpr_and_islamic_alignment': {
        'observation': 'EU GDPR (General Data Protection Regulation) aligns well with Islamic privacy principles',
        'shared_principles': [
            'Consent required',
            'Transparency required',
            'Data minimization (only collect what\'s needed)',
            'User rights (access, deletion, portability)',
            'Security required',
            'Breach notification required'
        ],
        'conclusion': 'Complying with GDPR is good step toward Islamic data ethics',
        'beyond_gdpr': 'Islamic ethics adds spiritual dimension - data is amanah (trust), not just legal requirement'
    },
    
    'final_principles': {
        'guiding_questions': [
            '1. Would I be comfortable if this data about me was collected?',
            '2. Am I treating user data as a sacred trust (amanah)?',
            '3. Am I being completely transparent?',
            '4. Am I collecting only what\'s truly necessary?',
            '5. Would the Prophet ﷺ approve of my data practices?'
        ],
        
        'golden_rule': 'Treat user data as you would want your own data treated',
        
        'highest_standard': {
            'prophet_example': 'Prophet ﷺ was known as Al-Amin (The Trustworthy) before prophethood',
            'application': 'Your platform should be known as most trustworthy with user data',
            'reputation': 'Islamic platforms should set the HIGHEST standards for privacy, not lowest',
            'competitive_advantage': 'Muslims will trust platform that truly respects their privacy per Islamic principles'
        }
    }
}
---

## COMPLETE RESEARCH FOUNDATION SUMMARY
def complete_research_summary():
    """
    Executive summary of entire Islamic economic research foundation
    For quick reference by development team
    """
    
    return {
        'mizaan_spending_tracker': {
            'quranic_foundation': [
                'Quran 25:67 - Balanced spending (not excessive, not miserly)',
                'Quran 17:29 - Neither tightly closed nor fully extended hand',
                'Quran 6:141 - Do not commit excess'
            ],
            
            'spending_categories': {
                'daruriyyat': 'Essentials - necessary for life',
                'hajiyyat': 'Needed - removes hardship',
                'tahsiniyyat': 'Improvements - beautifies life',
                'israf': 'Wasteful - excess and extravagance (forbidden)'
            },
            
            'zakat_calculator': {
                'nisab': '85g gold (~£4,445) or 595g silver (~£405) - use silver (lower, benefits poor)',
                'rate': '2.5%',
                'hawl': 'One lunar year (354 days) above nisab',
                'zakatable_assets': 'Cash, gold/silver, investments, business inventory',
                'non_zakatable': 'Primary residence, personal car, household items'
            },
            
            'key_features_islamic_basis': {
                'balance_algorithm': 'Quran 25:67 - measure deviation from middle path',
                'israf_detection': 'Quran 6:141 - flag wasteful spending',
                'charity_privacy': 'Hadith Bukhari 660 - "left hand not knowing" privacy protection',
                'monthly_reflection': 'Hadith Tirmidhi 2417 - prepare for Judgment Day questions'
            },
            
            'business_model': 'Freemium (free basic + paid premium) - no ads',
            'justification': 'Financial tools can be monetized; users expect to pay for financial apps'
        },
        
        'rizq_job_platform': {
            'quranic_foundation': [
                'Quran 67:15 - Walk earth seeking provision',
                'Quran 62:10 - Disperse after prayer seeking bounty',
                'Quran 4:32 - Don\'t envy others, ask Allah for your provision'
            ],
            
            'hadith_foundation': [
                'Bukhari 2072 - Best food is what you earn with hands',
                'Muslim 997 - Start with yourself, then dependents',
                'Bukhari/Muslim - Upper hand (giving) better than lower hand (receiving)'
            ],
            
            'halal_verification': {
                'clearly_haram': 'Alcohol, gambling, pork, interest-based finance, adult entertainment',
                'questionable': 'Music industry, mixed operations companies, conventional banks (indirect roles)',
                'halal': 'Clearly permissible industries with ethical operations'
            },
            
            'employment_ethics': {
                'contract_clarity': 'Quran 2:282 - Written, clear terms',
                'timely_payment': 'Hadith Ibn Majah 2443 - Pay before sweat dries',
                'worker_dignity': 'Hadith Bukhari 2545 - Workers are your brothers',
                'fair_treatment': 'No exploitation, safe conditions, reasonable workload'
            },
            
            'modern_work_guidance': {
                'non_muslim_employers': 'Permissible (Prophet worked for Khadijah)',
                'mixed_gender': 'Permissible with Islamic boundaries',
                'freelancing': 'Permissible with clear contracts',
                'gig_economy': 'Generally permissible, avoid haram deliveries if possible'
            },
            
            'business_model': 'Freemium for job seekers + B2B (employers pay) - no ads',
            'justification': 'Job platforms monetize through employers; halal verification is valuable service'
        },
        
        'cross_cutting_principles': {
            'economic_justice': [
                'Fair measurement/pricing (Quran 83:1-3)',
                'No exploitation (Quran 11:85)',
                'Transparency in transactions (Quran 2:282)',
                'No cheating (Hadith Muslim 102)'
            ],
            
            'technology_ethics': {
                'charging_for_islamic_software': 'Permissible - you\'re charging for service/tool, not knowledge itself',
                'freemium_preferred': 'Free basic access + paid premium = ideal model',
                'ads_vs_subscriptions': 'Subscriptions more Islamic (direct payment, no haram ad risk)',
                'data_privacy': 'User data is amanah (trust) - protect rigorously, be transparent'
            },
            
            'business_models': {
                'most_islamic': 'Direct payment (subscription/purchase)',
                'acceptable': 'Halal ads with transparency',
                'ideal': 'Freemium (free basic + paid premium) with community sponsorship options',
                'avoid': 'Haram ads, deceptive practices, data exploitation'
            }
        },
        
        'implementation_priorities': {
            'must_have': [
                'Halal verification for all features',
                'Privacy protection (encryption, user control)',
                'Transparent pricing and terms',
                'Quranic verses/hadith integrated throughout UI',
                'Islamic categorization (spending, jobs)',
                'Easy account deletion'
            ],
            
            'should_have': [
                'Freemium model with clear value tiers',
                'Community sponsorship features',
                'Educational content (Islamic finance, halal work)',
                'User testimonials and success stories',
                'Dua and reminder features'
            ],
            
            'nice_to_have': [
                'Multilingual (especially Arabic)',
                'Islamic calendar integration',
                'Charity/sadaqah tracking and privacy',
                'Mentorship matching',
                'Skills training courses'
            ]
        },
        
        'competitive_advantage': {
            'unique_value': 'ONLY platform built on authentic Islamic scholarship from day one',
            'differentiation': [
                'Every feature backed by Quran/Sunnah',
                'Halal verification, not just claims',
                'Privacy as Islamic amanah, not just compliance',
                'Community over competition mindset',
                'Empowerment (upper hand) philosophy'
            ],
            'target_market': 'Muslims seeking to align their economic lives with Islam',
            'market_size': '1.8 billion Muslims globally, millions in UK/West'
        },
        
        'success_metrics': {
            'impact_metrics': [
                'Muslims avoiding haram income',
                'Muslims achieving balanced spending',
                'Muslims fulfilling zakat obligation',
                'Muslims moving from "lower hand" to "upper hand"',
                'Families with barakah in finances'
            ],
            
            'business_metrics': [
                'User growth',
                'Premium conversion rate',
                'User satisfaction (NPS score)',
                'Community sponsorship uptake',
                'Platform sustainability'
            ],
            
            'spiritual_metric': 'Are we serving Allah and serving the ummah? If yes, continue. If no, pivot.'
        }
    }
FINAL MESSAGE TO DEVELOPMENT TEAM
def final_guidance_for_development_team():
    """
    Closing thoughts and guidance for the development journey ahead
    """
    
    return {
        'core_conviction': {
            'primary': 'You are not just building apps. You are building tools that help Muslims live Islam.',
            'responsibility': 'Every line of code should serve Allah and serve the ummah.',
            'intention': 'Make your niyyah (intention): "I code this to help Muslims achieve Quranic balance and halal provision"',
            'reward': 'If even one Muslim avoids riba, finds halal income, or fulfills zakat because of your work, it\'s sadaqah jariyah.'
        },
        
        'when_making_decisions': {
            'decision_framework': [
                '1. What does Quran/Sunnah say?',
                '2. What do scholars say?',
                '3. What serves the user\'s Islam best?',
                '4. What would the Prophet ﷺ approve of?',
                '5. Can I stand before Allah and defend this choice?'
            ],
            
            'when_tempted_to_compromise': {
                'scenario': 'Pressure to add haram ads, lower standards, collect excessive data for profit',
                'remember': [
                    'Quran 18:28 - "Do not obey one whose heart We have made heedless of Our remembrance"',
                    'Short-term profit < long-term barakah',
                    'One haram feature can nullify entire platform\'s benefit',
                    'Muslims trust you - don\'t betray that amanah'
                ],
                'guidance': 'If a feature requires compromising Islam, don\'t build it. Find halal alternative or skip it.'
            }
        },
        
        'technical_excellence_as_worship': {
            'principle': 'Ihsan (excellence) applies to code too',
            'hadith': 'Bayhaqi - "Allah loves that when you do something, you do it with excellence"',
            'application': [
                'Write clean, maintainable code',
                'Test thoroughly',
                'Fix bugs promptly',
                'Optimize performance',
                'Design intuitive UX',
                'Document clearly'
            ],
            'reasoning': 'Poor quality code that frustrates users or loses their data is betraying the amanah'
        },
        
        'community_over_profit': {
            'reminder': 'Success is not just revenue - it\'s impact',
            'metrics_that_matter': [
                'How many Muslims found halal income?',
                'How many achieved zakat fulfillment?',
                'How many avoided israf?',
                'How many moved from lower hand to upper hand?'
            ],
            'business_sustainability': 'Yes, you need revenue to sustain. But never sacrifice mission for profit.',
            'barakah_principle': 'Prioritize halal and serving ummah → Allah puts barakah in business'
        },
        
        'for_difficult_days': {
            'when_discouraged': {
                'feeling': 'This is too hard. Why not just build normal app?',
                'reminder': [
                    'Quran 94:5-6 - "Indeed with hardship comes ease"',
                    'You chose harder path because it serves Allah',
                    'Every challenge you overcome is reward',
                    'The ummah needs this - don\'t give up'
                ],
                'dua': '"O Allah, You are our Helper and Supporter. Make this work easy and grant it barakah."'
            },
            
            'when_progress_slow': {
                'feeling': 'We\'re not growing fast enough',
                'reminder': [
                    'Quality over speed',
                    'Barakah matters more than numbers',
                    'Prophet ﷺ started with few followers - eventually transformed world',
                    'One user deeply impacted > 1000 users barely engaged'
                ],
                'focus': 'Build something truly valuable. Growth will follow insha\'Allah.'
            },
            
            'when_financially_tight': {
                'feeling': 'We need revenue now. Should we compromise standards?',
                'reminder': [
                    'Quran 65:2-3 - "Whoever fears Allah, He will make a way out and provide from where he doesn\'t expect"',
                    'Halal provision may come slower but has barakah',
                    'Short-term gain from haram = long-term loss',
                    'Make dua, tighten budget, trust Allah'
                ],
                'practical': 'Explore community sponsorship, grants, halal investors before compromising'
            }
        },
        
        'this_research_document': {
            'purpose': 'This 30,000+ word document is your Islamic foundation',
            'use_it': [
                'Reference when designing features',
                'Share with team to align on values',
                'Show to investors to demonstrate depth',
                'Cite in marketing to build trust',
                'Return to it when making tough decisions'
            ],
            'not_final': 'Fiqh evolves with new scenarios. When new questions arise, consult scholars. This is starting point, not end.',
            'scholar_consultation': 'For major features, consult living scholars who understand technology (Sh. Joe Bradford, Sh. Mohammed Elshinawy, Mufti Menk, etc.)'
        },
        
        'dua_for_the_project': {
            'opening': 'Bismillah ar-Rahman ar-Rahim',
            'dua': [
                'Allahumma (O Allah),',
                'Make Mizaan and Rizq purely for Your sake,',
                'Make them means of helping Your servants live Your Shariah,',
                'Grant us sincerity in every feature we build,',
                'Protect us from compromise and temptation,',
                'Place barakah in this work that it benefits millions,',
                'Make it sadaqah jariyah for us,',
                'And grant us halal provision from this project,',
                'Without needing to compromise our deen.',
                'Ameen.'
            ],
            'closing': 'May Allah accept this effort and make it beneficial for the ummah.'
        },
        
        'final_reminder': {
            'ayah': 'Quran 3:26 - "Say: O Allah, Owner of Sovereignty, You give sovereignty to whom You will and You take sovereignty away from whom You will. You honor whom You will and You humble whom You will. In Your hand is all good. Indeed, You are over all things competent."',
            'application': 'Success is from Allah alone. You make effort. He gives results. Trust Him.',
            'closing_thought': 'You are building tools that bridge deen and dunya. The ummah needs this. May Allah make you successful in both worlds. Now go build something remarkable - for His sake. ✨'
        }
    }