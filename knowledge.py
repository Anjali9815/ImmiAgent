"""
ImmiAgent Knowledge Base
Accurate immigration data for F-1 international students
Source: USCIS.gov
"""

OPT_INFO = {
    "full_form": "Optional Practical Training",
    "description": "Temporary employment authorization for F-1 students directly related to their field of study.",
    "who_is_eligible": "F-1 students who have been enrolled full-time for at least one academic year.",
    "types": {
        "pre_completion": {
            "description": "OPT used before completing your degree.",
            "rules": "Limited to 20 hours/week while school is in session. Full-time during breaks."
        },
        "post_completion": {
            "description": "OPT used after completing your degree.",
            "rules": "Full-time employment (20+ hours/week required).",
            "duration": "12 months"
        }
    },
    "duration": "12 months total",
    "stem_extension": {
        "duration": "24 months additional (36 months total)",
        "eligible_degrees": "STEM designated degree programs only",
        "employer_requirement": "Employer must be enrolled in E-Verify",
        "apply_deadline": "Must apply before initial OPT expires"
    },
    "application_window": {
        "earliest": "90 days before program end date",
        "latest": "60 days after program end date",
        "recommended": "Apply as early as possible. Processing can take 3-5 months."
    },
    "required_documents": [
        "Form I-765 (Application for Employment Authorization)",
        "Form I-20 endorsed by DSO for OPT",
        "Copy of passport (identity page)",
        "Copy of F-1 visa stamp",
        "Copy of most recent I-94 (Arrival/Departure Record)",
        "Two passport-style photos",
        "Filing fee (check USCIS website for current amount)",
        "Copy of any previous EAD cards (if applicable)"
    ],
    "processing_time": "3-5 months (can vary, check USCIS processing times page)",
    "unemployment_limits": {
        "post_completion_opt": "Cannot be unemployed for more than 90 days total",
        "stem_extension": "Cannot be unemployed for more than 150 days total",
        "note": "Unemployment clock starts on your OPT start date, not EAD receipt date."
    },
    "important_rules": [
        "Cannot work before your OPT start date, even if you have the EAD card.",
        "Cannot work before receiving your EAD card.",
        "Must report employer changes to your DSO within 10 days.",
        "Must report address changes to your DSO within 10 days.",
        "Employment must be directly related to your field of study.",
        "Volunteer or unpaid work counts toward employment if related to field of study."
    ]
}

EAD_INFO = {
    "full_form": "Employment Authorization Document",
    "description": "Physical card (Form I-766) that proves you are authorized to work in the United States.",
    "how_to_get": "File Form I-765 with USCIS. For OPT, your DSO must first recommend OPT in SEVIS and issue an updated I-20.",
    "processing_time": "3-5 months typically. Check USCIS processing times for current estimates.",
    "can_work_before_receiving": "No. You cannot begin working until you have the physical EAD card AND your OPT start date has passed.",
    "what_if_delayed": {
        "description": "If your EAD card has not arrived by your OPT start date, you cannot work.",
        "options": [
            "Contact USCIS to check case status at uscis.gov/casestatus",
            "Contact your DSO for guidance",
            "If outside normal processing time, submit an e-Request or call USCIS Contact Center",
            "You may be eligible for expedited processing in certain circumstances"
        ]
    },
    "card_contains": [
        "Your photo",
        "Your name and date of birth",
        "Category (C09P for post-completion OPT)",
        "Valid from / Valid to dates",
        "Card number"
    ],
    "important_rules": [
        "Always carry your EAD card or a copy when working.",
        "If your card is lost or stolen, file a replacement I-765 immediately.",
        "EAD is tied to a specific immigration category. A new EAD is needed if your status changes.",
        "Expired EAD means you must stop working unless a new one is approved or you have a valid extension."
    ]
}

CPT_INFO = {
    "full_form": "Curricular Practical Training",
    "description": "Employment authorization for F-1 students where the work is an integral part of the curriculum (internship, co-op, practicum).",
    "who_is_eligible": "F-1 students who have been enrolled full-time for at least one academic year (exception: graduate students whose program requires immediate CPT).",
    "how_to_get": "Authorized by your DSO through SEVIS. No USCIS application needed.",
    "types": {
        "part_time": "20 hours or less per week. Does NOT affect OPT eligibility.",
        "full_time": "More than 20 hours per week. 12 months of full-time CPT eliminates OPT eligibility."
    },
    "required": [
        "Job offer letter from employer",
        "CPT request form (from your school)",
        "Academic advisor approval",
        "Course registration for the credit tied to CPT"
    ],
    "important_rules": [
        "Must have a job offer before applying.",
        "Must be enrolled in a course that requires or allows CPT.",
        "Cannot start working until CPT authorization is noted on your I-20.",
        "12 months of full-time CPT = no more OPT eligibility.",
        "Part-time CPT does not affect OPT eligibility regardless of duration."
    ]
}

H1B_INFO = {
    "full_form": "H-1B Specialty Occupation Visa",
    "description": "Employer-sponsored work visa for specialty occupation positions requiring at least a bachelor's degree.",
    "who_is_eligible": "Workers in specialty occupations with at least a bachelor's degree (or equivalent) in a related field.",
    "cap": {
        "regular_cap": "65,000 per fiscal year",
        "masters_cap": "Additional 20,000 for US master's degree or higher",
        "cap_exempt": "Universities, nonprofit research orgs, and government research orgs are cap-exempt"
    },
    "lottery": {
        "registration_period": "Usually early March",
        "selection": "Random lottery if registrations exceed cap",
        "results": "Usually announced by end of March",
        "start_date": "October 1 of the fiscal year"
    },
    "opt_to_h1b": {
        "cap_gap": "If your OPT expires before Oct 1 but you have a selected H-1B petition, your OPT and work authorization are automatically extended until Oct 1.",
        "important": "Your employer must file the H-1B petition before your OPT expires for cap-gap to apply."
    },
    "duration": "3 years initially, extendable to 6 years total",
    "important_rules": [
        "Employer must sponsor you. You cannot self-petition.",
        "Employer must pay prevailing wage for the position.",
        "Job must qualify as a specialty occupation.",
        "You are tied to your sponsoring employer. Changing jobs requires a new H-1B petition.",
        "H-1B transfer is possible if you change employers.",
        "Premium processing available (15 business days) for additional fee."
    ]
}

I20_INFO = {
    "full_form": "Certificate of Eligibility for Nonimmigrant Student Status (Form I-20)",
    "description": "Document issued by your school's DSO that certifies your enrollment and F-1 status. Required for visa applications, entry to the US, and employment authorization.",
    "when_you_need_updated_i20": [
        "Applying for OPT or STEM OPT extension",
        "Changing your major or degree level",
        "Transferring schools",
        "Extending your program end date",
        "Changing your funding source",
        "Applying for CPT"
    ],
    "important_rules": [
        "Keep ALL your I-20s. Never throw away old ones.",
        "Your I-20 must be signed (page 1) and not expired for travel.",
        "Travel signature is valid for 1 year (6 months during OPT).",
        "Report any changes (address, employer, major) to your DSO to keep I-20 current."
    ]
}

SEVIS_INFO = {
    "full_form": "Student and Exchange Visitor Information System",
    "description": "Government database that tracks international students and exchange visitors in the US.",
    "sevis_fee": "I-901 SEVIS fee must be paid before your visa interview.",
    "sevis_id": "Your SEVIS ID (starts with N) is on your I-20 in the top left corner. You need it for almost everything.",
    "status_types": [
        "Active — you are in valid F-1 status",
        "Completed — you finished your program",
        "Terminated — your record was ended (serious issue, contact DSO immediately)"
    ]
}

# ─── Common Questions Quick Lookup ───

COMMON_QUESTIONS = {
    "can i work off campus on f1": "Generally no. F-1 students can only work off-campus through CPT, OPT, or in cases of severe economic hardship (requires USCIS approval).",
    "what happens if my opt expires": "You enter a 60-day grace period. During this time you cannot work but can prepare to depart, transfer SEVIS, or change status.",
    "can i be self employed on opt": "Yes, but you must have proper business documentation, work in your field of study, and report it to your DSO.",
    "can i work for multiple employers on opt": "Yes. You can work for multiple employers on OPT. Each must be related to your field of study. Report all employers to your DSO.",
    "what is the 60 day grace period": "After your OPT end date or program completion, you have 60 days to depart the US, transfer to a new school, or change immigration status. You cannot work during this period.",
    "can i travel on opt": "Yes, but you need a valid passport, valid F-1 visa stamp, valid I-20 with travel signature (within 6 months), and your EAD card.",
    "what if i get laid off on opt": "Your unemployment clock starts. You have 90 days of total unemployment allowed on post-completion OPT (150 days on STEM OPT). Update your DSO immediately."
}

# ─── Glossary ───

GLOSSARY = {
    "OPT": "Optional Practical Training — work authorization for F-1 students",
    "EAD": "Employment Authorization Document — your work permit card",
    "CPT": "Curricular Practical Training — work authorization tied to your coursework",
    "H-1B": "Specialty Occupation Visa — employer-sponsored work visa",
    "I-20": "Certificate of Eligibility — your enrollment and status document",
    "DSO": "Designated School Official — your international student advisor",
    "SEVIS": "Student and Exchange Visitor Information System — government tracking database",
    "I-765": "Application for Employment Authorization — the form you file for EAD",
    "I-94": "Arrival/Departure Record — proves your legal entry to the US",
    "I-901": "SEVIS Fee Payment — required before visa interview",
    "SEVP": "Student and Exchange Visitor Program — the program that manages SEVIS",
    "USCIS": "United States Citizenship and Immigration Services",
    "CBP": "Customs and Border Protection — the agency at ports of entry",
    "RFE": "Request for Evidence — USCIS asking for more documents on your case",
    "LCA": "Labor Condition Application — employer files this before H-1B petition",
    "STEM": "Science, Technology, Engineering, Mathematics — qualifies for 24-month OPT extension",
    "E-Verify": "System employers use to verify work authorization. Required for STEM OPT employers.",
    "Cap-Gap": "Automatic extension of OPT if you have a pending or approved H-1B for Oct 1 start"
}