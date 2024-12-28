import json
import os

from src.spending_by_category import spending_by_category
from src.utils import get_data_from_excel

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.xlsx"))

expected_result = {
    "Дата операции": "07.12.2021 14:02:27",
    "Дата платежа": "07.12.2021",
    "Номер карты": "*4556",
    "Статус": "OK",
    "Сумма операции": -837.9,
    "Валюта операции": "RUB",
    "Сумма платежа": -837.9,
    "Валюта платежа": "RUB",
    "Кэшбэк": 41.0,
    "Категория": "Ж/д билеты",
    "MCC": 4112.0,
    "Описание": "РЖД",
    "Бонусы (включая кэшбэк)": 41,
    "Округление на инвесткопилку": 0,
    "Сумма операции с округлением": 837.9,
}

transactions = get_data_from_excel(file_path)


def test_spending_by_category() -> None:

    json_result = spending_by_category(transactions, "Ж/д билеты", "29.12.2021")

    result = json.loads(json_result)

    assert expected_result in result
