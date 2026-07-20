from providers import get_all_deals

from telegram import send_message

from settings import SEARCH

deals = get_all_deals()

count = 0

for deal in deals:

    if count >= SEARCH["max_results"]:
        break

    send_message(

f"""✈️

{deal.title}

מקור:
{deal.source}

{deal.link}
"""

    )

    count += 1

if count == 0:

    send_message("לא נמצאו עסקאות.")
