from providers import get_all_deals
from telegram import send_message
from settings import SEARCH


def build_message(deal):

    message = f"""✈️ {deal.title}
"""

    if deal.destination:
        message += f"\n📍 יעד: {deal.destination}"

    if deal.price:
        message += f"\n💰 מחיר: {deal.price}"

    if deal.source:
        message += f"\n📰 מקור: {deal.source}"

    if deal.link:
        message += f"\n\n{deal.link}"

    return message


def main():

    deals = get_all_deals()

    if not deals:
        send_message("לא נמצאו עסקאות.")
        return

    sent = 0

    for deal in deals:

        if sent >= SEARCH["max_results"]:
            break

        send_message(build_message(deal))

        sent += 1

    print(f"Sent {sent} deals")


if __name__ == "__main__":
    main()
