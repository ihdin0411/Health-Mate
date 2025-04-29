import csv
from datetime import datetime

def log_vitals(vitals, analysis):
    with open("health_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(),
            vitals['heart_rate'],
            vitals['spo2'],
            vitals['temperature'],
            analysis['status'],
            "; ".join(analysis['alerts'])
        ])
