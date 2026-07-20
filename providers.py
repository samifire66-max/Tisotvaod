from rss_provider import get_rss_deals


def get_all_deals():
    deals = []

    try:
        deals.extend(get_rss_deals())
    except Exception as e:
        print(f"RSS provider failed: {e}")

    return deals
