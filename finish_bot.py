from telegram import Update

from keyboards import hello_menu_keyboard


async def sleep(update: Update, context) -> None:
    name_user = update.message.from_user.username
    await update.message.reply_photo(
        photo=open("media/Sleep.png", "rb")
    )
    await update.message.reply_text(
        text=f"{name_user}, приходь пізніше ще пограємо 😁"
             f"\nА зараз  Ми ідемо відпочивати 😴"
             f"\nДо зустрічі 👋",
        reply_markup=hello_menu_keyboard()
    )