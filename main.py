import json
import os

from dotenv import load_dotenv

from src.get_currency_rate import get_currency_rate, load_user_currencies
from src.simple_search import data_search
from src.spending_by_category import spending_by_category
from src.top_transactions import top_transactions
from src.utils import get_data_from_excel, greeting_by_time
from src.value_of_shares import get_price, load_user_currencies_of_share
from src.views import generate_response

load_dotenv()

api_key = os.getenv("apilayer_key")

api_key_share = os.getenv("ALPHA_VANTAGE_API_KEY")

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "operations.xlsx"))

transactions = get_data_from_excel(file_path)

file_path_to_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "user_settings.json"))

user_settings = load_user_currencies(file_path_to_json)

user_settings_for_share = load_user_currencies_of_share(file_path_to_json)


if __name__ == "__main__":

    cards = generate_response(transactions)
    cards_data = json.loads(cards)

    top_transactions = top_transactions(transactions)
    top_transactions_data = json.loads(top_transactions)

    currency_rates = get_currency_rate(api_key, user_settings)
    currency_rates_data = json.loads(currency_rates)

    stock_prices = get_price(user_settings_for_share)
    stock_prices_data = json.loads(stock_prices)

    user_input = input('Для начала работы введите дату и время в формате "год-месяц-день часы:минуты:секунды": ')

    greeting = greeting_by_time(user_input)

    result = {
        "greeting": greeting,
        "cards": cards_data,
        "top_transactions": top_transactions_data,
        "currency_rates": currency_rates_data,
        "stock_prices": stock_prices_data,
    }

    json_result = json.dumps(result, ensure_ascii=False, indent=4)

    print(json_result)

    system_request_simple_search = input("Хотите произвести поиск транзакций(y/n)? ").lower()

    if system_request_simple_search == "y":
        user_simple_search = input(
            "Введите критерий поиска по списку транзакций (поиск осуществляется по наименованию категории или "
            "описанию): "
        )
        simple_search_result = data_search(transactions, user_simple_search)
        print(simple_search_result)

    system_request_search_by_category = input("Хотите сформировать отчет по конкретной категории(y/n)? ").lower()

    if system_request_search_by_category == "y":
        user_search_by_category = input("Введите наименование категории, по которой будет сформирован отчет: ")
        user_search_by_date = input("Введите дату, от которй будет сформирован отчет: ")

        if user_search_by_date != "":
            report_by_category = spending_by_category(transactions, user_search_by_category, user_search_by_date)
            print(report_by_category)
        else:
            report_by_category = spending_by_category(transactions, user_search_by_category)
            print(report_by_category)

    print("Работа программы завершена!")
