from telebot import TeleBot

# 👉 এখানে তোমার BotFather থেকে পাওয়া টোকেন বসাও
BOT_TOKEN = "7972514287:AAGLTVQgvgXfeywWmsXpsYegNVB_YmpFkjk"

bot = TeleBot(BOT_TOKEN)

# 🧹 কেউ গ্রুপে join করলে message delete করবে
@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print(f"✅ Deleted join message in {message.chat.title}")
    except Exception as e:
        print(f"❌ Error deleting join message: {e}")

# 🧹 কেউ গ্রুপ থেকে leave করলে message delete করবে
@bot.message_handler(content_types=['left_chat_member'])
def delete_left_message(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print(f"✅ Deleted left message in {message.chat.title}")
    except Exception as e:
        print(f"❌ Error deleting left message: {e}")

print("🤖 Bot is running...")
bot.infinity_polling()
