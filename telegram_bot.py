from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import json

with open("config.json", "r") as f:
    config = json.load(f)

admin_users = config.get("admin_users", [])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in admin_users:
        await update.message.reply_text("Merhaba, ben DOMDOM. Sorularını bekliyorum.")
    else:
        await update.message.reply_text("Erişim izniniz yok.")

# Mesajlara cevap veren ana fonksiyon
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in admin_users:
        return await update.message.reply_text("Bu botu kullanma izniniz yok.")

    message = update.message.text.lower()

    if "btc" in message:
        await update.message.reply_text("BTC şu an DOMDOM veritabanında 95.000 USD civarında.")
    elif "nasılsın" in message:
        await update.message.reply_text("İyiyim kardeşim, her şey kontrol altında.")
    else:
        await update.message.reply_text("Şimdilik bu konuda bir cevabım yok ama öğrenebilirim.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(config["telegram_api_key"]).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("[telegram_bot] Telegram botu aktif.")
    app.run_polling()
