from providers import get_all_deals
from telegram import send_message

deals = get_all_deals()

if not deals:
    send_message("לא נמצאו עסקאות.")
    raise SystemExit()

for deal in deals[:10]:

    send_message(
f"""✈️ עסקה חדשה

{deal["title"]}

מקור:
{deal["source"]}

{deal["link"]}
"""
    )
