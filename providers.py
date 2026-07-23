from rss_provider import get_rss_deals
from relevance import is_relevant


from rss_provider import get_rss_deals
from relevance import is_relevant


def get_all_deals():

    deals = []

    for deal in get_rss_deals():

        if is_relevant(deal):

            deals.append(deal)

    return deals
