from providers import get_all_deals
from telegram import send_message
from config import MAX_PRICE

deals = get_all_deals()

count = 0

for deal in deals:

    if deal["price"] > MAX_PRICE:
        continue

    count += 1

    send_message(
        f"""✈️ {deal['destination']}

{deal['title']}

₪{deal['price']}

מקור: {deal['source']}

{deal['link']}
"""
    )

if count == 0:
    send_message("לא נמצאו עסקאות מתאימות.")
