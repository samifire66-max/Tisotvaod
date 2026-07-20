def normalize(deal):

    return {
        "title": deal.get("title", ""),
        "destination": deal.get("destination", ""),
        "price": deal.get("price", 999999),
        "link": deal.get("link", ""),
        "source": deal.get("source", ""),
        "published": deal.get("published", "")
    }
