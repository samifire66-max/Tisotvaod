from telegram import send_message
from flight_search import search_flights
from utils import format_price


def main():
    deals = search_flights()

    if not deals:
        send_message("לא נמצאו עסקאות מתאימות כרגע.")
        return

    for deal in deals:
        message = f"""🔥 נמצאה עסקה!

יעד: {deal["destination"]}
יציאה: {deal["depart"]}
חזרה: {deal["return"]}
שדה: {deal["airport"]}
טיסה ישירה: כן
מחיר כולל: {format_price(deal["price"])}

קישור: {deal["link"]}

5 נוסעים | סוף שבוע"""

        send_message(message)


if __name__ == "__main__":
    main()
