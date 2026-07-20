
from normalizer import normalize


def get_rss_deals():

    sample = [
        {
            "title": "Weekend in Cyprus",
            "destination": "Larnaca",
            "price": 3290,
            "link": "https://example.com/deal1",
            "source": "RSS"
        },
        {
            "title": "Weekend in Greece",
            "destination": "Athens",
            "price": 4890,
            "link": "https://example.com/deal2",
            "source": "RSS"
        }
    ]

    return [normalize(x) for x in sample]
