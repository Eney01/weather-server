from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_sensor_data():
    # Генерація випадкових значень для температури, вологості та тиску
    temperature = round(random.uniform(-10, 40), 2)  # Випадкова температура в діапазоні -10°C до 40°C
    humidity = round(random.uniform(10, 90), 2)      # Випадкова вологість в діапазоні 10% до 90%
    pressure = round(random.uniform(950, 1050), 2)   # Випадковий тиск в діапазоні 950 до 1050 гПа
    return {
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    }

@app.route('/weather', methods=['GET'])
def get_weather_data():
    data = generate_sensor_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
