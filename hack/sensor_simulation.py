import random

def get_vitals():
    def maybe_abnormal(normal_range, abnormal_range, chance=0.2):
        """Randomly return a value from either the normal or abnormal range."""
        if random.random() < chance:
            return random.uniform(*abnormal_range)
        else:
            return random.uniform(*normal_range)

    return {
        "heart_rate": int(maybe_abnormal((60, 100), (40, 130))),  # normal: 60-100 bpm
        "spo2": round(maybe_abnormal((95, 100), (85, 94)), 1),    # normal: 95-100%
        "temperature": round(maybe_abnormal((36.5, 37.5), (35.0, 39.0)), 1)  # normal: 36.5–37.5°C
    }
