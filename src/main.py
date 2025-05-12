from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

acc_num = "73654103330135874305"
card_num = "1234567812345678"

check_data = "2024-03-11T02:26:18.671407"
card = "Visa Platinum 8990922113665229"


if __name__ == "__main__":

    print(get_mask_card_number(card_num))
    print(get_mask_account(acc_num))

    print(mask_account_card(card))
    print(get_date(check_data))

    print(filter_by_state(transactions))
    print(sort_by_date(transactions))
