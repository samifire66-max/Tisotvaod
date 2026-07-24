from providers import get_all_deals
from telegram import send_message
from relevance import score
from settings import SEARCH


def build_message(deal):

    lines = [
        f"✈️ {deal.title}"
    ]

    if deal.destination:
        lines.append(f"📍 יעד: {deal.destination}")

    if deal.price is not None:
        lines.append(f"💰 מחיר: {deal.price}")

    if deal.source:
        lines.append(f"📰 מקור: {deal.source}")

    lines.append(f"⭐ ציון: {score(deal)}")

    if deal.link:
        lines.append("")
        lines.append(deal.link)

    return "\n".join(lines)


def remove_duplicates(deals):

    seen = set()
    result = []

    for deal in deals:

        key = (
            (deal.link or "").strip().lower(),
            (deal.title or "").strip().lower()
        )

        if key in seen:
            continue

        seen.add(key)
        result.append(deal)

    return result


def main():

    print("========== DEBUG ==========")

    deals = get_all_deals()

    print(f"Deals returned: {len(deals)}")

    if not deals:
        print("No deals found.")
        send_message("❌ לא נמצאו עסקאות.")
        return

    deals = remove_duplicates(deals)

    print(f"After duplicates: {len(deals)}")

    deals.sort(key=score, reverse=True)

    sent = 0

    for deal in deals:

        s = score(deal)

        print(f"[{s}] {deal.title}")

        if s < 60:
            continue

        send_message(build_message(deal))
        sent += 1

        if sent >= SEARCH["max_results"]:
            break

    print(f"Sent {sent} deals")
    print("========== END ==========")


if __name__ == "__main__":
    main()
