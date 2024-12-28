import json
import os
import typing

import pandas as pd

from src.utils import get_data_from_excel

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.xlsx"))

transactions = get_data_from_excel(file_path)


def top_transactions(transactions: list) -> typing.Any:
    """Принимает на вход датафрейм и возвращает json-ответ:
    Топ-5 транзакций по сумме платежа, где 'Номер карты' не пустой"""

    df = pd.DataFrame(transactions)

    df = df.where(pd.notnull(df), None)
    df.replace("", None, inplace=True)

    df_filtered = df[df["Номер карты"].notnull()]

    top_5 = df_filtered.nlargest(5, "Сумма платежа")

    top_5_filtered = top_5[["Дата платежа", "Сумма платежа", "Категория", "Описание"]]

    return json.dumps(top_5_filtered.to_dict(orient="records"), ensure_ascii=False, indent=4)


# a = top_transactions(transactions)
# print(a)
