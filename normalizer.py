
def normalize(deal):

    return {
        "title": deal.get("title", ""),
        "price": int(deal.get("price", 999999)),
        "destination": deal.get("destination", ""),
        "link": deal.get("link", ""),
        "source": deal.get("source", "")
    }
