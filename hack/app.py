from flask import Flask, render_template, jsonify
from sensor_simulation import get_vitals
from health_ai import analyze_health
from logger import log_vitals

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/vitals")
def api_vitals():
    vitals = get_vitals()
    analysis = analyze_health(vitals)
    log_vitals(vitals, analysis)
    return jsonify({**vitals, **analysis})

if __name__ == "__main__":
    app.run(debug=True)
# This is a simple Flask application that simulates health monitoring.  