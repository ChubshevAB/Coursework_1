import json
import os

from src.simple_search import data_search
from src.utils import get_data_from_excel

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.xlsx"))

transactions = get_data_from_excel(file_path)

expected_result = {
    "Дата операции": "29.12.2021 22:32:24",
    "Дата платежа": "30.12.2021",
    "Номер карты": "*4556",
    "Статус": "OK",
    "Сумма операции": -1411.4,
    "Валюта операции": "RUB",
    "Сумма платежа": -1411.4,
    "Валюта платежа": "RUB",
    "Кэшбэк": 70.0,
    "Категория": "Ж/д билеты",
    "MCC": 4112.0,
    "Описание": "РЖД",
    "Бонусы (включая кэшбэк)": 70,
    "Округление на инвесткопилку": 0,
    "Сумма операции с округлением": 1411.4,
}


def test_data_search() -> None:

    json_result = data_search(transactions, "Ж/д билеты")

    result = json.loads(json_result)

    assert expected_result in result
