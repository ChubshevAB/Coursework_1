import json

from src.views import generate_response


transactions_data = [
    {
        "Номер карты": 1234567812345678,
        "Сумма операции": -1000,
        "Валюта операции": "RUB",
        "Статус": "OK",
        "Категория": "Покупка"
    },
    {
        "Номер карты": 1234567812345678,
        "Сумма операции": -500,
        "Валюта операции": "RUB",
        "Статус": "OK",
        "Категория": "Покупка"
    },
    {
        "Номер карты": 1234567812345678,
        "Сумма операции": 1500,
        "Валюта операции": "RUB",
        "Статус": "OK",
        "Категория": "Переводы"
    },
    {
        "Номер карты": 8765432187654321,
        "Сумма операции": -100,
        "Валюта операции": "RUB",
        "Статус": "OK",
        "Категория": "Покупка"
    },
    {
        "Номер карты": 8765432187654321,
        "Сумма операции": -250,
        "Валюта операции": "USD",
        "Статус": "OK",
        "Категория": "Покупка"
    },
]

expected_response = [
    {
        "last_digits": "5678",
        "total_spent": 1500,
        "cashback": 15.00,
    },
    {
        "last_digits": "4321",
        "total_spent": 100,
        "cashback": 1.00,
    }
]

def test_generate_response() -> None:
    response = generate_response(transactions_data)
    response_data = json.loads(response)
    assert response_data == expected_response
