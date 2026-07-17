import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "1238261691"


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Telegram message sent.")
    else:
        print("Telegram error:")
        print(response.text)


if __name__ == "__main__":
    send_message(
        "✅ מערכת <b>טיסות ועוד</b> התחברה בהצלחה!\n\n"
        "זוהי הודעת בדיקה ראשונה."
    )
