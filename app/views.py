from django.shortcuts import render
from analyzer.detector import analyze_logs
from database.db import insert_log, fetch_logs
from alerts.alerts import send_alert
from analyzer.ml_model import detect_anomaly


import requests
import re


# 🌍 Extract IP from log
def extract_ip(log):
    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', log)
    return match.group(0) if match else None


# 🌍 Get IP details
def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        return requests.get(url).json()
    except:
        return {}


def index(request):
    return render(request, "index.html")


def analyze(request):
    if request.method == "POST":
        log_input = request.POST.get("log")

        # 🔍 Rule-based detection
        result = analyze_logs([log_input])[0]

        # 🤖 AI anomaly detection
        anomaly = detect_anomaly([log_input])[0]
        if anomaly == -1:
            result["threat"] = "Anomaly Detected (AI)"

        # 💾 Save to DB
        insert_log(result["log"], result["threat"])

        # 🚨 Send alert
        if result["threat"] != "Normal":
            send_alert(f"Threat Detected: {result['threat']}")

        # 🌍 IP tracking
        ip = extract_ip(log_input)
        ip_info = get_ip_info(ip) if ip else {}

        return render(request, "result.html", {
            "result": result,
            "ip": ip_info
        })


def view_logs(request):
    logs = fetch_logs()
    return render(request, "logs.html", {"logs": logs})

