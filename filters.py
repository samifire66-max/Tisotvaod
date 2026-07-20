FLIGHT_KEYWORDS = [

    "flight",
    "flights",
    "airfare",
    "airfares",
    "deal",
    "deals",
    "cheap",
    "fare",
    "roundtrip",
    "round trip",
    "nonstop",
    "direct",

    "טיסה",
    "טיסות",
    "דיל",
    "חופשה"

]


def is_flight_deal(title):

    title = title.lower()

    for word in FLIGHT_KEYWORDS:

        if word.lower() in title:
            return True

    return False
