import re

def detect_threat(log):
    log = log.lower()

    if "failed password" in log:
        return "Brute Force Attack"

    elif re.search(r"(select|drop|insert|or 1=1)", log):
        return "SQL Injection Attempt"

    elif "404" in log:
        return "Scanning Activity"

    elif "unauthorized" in log:
        return "Unauthorized Access"

    return "Normal"


def analyze_logs(log_list):
    results = []

    for log in log_list:
        threat = detect_threat(log)

        results.append({
            "log": log,
            "threat": threat
        })

    return results