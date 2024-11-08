import pytest
from app import app  # Імпортуємо Flask додаток з файлу app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client  # Створюємо клієнт для тестування

def test_weather(client):
    response = client.get('/weather')  # Викликаємо GET запит до ендпоінту /weather
    assert response.status_code == 200  # Перевіряємо, що статус код 200 (успіх)
    data = response.get_json()  # Отримуємо JSON відповідь
    assert "temperature" in data  # Перевіряємо, що в відповіді є температура
    assert "humidity" in data  # Перевіряємо, що в відповіді є вологість
    assert "status" in data  # Перевіряємо, що в відповіді є статус
