from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

def fetch_all_data():
    conn = sqlite3.connect("health_data.db")
    c = conn.cursor()
    c.execute("SELECT timestamp, heart_rate FROM health")
    rows = c.fetchall()
    conn.close()
    return rows

@app.route("/get_data")
def get_data():
    return jsonify(fetch_all_data())

@app.route("/latest")
def latest():
    row = fetch_all_data()[-1]
    timestamp, bpm = row
    status = "Low" if bpm < 50 else ("High" if bpm > 120 else "Normal")
    return jsonify({"timestamp": timestamp, "bpm": bpm, "status": status})

@app.route("/dashboard")
def dashboard():
    data = fetch_all_data()
    results = []
    for timestamp, bpm in data:
        status = "Low" if bpm < 50 else ("High" if bpm > 120 else "Normal")
        results.append({"timestamp": timestamp, "bpm": bpm, "status": status})
    return render_template("dashboard.html", data=results)

if __name__ == "__main__":
    app.run(debug=True)
