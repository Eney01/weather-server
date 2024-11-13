# Вибір базового образу з Python
FROM python:3.9-slim

# Встановлення робочої директорії в контейнері
WORKDIR /app

# Копіюємо файли в контейнер
COPY . .

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт для доступу до сервера
EXPOSE 5000

# Запуск додатку
CMD ["python", "app.py"]
