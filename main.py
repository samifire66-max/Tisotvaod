from providers import get_all_deals
from telegram import send_message
from relevance import score
from settings import SEARCH


def build_message(deal):

    lines = []

    lines.append(f"✈️ {deal.title}")

    if deal.destination:
        lines.append(f"📍 יעד: {deal.destination}")

    if deal.price:
        lines.append(f"💰 מחיר: {deal.price}")

    lines.append(f"⭐ ציון: {score(deal)}")

    if deal.source:
        lines.append(f"📰 מקור: {deal.source}")

    if deal.link:
        lines.append("")
        lines.append(deal.link)

    return "\n".join(lines)


def remove_duplicates(deals):

    unique = {}
    result = []

    for deal in deals:

        key = ""

        if deal.link:
            key = deal.link.strip().lower()

        elif deal.title:
            key = deal.title.strip().lower()

        if key in unique:
            continue

        unique[key] = True
        result.append(deal)

    return result


def sort_deals(deals):

    return sorted(
        deals,
        key=lambda d: (
            score(d),
            d.price if d.price else 999999
        ),
        reverse=True,
    )


def main():

    deals = get_all_deals()

    deals = remove_duplicates(deals)

    deals = sort_deals(deals)

    if not deals:
        send_message("לא נמצאו עסקאות רלוונטיות.")
        return

    sent = 0

    for deal in deals:

        if score(deal) < 60:
            continue

        send_message(build_message(deal))

        sent += 1

        if sent >= SEARCH["max_results"]:
            break

    print(f"Sent {sent} deals")


if __name__ == "__main__":
    main()
        
        sent += 1

    print(f"Sent {sent} deals")


if __name__ == "__main__":
    main()
