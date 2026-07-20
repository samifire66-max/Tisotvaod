import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

MAX_PRICE = 4000

ADULTS = 2
CHILDREN = [14, 12, 9]

DIRECT_ONLY = True

AIRPORTS = [
    "TLV",
    "HFA"
]

TRIP_OPTIONS = [
    (3, 4),   # חמישי-ראשון
    (2, 3)    # שישי-ראשון
]
RSS_FEEDS = [
    "https://www.theflightdeal.com/feed/",
    "https://travelfree.info/feed/"
]
