# Django Stripe Payment Test Task
Тестовое задание: сервис оформления заказов и оплаты с использованием платежной системы Stripe.
Проект реализован на Django и демонстрирует работу с корзиной, заказами, скидками, налогами и Stripe Checkout.

---

## Стек технологий
- Python 3.10+
- Django
- Stripe API
- SQLite3
- HTML (Django templates)

---

## Функциональность
- Регистрация и авторизация пользователей
- Просмотр списка товаров и страницы товара
- Добавление товаров в корзину
- Создание заказа
- Поддержка скидок и налогов
- Оплата заказа через Stripe Checkout
- Обработка статусов оплаты

---

## Запуск проекта локально
### 1. Клонировать репозиторий
```bash
git clone https://github.com/sergeybogatov194-dev/django-stripe-payment.git
cd django-stripe-payment
```

### 2. Создать и активировать виртуальное окружение
```bash
python -m venv .venv
source .venv/bin/activate  # Linux /macOS
.venv/Scripts/activate  # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Создать и настроить файл .env
Создать файл .env в корне проекта и добавить следующие переменные окружения
- SECRET_KEY
- DEBUG
- STRIPE_PUBLISHABLE_KEY
- STRIPE_SECRET_KEY

### 5. Применить миграции
```bash
python manage.py migrate
```

### 6. Создать суперпользователя (опционально)
```bash
python manage.py createsuperuser
```

### 7. Запустить сервер
```bash
python manage.py runserver
```
### Сервер запустится на http://127.0.0.1:8000

