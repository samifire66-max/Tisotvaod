import re

PRICE_REGEX = re.compile(
    r"(₪|\$|€|£)\s?(\d+(?:,\d{3})?)|(\d+(?:,\d{3})?)\s?(₪|\$|€|£)"
)

DESTINATIONS = {
    "rome": "Rome",
    "milan": "Milan",
    "bergamo": "Milan",
    "athens": "Athens",
    "thessaloniki": "Thessaloniki",
    "larnaca": "Larnaca",
    "paphos": "Paphos",
    "prague": "Prague",
    "budapest": "Budapest",
    "vienna": "Vienna",
    "berlin": "Berlin",
    "munich": "Munich",
    "frankfurt": "Frankfurt",
    "paris": "Paris",
    "nice": "Nice",
    "london": "London",
    "manchester": "Manchester",
    "barcelona": "Barcelona",
    "madrid": "Madrid",
    "lisbon": "Lisbon",
    "porto": "Porto",
    "amsterdam": "Amsterdam",
    "brussels": "Brussels",
    "warsaw": "Warsaw",
    "krakow": "Krakow",
    "bucharest": "Bucharest",
    "sofia": "Sofia",
    "dubrovnik": "Dubrovnik",
    "zagreb": "Zagreb",
    "split": "Split",
    "naples": "Naples",
    "venice": "Venice",
    "dubai": "Dubai",
    "abu dhabi": "Abu Dhabi"
}


TLV_PATTERNS = [
    "tlv",
    "tel aviv",
    "ben gurion"
]


def extract_price(text):

    if not text:
        return None, None

    m = PRICE_REGEX.search(text)

    if not m:
        return None, None

    if m.group(1):
        value = int(m.group(2).replace(",", ""))
        return value, m.group(1)

    value = int(m.group(3).replace(",", ""))
    return value, m.group(4)


def extract_destination(text):

    if not text:
        return None

    t = text.lower()

    for key, value in DESTINATIONS.items():

        if key in t:
            return value

    return None


def has_tlv(text):

    if not text:
        return False

    t = text.lower()

    return any(x in t for x in TLV_PATTERNS)
