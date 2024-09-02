from telegram import Update

from keyboards import eating_menu_keyboard, friend_menu_keyboard


async def eat(update: Update, context) -> None:
    name_user = update.message.from_user.username

    await update.message.reply_photo(
        photo=open("media/eating.png", "rb")
    )
    await update.message.reply_text(
        text=f"{name_user} що Ми будемо їсти 🍲?",
        reply_markup=eating_menu_keyboard()
    )


async def apple(update: Update, context) -> None:
    await update.message.reply_photo(
        photo=open("media/apple.png", "rb")
    )
    await update.message.reply_text(
        text=f"Яблуко 🍎 дуже корисний перекус 👍"
             f"\nАле ним не наїсишся 😒"
             f"\nОбери ще щось 🤨⬇️",
        reply_markup=eating_menu_keyboard()
    )


async def pizza(update: Update, context) -> None:
    await update.message.reply_photo(
        photo=open("media/pizza.png", "rb")
    )
    await update.message.reply_text(
        text=f"Якщо з'їсти багато піци 🍕 - буде боліти живіт 🤢"
             f"\nОбери щось інше 🤨⬇️",
        reply_markup=eating_menu_keyboard()
    )


async def ice_cream(update: Update, context) -> None:
    await update.message.reply_photo(
        photo=open("media/ice_cream.png", "rb")
    )
    await update.message.reply_text(
        text=f"Якщо постійно їсти морозиво 🍦 -  будуть боліти зубки 🦷😨"
             f"\nОбери щось інше 🤨⬇️",
        reply_markup=eating_menu_keyboard()
    )


async def banana(update: Update, context) -> None:
    await update.message.reply_photo(
        photo=open("media/banana.png", "rb")
    )
    await update.message.reply_text(
        text=f"Банан 🍌 смачний і поживний 🔥!!! "
             f"\nЯ наївся 😄!!!"
             f"\nДякую 🥰!!!",
        reply_markup=friend_menu_keyboard()
    )


async def star(update: Update, context) -> None:
    await update.message.reply_photo(
        photo=open("media/Star in sky.png", "rb")
    )
    await update.message.reply_text(
        text=f"Це жарт 🤣🤣🤣!"
             f"\nЗірки ⭐ не можливо з'їсти, вони далеко у космосі 🌌."
             f"\nОбери щось інше 🤨⬇️",
        reply_markup=eating_menu_keyboard()
    )


async def not_eat(update: Update, context) -> None:
    name_user = update.message.from_user.username

    await update.message.reply_text(
        text=f"Добре, {name_user} у що будемо грати далі 😄?",
        reply_markup=friend_menu_keyboard()
    )
