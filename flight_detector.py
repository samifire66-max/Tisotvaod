HOTEL_WORDS = [
    "hotel",
    "hostel",
    "resort",
    "apartment",
    "apartments",
    "villa",
    "spa",
    "suite",
    "double room",
    "room",
    "accommodation",
    "premier inn",
    "intercontinental",
    "leonardo",
    "eurostars",
]

NOT_FLIGHT_WORDS = [
    "train",
    "rail",
    "railway",
    "express",
    "cruise",
    "ferry",
]

FLIGHT_WORDS = [
    "flight",
    "flights",
    "airfare",
    "fare",
    "round trip",
    "return",
    "non-stop",
    "nonstop",
    "direct flight",
    "ryanair",
    "wizz",
    "wizzair",
    "easyjet",
    "pegasus",
    "el al",
    "aegean",
    "lufthansa",
    "boarding",
]


def is_flight(text: str) -> bool:
    if not text:
        return False

    text = text.lower()

    for word in HOTEL_WORDS:
        if word in text:
            return False

    for word in NOT_FLIGHT_WORDS:
        if word in text:
            return False

    for word in FLIGHT_WORDS:
        if word in text:
            return True

    return False
