from rss_provider import get_rss_deals
from relevance import is_relevant


def get_all_deals():

    all_deals = get_rss_deals()

    print(f"Collected from RSS: {len(all_deals)}")

    relevant = []

    for deal in all_deals:

        if is_relevant(deal):
            relevant.append(deal)

    print(f"Relevant deals: {len(relevant)}")

    return relevant
