from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)


def get_db():
    max_retries = 10
    for i in range(max_retries):
        try:
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "mysql-service"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "password123"),
                database=os.getenv("DB_NAME", "myapp"),
            )
        except mysql.connector.Error as err:
            if i < max_retries - 1:
                time.sleep(2)
                continue
            raise err


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/api/users", methods=["GET"])
def get_users():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, created_at FROM users ORDER BY id DESC")
        users = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.json or {}
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()

        if not name or not email:
            return jsonify({"error": "name and email are required"}), 400

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email),
        )
        db.commit()
        user_id = cursor.lastrowid
        cursor.close()
        db.close()
        return jsonify({"id": user_id, "message": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
