from telegram import Update

from keyboards import friend_menu_keyboard


async def dance(update: Update, context) -> None:
    name_user = update.message.from_user.username

    await update.message.reply_text(
        f"{name_user}, ТАНЦЮЙ разом зі мною!!!"
    )
    await update.message.reply_text(
        "https://www.youtube.com/watch?v=ld__dVatHiE"
    )
    await update.message.reply_text(
        text=f"Вибери що Ми будемо робити після танців!",
        reply_markup=friend_menu_keyboard()
    )
