import feedparser

from normalizer import normalize
from sources import RSS_FEEDS


def get_rss_deals():

    deals = []

    for url in RSS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries:

            deals.append(

                normalize({

                    "title": entry.get("title", ""),

                    "link": entry.get("link", ""),

                    "source": feed.feed.get("title", url),

                    "published": entry.get("published", "")

                })

            )

    return deals
