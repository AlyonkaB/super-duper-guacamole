from telegram import Update

from keyboards import friend_menu_keyboard


async def friend_selection_handler(update: Update, context) -> None:
    query = update.callback_query
    if query.data == "friend_one":
        await query.message.reply_text(
            text=f"Мене звати Єдинорожка🦄:"
        )
        await query.message.reply_photo(
            photo=open("media/Friend_1.png", "rb")
        )

    if query.data == "friend_two":
        await query.message.reply_text(
            text=f"Мене звати Кицюня😸:"
        )
        await query.message.reply_photo(
            photo=open("media/Friend_2.png", "rb")
        )

    if query.data == "friend_tree":
        await query.message.reply_text(
            text=f"Мене звати Вухастик🐰:"
        )
        await query.message.reply_photo(
            photo=open("media/Friend_3.png", "rb")
        )

    if query.data == "friend_four":
        await query.message.reply_text(
            text=f"Мене звати Кроко🐊:"
        )
        await query.message.reply_photo(
            photo=open("media/Friend_4.png", "rb")
        )
    await query.message.reply_text(
        text=f"Що будемо робити разом?",
        reply_markup=friend_menu_keyboard()
    )
