from telebot import TeleBot
import json
import os

BOT_TOKEN = "7972514287:AAGLTVQgvgXfeywWmsXpsYegNVB_YmpFkjk"
bot = TeleBot(BOT_TOKEN)
DATA_FILE = "users.json"

def save_user(chat_id):
    users = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    if chat_id not in users:
        users.append(chat_id)
        with open(DATA_FILE, "w") as f:
            json.dump(users, f)
        print(f"🟢 New user added! Total users: {len(users)}")

@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print(f"✅ Deleted join message in {message.chat.title}")
    except Exception as e:
        print(f"❌ Error deleting join message: {e}")

@bot.message_handler(content_types=['left_chat_member'])
def delete_left_message(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print(f"✅ Deleted left message in {message.chat.title}")
    except Exception as e:
        print(f"❌ Error deleting left message: {e}")

@bot.message_handler(commands=['start'])
def handle_start(message):
    save_user(message.chat.id)
    bot.reply_to(message, "Welcome! 👋 I'm your Join Left Clean Bot — keeping your group clean automatically!")

@bot.message_handler(commands=['stats'])
def handle_stats(message):
    total_users = 0
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
        total_users = len(users)
    formatted_count = "{:,}".format(total_users)
    stats_message = f"JOIN LEFT CLEAN BOT\n📊 Total users using this bot: {formatted_count}\n\nKeep your groups clean effortlessly! ✨"
    bot.reply_to(message, stats_message)

print("🤖 Bot is running...")
bot.infinity_polling()
