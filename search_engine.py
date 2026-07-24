from telegram import send_message


class SearchEngine:

    def __init__(self):
        self.deals = []

    def add_deals(self, deals):
        if deals:
            self.deals.extend(deals)

    def filter_deals(self):
        filtered = []

        for deal in self.deals:
            price = deal.get("price", 999999)

            if price <= 42000:
                filtered.append(deal)

        return filtered

    def notify(self):

        deals = self.filter_deals()

        if not deals:
            print("No matching deals found.")
            return

        for deal in deals:

            message = (
                f"✈ יעד: {deal['destination']}\n"
                f"💰 מחיר: ₪{deal['price']}\n"
                f"🏨 {deal['hotel']}\n"
                f"⭐ {deal['rating']}\n"
                f"🔗 {deal['url']}"
            )

            send_message(message)
