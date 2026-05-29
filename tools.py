import knowledge


def explain_visa_term(term : str, **kwargs):
    """Explain an immigration term like OPT, EAD, CPT, H1B, I-20"""
    term = term.upper()
    if term in knowledge.GLOSSARY:
        return knowledge.GLOSSARY[term]
    else:
        return "TERM Not Found!"


def check_deadline(term: str, **kwargs):
    """Check the deadline"""
    term = term.upper()
    if term.startswith("OPT"):
        return knowledge.OPT_INFO["application_window"]
    else:
        return "TERM Not Found!"


def check_work_eligibility(term: str, **kwargs):
    """Check work eligibility"""
    keys = ["who_is_eligible", "types", "duration", ]
    if term.upper() == "OPT":
        return {k: knowledge.OPT_INFO[k] for k in keys if k in knowledge.OPT_INFO}
    elif term.upper() == "CPT":
        return {k: knowledge.CPT_INFO[k] for k in keys if k in knowledge.CPT_INFO}
    elif term.upper() == "H1B":
        return {k: knowledge.H1B_INFO[k] for k in keys if k in knowledge.H1B_INFO}
    else:
        return "TERM Not Found!"

def track_document_status(term: str, **kwargs):
    """Track the status of immigration documents"""
    keys = ["required_documents", "important_rules"]
    if term.upper() == "OPT":
        return {k: knowledge.OPT_INFO[k] for k in keys}
    elif term.upper() == "CPT":
        return {k: knowledge.CPT_INFO[k] for k in keys}
    elif term.upper() == "H1B":
        return {k: knowledge.H1B_INFO[k] for k in keys}
    else:
        return "TERM Not Found!"

def get_timeline(term: str, **kwargs):
    """Get the timeline"""
    keys = ["processing_time", "application_window", "duration"]
    if term.upper() == "OPT":
        return {k: knowledge.OPT_INFO[k] for k in keys if k in knowledge.OPT_INFO}
    elif term.upper() == "CPT":
        return {k: knowledge.CPT_INFO[k] for k in keys if k in knowledge.CPT_INFO}
    elif term.upper() == "H1B":
        return {k: knowledge.H1B_INFO[k] for k in keys if k in knowledge.H1B_INFO}
    else:
        return "TERM Not Found!"
