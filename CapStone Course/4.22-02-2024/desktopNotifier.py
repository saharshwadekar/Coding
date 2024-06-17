import random
import datetime
import time
from plyer import notification

quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The best way to predict the future is to create it. - Peter Drucker",
]

def show_notification():
    quote = random.choice(quotes)

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    message = f"Quote of the day:\n\n{quote}\n\nDate: {current_date}"

    notification.notify(
        title="Random Quote",
        message=message,
        timeout=10 
    )

while True:
    show_notification()
    time.sleep(5)