import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("1234567887654321", "Отсутствует наименование карты(счета)"),
        ("Счет 45878990922113665229", "Счет **5229"),
        ("", "Данные отсутствуют"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_wrong_get_date():
    assert get_date("2024-03-11X02:26:18.671407") == "Некорректный формат даты"