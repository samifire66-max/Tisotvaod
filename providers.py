from rss_provider import get_rss_deals
from relevance import is_relevant


def get_all_deals():

    deals = []

    rss = get_rss_deals()

    for deal in rss:

        if is_relevant(deal.title):

            deals.append(deal)

    return deals
