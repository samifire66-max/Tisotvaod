import feedparser

from normalizer import normalize
from sources import SOURCES


def get_rss_deals():

    deals = []

    for source in SOURCES:

        feed = feedparser.parse(source["url"])

        if not feed.entries:
            continue

        for entry in feed.entries:

            deal = normalize(
                {
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "source": source["name"],
                    "published": entry.get("published", ""),
                }
            )

            if deal:
                deals.append(deal)

    return deals
