from telegram import Update

from keyboards import eating_menu_keyboard


async def eat(update: Update, context) -> None:
    name_user = update.message.from_user.username

    await update.message.reply_photo(
        photo=open("media/eating.png", "rb")
    )
    await update.message.reply_text(
        text=f"{name_user} що Ми будемо їсти?",
        reply_markup=eating_menu_keyboard()
    )

