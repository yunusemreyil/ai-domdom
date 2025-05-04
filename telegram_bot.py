from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

# config.json dosyasını oku
with open("config.json", "r") as f:
    config = json.load(f)

admin_users = config.get("admin_users", [])

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in admin_users:
        await update.message.reply_text("Merhaba, ben DOMDOM. Telegram bağlantısı başarılı.")
    else:
        await update.message.reply_text("Erişim izniniz yok.")

# Telegram botunu başlat
if __name__ == '__main__':
    app = ApplicationBuilder().token(config["telegram_api_key"]).build()
    app.add_handler(CommandHandler("start", start))
    print("[telegram_bot] Telegram botu aktif.")
    app.run_polling()
