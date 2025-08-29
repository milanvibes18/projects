from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

DB_FILE = "digital_twin.db"


def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/devices")
def get_devices():
    conn = get_db_connection()
    devices = conn.execute("SELECT * FROM devices").fetchall()
    conn.close()
    return jsonify([dict(d) for d in devices])


@app.route("/get_data")
def get_data():
    conn = get_db_connection()
    data = conn.execute(
        "SELECT * FROM device_data ORDER BY timestamp DESC LIMIT 10"
    ).fetchall()
    conn.close()
    return jsonify([dict(d) for d in data])


@app.route("/latest")
def latest():
    conn = get_db_connection()
    latest_data = conn.execute(
        "SELECT * FROM device_data ORDER BY timestamp DESC LIMIT 1"
    ).fetchone()
    conn.close()
    return jsonify(dict(latest_data)) if latest_data else jsonify({})


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
