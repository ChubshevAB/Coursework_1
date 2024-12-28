import json
import os
import typing
from datetime import datetime, timedelta

from src.utils import get_data_from_excel

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.xlsx"))

transactions = get_data_from_excel(file_path)


def spending_by_category(transactions: list, category: str, date=None) -> typing.Any:
    """Функция принимает категорию трат и опционально дату, возвращает информацию о тратах по указанной категории за
    три месяца от указанной даты. Если дата не указана, берется текущаа дата"""

    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, "%d.%m.%Y")

    # Определяем дату три месяца назад
    three_months_ago = date - timedelta(days=90)

    filtered_transactions = []

    # Фильтруем транзакции за последние три месяца по категории
    for transaction in transactions:
        if (
            three_months_ago <= datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S") <= date
            and category == transaction["Категория"]
        ):
            filtered_transactions.append(transaction)

    return json.dumps(filtered_transactions, ensure_ascii=False, indent=4)


# a = spending_by_category(transactions, 'Каршеринг', '31.12.2021')
# print(a)
