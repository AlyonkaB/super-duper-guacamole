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


from keyboards import (
    start_menu_keyboard,
    hello_menu_keyboard
)

from select_friend_bot import friend_selection_handler
from song_bot import song
from dance_bot import dance
from eat_bot import eat


load_dotenv()
ADMIN_BOT_TOKEN = os.getenv("ADMIN_BOT_TOKEN")


async def start(update: Update, context):
    await update.message.reply_text(
        text=f"Ну що почнемо?"
             f"\n Я Твій Tamagotchi-bot і сьогодні Ми будемо с тобою гратися!"
             f"\n Давай привіта́ємось один з одним!",
        reply_markup=hello_menu_keyboard()
    )
    await update.message.reply_photo(
        photo=open("media/Tamagochi_bot.png", "rb")
    )


async def hello(update: Update, context) -> None:
    name_user = update.message.from_user.username

    await update.message.reply_photo(
        photo=open("media/Friend and I.png", "rb")
    )
    await update.message.reply_text(
        f"Привіт {name_user}, Вибери собі друга з яким Ти будеш дружити!",
        reply_markup=start_menu_keyboard()
    )


def main():
    app = ApplicationBuilder().token(ADMIN_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text(strings=("Привіт👋",)), hello))
    app.add_handler(CallbackQueryHandler(friend_selection_handler))
    app.add_handler(MessageHandler(filters.Text(strings=("Обрати іншого друга 🌈",)), hello))
    app.add_handler(MessageHandler(filters.Text(strings=("Співати🎵",)), song))
    app.add_handler(MessageHandler(filters.Text(strings=("Танцювати 💃",)), dance))
    app.add_handler(MessageHandler(filters.Text(strings=("Покормити 🥣",)), eat))

    app.run_polling()


if __name__ == '__main__':
    main()
