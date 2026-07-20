from providers import get_all_deals
from telegram import send_message
from filters import is_flight_deal

deals = get_all_deals()

count = 0

for deal in deals:

    if not is_flight_deal(deal["title"]):
        continue

    count += 1

    send_message(
f"""✈️

{deal["title"]}

מקור:
{deal["source"]}

{deal["link"]}
"""
    )

if count == 0:

    send_message("לא נמצאו עסקאות טיסה.")
