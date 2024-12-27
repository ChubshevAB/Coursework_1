import os
import typing
from datetime import datetime

import pandas as pd

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.xlsx"))


def get_data_from_excel(file_path: str) -> list:
    """Принимает на вход путь к файлу в формате xlsx и возвращает список словарей с транзакциями"""

    df = pd.read_excel(file_path)
    result = df.to_dict(orient="records")
    return result


def greeting_by_time(date_string: str) -> typing.Any:
    """Приветствует пользователя в зависимости от времени суток"""

    time = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    hour = time.hour

    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

# a = greeting_by_time('2021-12-31 16:42:04')
# print(a)
