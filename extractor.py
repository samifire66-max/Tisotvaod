import re

PRICE_REGEX = re.compile(r"(₪|\$|€|£)\s?(\d+)|(\d+)\s?(₪|\$|€|£)")

DESTINATIONS = [
    "rome",
    "milan",
    "athens",
    "larnaca",
    "paphos",
    "prague",
    "budapest",
    "vienna",
    "berlin",
    "paris",
    "london",
    "barcelona",
    "madrid",
    "lisbon",
    "amsterdam",
    "dubai"
]


def extract_price(title):

    m = PRICE_REGEX.search(title)

    if not m:
        return None, None

    if m.group(1):
        return int(m.group(2)), m.group(1)

    return int(m.group(3)), m.group(4)


def extract_destination(title):

    t = title.lower()

    for city in DESTINATIONS:

        if city in t:
            return city.title()

    return None
