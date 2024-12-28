import json
import os
import re
import typing

from src.utils import get_data_from_excel

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.xlsx"))

transactions = get_data_from_excel(file_path)


def data_search(transactions: list, search_str: str) -> typing.Any:
    """Принимает на вход список словарей с банковскими операциями и строку для поиска, возвращает список банковских
    операций, где есть данная строка"""

    result = []
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    for el in transactions:
        for v in el.values():
            if (
                isinstance(v, str)
                and pattern.search(v)
                and search_str in el["Категория"]
                or search_str in el["Описание"]
            ):
                result.append(el)

    return json.dumps(result, ensure_ascii=False, indent=4)


# a = data_search(transactions, 'Ж/д билеты')
# print(a)
