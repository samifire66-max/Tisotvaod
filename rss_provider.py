import feedparser

from normalizer import normalize
from sources import SOURCES


def get_rss_deals():

    deals = []

    for source in SOURCES:

        feed = feedparser.parse(source["url"])

        print(f"Reading {source['name']}")

        if not feed.entries:
               print("  -> 0 entries")
    continue

print(f"  -> {len(feed.entries)} entries")

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
