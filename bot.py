import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN", "")
MANAGER = "https://t.me/OlenaMatviienko"

TEXTS = {
    "program": (
        "🌊 *Дитячий табір Kids UA в Кемері (Туреччина) від простору «БЕРЕГИНЯ»* ☀️\n\n"
        "Сонце, море та незабутній відпочинок на березі Середземного моря! Кожен наш день — це поєднання драйву, корисного відпочинку та безпеки під наглядом дбайливих вожатих.\n\n"
        "📋 *Що чекає на дітей протягом дня:*\n\n"
        "🤸‍♂️ *Бадьорий ранок* — прокидаємося, робимо легку розминку або йдемо на ранковий заплив у басейні, щоб зарядитися енергією на весь день.\n"
        "🥞 *Смачний сніданок* — смачний, поживний та збалансований буфет — сили нам точно знадобляться.\n"
        "🏖️ *Море та сонце* — командні ігри на узбережжі, пляжний волейбол, купання та пляжні квести під наглядом вожатих.\n"
        "🍉 *Релакс сієста* — найтепліші години проводимо в затінку: настільні ігри, творчі майстер-класи, перегляд фільмів або просто відпочинок у номерах без гаджетів.\n"
        "🎲 *Настільні ігри* — гуртують команду, розвивають логіку, вчать домовлятися та допомагають знайти нових друзів.\n"
        "🏆 *Драйв та активності* — спортивні змагання, тренінги з лідерства, підготовка до вечірніх шоу або квести по території.\n"
        "✨ *Вечірнє шоу та магія* — тематичні вечірки, конкурси, запальні дискотеки, затишні посиденьки під турецьким небом або вечори щирих розмов.\n"
        "💤 *Втомлені і щасливі* — повні емоцій лягаємо спати, щоб завтра почати нову пригоду."
    ),
    "prices": "💰 *Ціни*\n\nЦіни на літо 2026 скоро будуть опубліковані.\nСлідкуйте за оновленнями!",
    "dates": "📅 *Дати змін*\n\nПерша зміна стартує з 27.06.2026.\nДеталі скоро з'являться тут!",
    "register": "✅ *Як записатись*\n\nДля бронювання місця в таборі, будь ласка, заповніть коротку анкету учасника:\n👉 [Заповнити анкету](https://docs.google.com/forms/d/e/1FAIpQLSfR59nWsWuwNOXmKkLu3ydAX0t9prRESoEmFg8TP32STn6xLg/viewform?usp=header)",
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
