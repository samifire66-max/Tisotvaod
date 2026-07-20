from rss_provider import get_rss_deals


def get_all_deals():

    deals = []

    deals.extend(get_rss_deals())

    return deals
