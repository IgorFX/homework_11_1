import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("12345634567", "Неверный номер карты"),
        ("123456781345676565665", "Неверный номер карты"),
        ("12345678abcd5678", "Неверный номер карты"),
        ("", "Отсутствует номер карты"),
    ],
)
def test_get_mask_card_number(value: str, expected: str) -> None:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654103330135874305", "**4305"),
        ("736541033301387405", "Неверный номер счета"),
        ("7365410333013587405", "Неверный номер счета"),
        ("", "Отсутствует номер счета"),
    ],
)
def test_get_mask_account(value: str, expected: str) -> None:
    assert get_mask_account(value) == expected
