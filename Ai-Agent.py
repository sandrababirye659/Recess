from telegram import Bot
TELEGRAM_TOKEN = "7827036191:AAG6YY3NJHHako8MngHiTQxv8PzoASXNjBk"
CHAT_ID = "6817915359"  # Your confirmed chat ID

def post_to_telegram():
    print(f"➡ Using TOKEN: {TELEGRAM_TOKEN[:10]}...")
    print(f"➡ Using CHAT_ID: {CHAT_ID}")
    
    bot = Bot(token=TELEGRAM_TOKEN)
    message = "🚀 This is a test message from Babirye's Telegram bot!"
    bot.send_message(chat_id=CHAT_ID, text=message)
    print("✅ Message sent!")

post_to_telegram()