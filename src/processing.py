def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    возвращает новый список, отсортированный по дате"""

    new_transactions_list = []

    for item in data:
        if item.get("date", 0):
            new_transactions_list.append(item)

    new_transactions_list.sort(key=lambda x: x["date"], reverse=descending)

    return new_transactions_list


def filter_by_state(data: list[dict], state: str = "CANCELED") -> list:
    """Принимает на вход список словарей возвращает новый список
    словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""

    operations_state = []

    for operation in data:
        if operation.get("state", 0) == state:
            operations_state.append(operation)

    return operations_state