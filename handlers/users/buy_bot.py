from typing import Union

from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards.inline.menu_keyboards import main_level_keyboard, menu_cb, category_level, additional_item_level
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await list_main(message)


async def list_main(message: Union[CallbackQuery, Message], **kwargs):
    # Клавиатуру формируем с помощью следующей функции (где делается запрос в базу данных)
    markup = await main_level_keyboard()
    # Проверяем, что за тип апдейта. Если Message - отправляем новое сообщение
    if isinstance(message, Message):
        await message.answer("В данном меню можно", reply_markup=markup)

    # Если CallbackQuery - изменяем это сообщение
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_categories(callback: CallbackQuery, sign, **kwargs):
    markup = await category_level(sign)
    # Изменяем сообщение, и отправляем новые кнопки с категориями
    await callback.message.edit_reply_markup(markup)


async def list_subcategories(callback: CallbackQuery, sign, category, **kwargs):
    markup = await additional_item_level(sign, category)
    if category == 'tz':
        await callback.message.answer('Напишите ваше Техническое задание')
    else:
        # Изменяем сообщение, и отправляем новые кнопки с категориями
        await callback.message.edit_reply_markup(markup)


@dp.callback_query_handler(menu_cb.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """

    # Получаем текущий уровень меню, который запросил пользователь
    current_level = callback_data.get("level")

    # Получаем категорию, которую выбрал пользователь (Передается всегда)
    category = callback_data.get("category")

    # Получаем подкатегорию, которую выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    sign = callback_data.get("sign")

    # Прописываем "уровни" в которых будут отправляться новые кнопки пользователю
    levels = {
        "0": list_main,  # Отдаем главную
        "1": list_categories,  # Отдаем категории
        "2": list_subcategories,
    }

    # Забираем нужную функцию для выбранного уровня
    current_level_function = levels[current_level]

    # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
    await current_level_function(
        call,
        category=category,
        sign=sign,
    )
