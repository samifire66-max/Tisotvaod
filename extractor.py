import re

PRICE_REGEX = re.compile(
    r"(₪|\$|€|£)\s?(\d+(?:,\d{3})?)|(\d+(?:,\d{3})?)\s?(₪|\$|€|£)",
    re.IGNORECASE,
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
    "abu dhabi": "Abu Dhabi",
    "madeira": "Madeira",
    "malta": "Malta",
    "crete": "Crete",
    "heraklion": "Heraklion",
    "rhodes": "Rhodes",
    "sicily": "Sicily",
    "catania": "Catania",
    "palermo": "Palermo",
}

TLV_PATTERNS = (
    "tlv",
    "tel aviv",
    "ben gurion",
    "ben-gurion",
    "israel",
    "from israel",
    "departing israel",
    "departing tel aviv",
    "from tel aviv",
)


def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<[^>]+>", " ", text).lower()


def extract_price(text):

    text = clean_text(text)

    m = PRICE_REGEX.search(text)

    if not m:
        return None, None

    if m.group(1):
        return int(m.group(2).replace(",", "")), m.group(1)

    return int(m.group(3).replace(",", "")), m.group(4)


def extract_destination(text):

    text = clean_text(text)

    found = []

    for key, value in DESTINATIONS.items():
        if key in text:
            found.append((text.index(key), value))

    if not found:
        return None

    found.sort()

    return found[0][1]


def has_tlv(text):

    text = clean_text(text)

    return any(pattern in text for pattern in TLV_PATTERNS)
