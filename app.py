# app.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/weather')
def weather():
    data = {
        "temperature": round(random.uniform(-10, 35), 1),  # температура від -10 до +35
        "humidity": random.randint(0, 100),                # вологість від 0 до 100
        "status": random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"])  # випадковий стан
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
