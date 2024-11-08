from flask import Flask

app = Flask(__name__)

@app.route('/weather')
def weather():
    # Мокані дані для тесту
    return {
        "temperature": 22, 
        "humidity": 80, 
        "status": "clear"
    }

if __name__ == '__main__':
    app.run(debug=True)

