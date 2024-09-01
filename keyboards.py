from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


def start_menu_keyboard():
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Секретний 🎁 друг 1", callback_data="friend_one")],
            [InlineKeyboardButton("Секретний 🎁 друг 2", callback_data="friend_two")],
            [InlineKeyboardButton("Секретний 🎁 друг 3", callback_data="friend_tree")],
            [InlineKeyboardButton("Секретний 🎁 друг 4", callback_data="friend_four")]
        ]
    )
    return keyboard


def hello_menu_keyboard():
    reply_markup = ReplyKeyboardMarkup(
        [
            ["Привіт👋"]
        ],
        one_time_keyboard=True,
        resize_keyboard=True,
    )
    return reply_markup


def friend_menu_keyboard():
    reply_markup = ReplyKeyboardMarkup(
        [
            ["Співати🎵"],
            ["Танцювати 💃"],
            ["Покормити 🥣"],
            ["Відпочивати 😴"],
            ["Обрати іншого друга 🌈"]
        ],
        one_time_keyboard=True,
        resize_keyboard=True,
    )
    return reply_markup


def eating_menu_keyboard():
    reply_markup = ReplyKeyboardMarkup(
        [
            ["Яблучко 🍎"],
            ["Піца 🍕"],
            ["Морозиво 🍦"],
            ["Банан 🍌"],
            ["Зірка в космосі ⭐"],
            ["Я не хочу істи 🙊"]
        ],
        one_time_keyboard=True,
        resize_keyboard=True,
    )
    return reply_markup
