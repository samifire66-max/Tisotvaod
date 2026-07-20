from deal import Deal

from extractor import extract_price
from extractor import extract_destination


def normalize(data):

    title = data.get("title", "")

    price, currency = extract_price(title)

    destination = extract_destination(title)

    return Deal(

        title=title,

        link=data.get("link", ""),

        source=data.get("source", ""),

        destination=destination or "",

        price=price,

        published=data.get("published", "")

    )
