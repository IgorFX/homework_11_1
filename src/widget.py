from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Возвращает название карты(счета) и маскиолваный номер карты(счета)"""

    if len(card) != 0:

        account_card = card.split()

        if account_card[0] == "Счет":
            masked_account = get_mask_account(account_card[1])
            return f"{account_card[0]} {masked_account}"

        elif len(account_card) == 1 and account_card[-1].isdigit():
            return "Отсутствует наименование карты(счета)"

        else:
            if len(account_card) > 2:
                card_name = f"{account_card[0]} {account_card[1]}"

            masked_card = get_mask_card_number(account_card[-1])
    else:
        return "Данные отсутствуют"

    return f"{card_name} {masked_card}"


def get_date(data: str) -> str:
    """Принимает стоку с датой и временем, проверяет на присутствие
    данных и их корректность, и возвращает дату в формате ДД.ММ.ГГ"""

    if len(data) == 26 and "T" in data:
        year = data[:4]
        month = data[5:7]
        day = data[8:10]

    else:
        return "Некорректный формат даты"

    return f"{day}.{month}.{year}"
