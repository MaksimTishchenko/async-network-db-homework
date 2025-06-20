# Async Network & DB Homework

Проект по выполнению домашнего задания "Асинхронная работа с сетью и БД".

## 🧾 Описание

Этот проект демонстрирует:
- Асинхронную загрузку данных с [JSONPlaceholder](https://jsonplaceholder.typicode.com) 
- Обработку и сохранение данных в базу данных (SQLite или PostgreSQL)
- Использование SQLAlchemy 2.0+ с асинхронным движком
- Параллельные запросы через `asyncio.gather`
- ORM-модели `User` и `Post` с отношениями

## 🛠 Технологии

- Python 3.11+
- `aiohttp` — для асинхронных HTTP-запросов
- `SQLAlchemy >= 1.4` — для работы с базой данных
- `asyncpg` (опционально) — для PostgreSQL
- `aiosqlite` — если используется SQLite
- `pytest` — для тестирования

## 📁 Структура проекта

- homework_04/
- ├── main.py # Точка входа, запуск всей программы
- ├── models.py # Модели SQLAlchemy + engine
- ├── jsonplaceholder_requests.py # Запросы к API
- ├── init .py # Пакетный файл
- └── requirements.txt # Зависимости


## 🚀 Установка и запуск

### 1. Установите зависимости

pip install -r requirements.txt

### 2. Запустите программу 

cd homework_04
python main.py
