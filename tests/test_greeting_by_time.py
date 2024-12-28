from src.utils import greeting_by_time


def test_greeting_morning() -> None:
    # Тестируем утреннее приветствие
    date_string = "2023-10-01 09:00:00"
    expected_greeting = "Доброе утро"

    result = greeting_by_time(date_string)

    assert result == expected_greeting


def test_greeting_day() -> None:
    # Тестируем дневное приветствие
    date_string = "2023-10-01 15:00:00"
    expected_greeting = "Добрый день"

    result = greeting_by_time(date_string)

    assert result == expected_greeting


def test_greeting_evening() -> None:
    # Тестируем вечернее приветствие
    date_string = "2023-10-01 20:00:00"
    expected_greeting = "Добрый вечер"

    result = greeting_by_time(date_string)

    assert result == expected_greeting


def test_greeting_night() -> None:
    # Тестируем ночное приветствие
    date_string = "2023-10-01 23:30:00"
    expected_greeting = "Доброй ночи"

    result = greeting_by_time(date_string)

    assert result == expected_greeting
