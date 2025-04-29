def analyze_health(vitals):
    alerts = []
    if vitals['heart_rate'] > 100 or vitals['heart_rate'] < 60:
        alerts.append("Abnormal heart rate")
    if vitals['spo2'] < 94:
        alerts.append("Low oxygen saturation")
    if vitals['temperature'] > 37.5:
        alerts.append("Fever detected")

    return {
        "alerts": alerts,
        "status": "OK" if not alerts else "Warning"
    }
