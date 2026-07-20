from providers import get_all_deals
from telegram import send_message

deals = get_all_deals()

if not deals:

    send_message("לא נמצאו עסקאות.")

    raise SystemExit()

for deal in deals[:10]:

    message = f"""✈️ {deal.title}

מקור:
{deal.source}

{deal.link}
"""

    if deal.destination:

        message += f"\nיעד: {deal.destination}"

    if deal.price:

        message += f"\nמחיר: ₪{deal.price}"

    send_message(message)
