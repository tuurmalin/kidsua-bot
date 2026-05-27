import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN", "")
MANAGER = "https://t.me/OlenaMatviienko"

TEXTS = {
    "program": "📋 *Програма табору*\n\nПрограма табору на літо 2026 скоро буде опублікована.\nСлідкуйте за оновленнями!",
    "prices": "💰 *Ціни*\n\nЦіни на літо 2026 скоро будуть опубліковані.\nСлідкуйте за оновленнями!",
    "dates": "📅 *Дати змін*\n\nПерша зміна стартує з 27.06.2026.\nДеталі скоро з'являться тут!",
    "register": "✅ *Як записатись*\n\nІнформація про реєстрацію скоро буде опублікована.\nСлідкуйте за оновленнями!",
}

def main_menu():
    keyboard = [
        [InlineKeyboardButton("📋 Програма табору", callback_data="program")],
        [InlineKeyboardButton("💰 Ціни", callback_data="prices")],
        [InlineKeyboardButton("📅 Дати змін", callback_data="dates")],
        [InlineKeyboardButton("✅ Як записатись", callback_data="register")],
        [InlineKeyboardButton("💬 Зв'язатись з менеджером", url=MANAGER)],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Вітаємо у Kids UA Camp!\n\nЛітній табір для українських дітей в Анталії ☀️\nДіти 6-15 років | Літо 2026\n\nОберіть що вас цікавить:",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "back":
        await query.edit_message_text(
            "👋 Вітаємо у Kids UA Camp!\n\nЛітній табір для українських дітей в Анталії ☀️\nДіти 6-15 років | Літо 2026\n\nОберіть що вас цікавить:",
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )
    else:
        text = TEXTS.get(query.data, "Інформація скоро буде!")
        keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data="back")]]
        await query.edit_message_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
