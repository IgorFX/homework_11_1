from collections.abc import Iterator

def filter_by_currency(data: list[dict], currency: str) -> Iterator[dict]:
    """Функция принимает на вход список словарей и возвращает итератор"""

    for item in data:
        if item.get("operationAmount", 0).get("currency", 0).get("code", 0) == currency:
            print(item)
            yield item


def transaction_descriptions(data: list[dict]) -> Iterator[str]:
    """Функция принимает на вход список словарей и возвращает итератор"""

    for item in data:

        if item.get("description", 0):
            yield item["description"]

    return "Транзакция не имеет описания"


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Функция генерирует номера карт в диапазоне от start до end"""

    for num in range(start, end):

        card_number = f"{num:016d}"

    yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
