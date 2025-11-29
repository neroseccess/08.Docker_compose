import os
import time
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "apppass")

def get_conn(retries=20, delay=1):
    for i in range(retries):
        try:
            return psycopg2.connect(
                host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS
            )
        except Exception:
            time.sleep(delay)
    raise RuntimeError("DB not reachable")

@app.get("/")
def index():
    return "OK: Flask is running. Try /health or /db"

@app.get("/health")
def health():
    return jsonify(status="up")

@app.get("/db")
def db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    now = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify(db_time=str(now))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
