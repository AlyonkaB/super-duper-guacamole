from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

import os
from dotenv import load_dotenv

from finish_bot import sleep
from keyboards import (
    start_menu_keyboard,
    hello_menu_keyboard
)

from select_friend_bot import friend_selection_handler
from song_bot import song
from dance_bot import dance
from eat_bot import eat, apple, pizza, ice_cream, banana, star, not_eat

load_dotenv()
ADMIN_BOT_TOKEN = os.getenv("ADMIN_BOT_TOKEN")


async def start(update: Update, context):
    await update.message.reply_text(
        text=f"Ну що почнемо?"
             f"\n Я Твій Tamagotchi-bot і сьогодні Ми будемо с тобою гратися!"
             f"\n Давай привіта́ємось один з одним!",
        reply_markup=hello_menu_keyboard()
    )
    with open("media/Tamagochi_bot.png", "rb") as photo:
        await update.message.reply_photo(
            photo=photo
        )


async def hello(update: Update, context) -> None:
    name_user = update.message.from_user.username
    with open("media/Friend and I.png", "rb") as photo:
        await update.message.reply_photo(
            photo=photo
        )

    await update.message.reply_text(
        f"Привіт {name_user}, Вибери собі друга з яким Ти будеш дружити!",
        reply_markup=start_menu_keyboard()
    )


async def dont_understand(update: Update, context):
    with open("media/dnt_understand.png", "rb") as photo:
        await update.message.reply_photo(
            photo=photo
        )
    await update.message.reply_text(
        text=f"😔 НЕ РОЗУМІЮ ТЕБЕ 😔"
             f"\n⬇️ Зроби свій вибір в меню ⬇️!")


def main():
    app = ApplicationBuilder().token(ADMIN_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text(strings=("Привіт👋",)), hello))
    app.add_handler(CallbackQueryHandler(friend_selection_handler))
    app.add_handler(MessageHandler(filters.Text(strings=("Обрати іншого друга 🌈",)), hello))
    app.add_handler(MessageHandler(filters.Text(strings=("Співати🎵",)), song))
    app.add_handler(MessageHandler(filters.Text(strings=("Танцювати 💃",)), dance))
    app.add_handler(MessageHandler(filters.Text(strings=("Покормити 🥣",)), eat))
    app.add_handler(MessageHandler(filters.Text(strings=("Яблучко 🍎",)), apple))
    app.add_handler(MessageHandler(filters.Text(strings=("Піца 🍕",)), pizza))
    app.add_handler(MessageHandler(filters.Text(strings=("Морозиво 🍦",)), ice_cream))
    app.add_handler(MessageHandler(filters.Text(strings=("Банан 🍌",)), banana))
    app.add_handler(MessageHandler(filters.Text(strings=("Зірка в космосі ⭐",)), star))
    app.add_handler(MessageHandler(filters.Text(strings=("Я не хочу істи 🙊",)), not_eat))
    app.add_handler(MessageHandler(filters.Text(strings=("Відпочивати 😴",)), sleep))
    app.add_handler(MessageHandler(filters.Text(), dont_understand))
    app.run_polling()


if __name__ == '__main__':
    main()
