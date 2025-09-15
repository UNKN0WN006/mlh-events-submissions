def classify(type, desc):
    # Simple rule-based classifier for demo
    if "phish" in desc.lower():
        return "high"
    if "malware" in desc.lower():
        return "high"
    if "login" in desc.lower():
        return "medium"
    return "low"
