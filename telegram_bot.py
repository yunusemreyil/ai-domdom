from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import json
import openai

# config.json'dan ayarları yükle
with open("config.json", "r") as f:
    config = json.load(f)

admin_users = config.get("admin_users", [])
openai.api_key = config.get("openai_api_key")

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in admin_users:
        await update.message.reply_text("Merhaba, ben DOMDOM AI. Her sorunu cevaplamak için hazırım.")
    else:
        await update.message.reply_text("Erişim izniniz yok.")

# GPT destekli mesaj işleyici
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in admin_users:
        return await update.message.reply_text("Bu botu kullanma izniniz yok.")

    user_message = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen DOMDOM adında bir Telegram sohbet yapay zekasısın."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text(f"Hata oluştu: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(config["telegram_api_key"]).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("[telegram_bot] GPT destekli Telegram botu aktif.")
    app.run_polling()
