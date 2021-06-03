from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from data.iteams import additional_services

menu_cb = CallbackData("show_menu", "level", "category", "item_id", "sign")
buy_item = CallbackData("buy", "item_id")


def make_callback_data(level, category="0", item_id="0", sign="0"):
    """Формирует коллбэкдату для каждого элемента меню"""
    return menu_cb.new(level=level, category=category, item_id=item_id, sign=sign)


async def main_level_keyboard():
    # Указываем, что текущий уровень меню - 0
    CURRENT_LEVEL = 0

    # Создаем Клавиатуру
    markup = InlineKeyboardMarkup()

    # Сформируем колбек дату, которая будет на кнопке. Следующий уровень - текущий + 1, и перечисляем категории
    callback_data_buy_bot = make_callback_data(level=CURRENT_LEVEL + 1, sign="buy_bot")
    callback_data_developer_info = make_callback_data(level=CURRENT_LEVEL + 1, sign="developer_info")

    # Вставляем кнопку в клавиатуру
    markup.insert(
        InlineKeyboardButton(text="Создать бота", callback_data=callback_data_buy_bot)
    )
    markup.insert(
        InlineKeyboardButton(text="О разработчике", url="https://kwork.ru/user/dmitriybersenev",
                             callback_data=callback_data_developer_info)
    )

    # Возвращаем созданную клавиатуру в хендлер
    return markup


async def category_level(sign):
    # Указываем, что текущий уровень меню - 0
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    # Сформируем колбек дату, которая будет на кнопке. Следующий уровень - текущий + 1, и перечисляем категории
    callback_data_tz = make_callback_data(level=CURRENT_LEVEL + 1, category='tz', sign=sign)
    callback_data_add_services = make_callback_data(level=CURRENT_LEVEL + 1, category='add_services', sign=sign)

    buy_bot_button = "Написать ТЗ"
    developer_info_button = "Дополнительные услуги"

    # Вставляем кнопку в клавиатуру
    markup.insert(
        InlineKeyboardButton(text=buy_bot_button, callback_data=callback_data_tz)
    )
    markup.insert(
        InlineKeyboardButton(text=developer_info_button, callback_data=callback_data_add_services)
    )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1))
    )

    # Возвращаем созданную клавиатуру в хендлер
    return markup


async def additional_item_level(sign, category):
    # Указываем, что текущий уровень меню - 0
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=2)

    # Сформируем колбек дату, которая будет на кнопке. Следующий уровень - текущий + 1, и перечисляем категории
    for subcategory in additional_services:
        callback_data = make_callback_data(level=CURRENT_LEVEL, category=category, sign=sign,
                                           item_id=subcategory.name)

        button_text = f"{subcategory.name} - {subcategory.amount} Руб."

        # Вставляем кнопку в клавиатуру
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1))
    )

    # Возвращаем созданную клавиатуру в хендлер
    return markup
