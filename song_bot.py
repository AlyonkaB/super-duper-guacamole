from telegram import Update

from keyboards import friend_menu_keyboard


async def song(update: Update, context) -> None:
    name_user = update.message.from_user.username

    await update.message.reply_photo(
        photo=open("media/Song.png", "rb")
    )
    await update.message.reply_text(
        f"{name_user}, СПІВАЙ разом зі мною!!!"
    )
    await update.message.reply_audio(
        audio=open("media/Fanny Song.mp3", "rb")
    )
    await update.message.reply_text(
        text=f"Вибери що Ми будемо робити після співів!",
        reply_markup=friend_menu_keyboard()
    )
