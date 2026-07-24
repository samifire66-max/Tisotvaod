from flight_detector import is_flight

EUROPE = {
    "Rome",
    "Milan",
    "Athens",
    "Larnaca",
    "Paphos",
    "Prague",
    "Budapest",
    "Vienna",
    "Berlin",
    "Paris",
    "London",
    "Barcelona",
    "Madrid",
    "Lisbon",
    "Amsterdam",
    "Dubrovnik",
    "Sofia",
    "Bucharest",
    "Warsaw",
    "Krakow",
    "Naples",
    "Venice",
}


def score(deal):

    title = (deal.title or "")

    if not is_flight(title):
        return 0

    score = 0

    title_lower = title.lower()

    if "tlv" in title_lower:
        score += 60

    if "tel aviv" in title_lower:
        score += 60

    if "ben gurion" in title_lower:
        score += 60

    if deal.destination in EUROPE:
        score += 30

    if deal.price:

        if deal.price <= 100:
            score += 40
        elif deal.price <= 200:
            score += 30
        elif deal.price <= 300:
            score += 20

    usa = [
        "new york",
        "miami",
        "orlando",
        "chicago",
        "las vegas",
        "los angeles",
        "dallas",
        "houston",
        "san francisco",
    ]

    for city in usa:
        if city in title_lower:
            score -= 100

    return score


def is_relevant(deal):
    return score(deal) >= 60
