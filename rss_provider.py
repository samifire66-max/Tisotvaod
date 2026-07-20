import feedparser
from datetime import datetime
from normalizer import normalize
from config import RSS_FEEDS


def get_rss_deals():

    deals = []

    for feed_url in RSS_FEEDS:

        feed = feedparser.parse(feed_url)

        for entry in feed.entries:

            title = entry.get("title", "")

            link = entry.get("link", "")

            published = entry.get("published", "")

            deal = normalize({
                "title": title,
                "destination": "",
                "price": 999999,
                "link": link,
                "source": feed.feed.get("title", feed_url),
                "published": published
            })

            deals.append(deal)

    return deals
