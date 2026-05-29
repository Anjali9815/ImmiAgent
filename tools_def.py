TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "explain_visa_term",
            "description": "Explain an immigration term like OPT, EAD, CPT, H1B, I-20, SEVIS, DSO. Use this when the user asks what something means.",
            "parameters": {
                "type": "object",
                "properties": {
                    "term": {
                        "type": "string",
                        "description": "The immigration term to explain"
                    }
                },
                "required": ["term"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_deadline",
            "description": "Check application deadlines and timelines for a visa type. Use this when the user asks about deadlines, when to apply, or how early/late they can file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "term": {
                        "type": "string",
                        "description": "The visa type to check deadlines for (e.g. OPT, CPT)"
                    }
                },
                "required": ["term"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_work_eligibility",
            "description": "Check who is eligible to work under a specific visa type. Use this when the user asks if they are eligible, who can work, or about work authorization requirements.",
            "parameters": {
                "type": "object",
                "properties": {
                    "term": {
                        "type": "string",
                        "description": "The visa type to check eligibility for (e.g. OPT, CPT, H1B)"
                    }
                },
                "required": ["term"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "track_document_status",
            "description": "Get the list of required documents and important rules for a visa type. Use this when the user asks what documents they need, what paperwork to prepare, or about document requirements.",
            "parameters": {
                "type": "object",
                "properties": {
                    "term": {
                        "type": "string",
                        "description": "The visa type to get document info for (e.g. OPT, CPT, H1B)"
                    }
                },
                "required": ["term"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_timeline",
            "description": "Get the full timeline including processing time, application window, and duration for a visa type. Use this when the user asks how long something takes, when to apply, or about the process timeline.",
            "parameters": {
                "type": "object",
                "properties": {
                    "term": {
                        "type": "string",
                        "description": "The visa type to get timeline for (e.g. OPT, CPT, H1B)"
                    }
                },
                "required": ["term"]
            }
        }
    }
]