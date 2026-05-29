import knowledge


def explain_visa_term(term):
    """Explain an immigration term like OPT, EAD, CPT, H1B, I-20"""
    term = term.upper()
    if term in knowledge.GLOSSARY:
        return knowledge.GLOSSARY[term]
    else:
        return "TERM Not Found!"


def check_deadline(term):
    """Check the deadline"""
    term = term.upper()
    if term.startswith("OPT"):
        return knowledge.OPT_INFO["application_window"]
    else:
        return "TERM Not Found!"
print(check_deadline("OPT"))

def check_work_eligibility(term):
    """Check work eligibility"""
    pass

def track_document_status(term):
    """Track the status of immigration documents"""
    pass

def get_timeline(term):
    """Get the timeline"""
    pass




# print(explain_visa_term("opt"))
# print(explain_visa_term("ead"))
# print(explain_visa_term("xyz"))