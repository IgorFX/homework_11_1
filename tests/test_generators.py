import pytest
from src.generators import filter_by_currency
from src.generators import card_number_generator
from src.generators import transaction_descriptions


def test_filter_by_currency_incorrect_currency(full_transactions):
    filtered = filter_by_currency(full_transactions, 'EUR')
    with pytest.raises(StopIteration):
        next(filtered)


def test_filter_by_currency(full_transactions):
    generator = filter_by_currency(full_transactions, 'USD')
    assert next(generator) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}


@pytest.mark.parametrize("start, end, expected", [
    (1, 2, "0000 0000 0000 0001"),
    (41, 42, "0000 0000 0000 0041"),
    (2201, 2202, "0000 0000 0000 2201"),
])
def test_card_number_generator(start, end, expected):
    generator = card_number_generator(start, end)
    assert next(generator) == expected


def test_transaction_descriptions(full_transactions):
    generator = transaction_descriptions(full_transactions)
    assert next(generator) == "Перевод организации"