def get_mask_card_number(str_card_number: str) -> str:
    """Функция принимает номер карты в формате str и возвращает
    в формате str виде XXXX XX** **** XXXX"""

    if len(str_card_number) == 16 and str_card_number.isdigit():
        masked_card_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"
        return masked_card_number
    elif str_card_number == "":
        return "Отсутствует номер карты"

    return "Неверный номер карты"


def get_mask_account(str_account_number: str) -> str:
    """Функция принимает номер счета в int и возвращает
    в формате str в виде **XXXX"""

    if len(str_account_number) == 20 and str_account_number.isdigit():
        masked_account_number = f"**{str_account_number[-4:]}"
        return masked_account_number

    elif str_account_number == "":
        return "Отсутствует номер счета"

    return "Неверный номер счета"
