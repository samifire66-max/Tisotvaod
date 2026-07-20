from deal import Deal


def normalize(data):

    return Deal(
        title=data.get("title", ""),
        link=data.get("link", ""),
        source=data.get("source", ""),
        destination=data.get("destination", ""),
        price=data.get("price"),
        published=data.get("published", "")
    )
