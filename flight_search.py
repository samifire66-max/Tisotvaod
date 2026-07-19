from config import MAX_PRICE
from utils import next_weekend_dates


def search_flights():
    """
    גרסה 0.1 — מחזירה עסקאות לדוגמה.
    בשלב הבא נחבר מקור נתונים אמיתי.
    """

    depart, return_date = next_weekend_dates()

    deals = [
        {
            "destination": "Paphos",
            "airport": "TLV",
            "depart": depart,
            "return": return_date,
            "price": 3680,
            "direct": True,
            "link": "https://example.com/paphos"
        },
        {
            "destination": "Athens",
            "airport": "TLV",
            "depart": depart,
            "return": return_date,
            "price": 4120,
            "direct": True,
            "link": "https://example.com/athens"
        },
        {
            "destination": "Larnaca",
            "airport": "TLV",
            "depart": depart,
            "return": return_date,
            "price": 3290,
            "direct": True,
            "link": "https://example.com/larnaca"
        },
    ]

    filtered = [
        d for d in deals
        if d["price"] <= MAX_PRICE and d["direct"]
    ]

    return filtered
