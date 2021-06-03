from typing import List, Coroutine

from asgiref.sync import sync_to_async
from django_project.telegrambot.usersmanage.models import Item, User


@sync_to_async
def add_user(user_id, full_name, username):
    try:
        return User(user_id=int(user_id), name=full_name, username=username).save()
    except Exception:
        return select_user(int(user_id))


@sync_to_async
def select_all_users():
    users = User.objects.all()
    return users


@sync_to_async
def select_user(user_id: int):
    user = User.objects.filter(user_id=user_id).first()
    return user


@sync_to_async
def count_users():
    total = User.objects.all().count()
    return total


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
@sync_to_async
def add_item(**kwargs):
    new_item = Item(**kwargs).save()
    return new_item


# Функция для вывода товаров с РАЗНЫМИ категориями
@sync_to_async
def get_categories() -> List[Item]:
    items = Item.objects.distinct("category_name").all()
    return items


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
@sync_to_async
def get_subcategories(category) -> List[Item]:
    return Item.objects.distinct("subcategory_name").filter(category_code=category).all()


# Функция для подсчета товаров с выбранными категориями и подкатегориями
@sync_to_async
def count_items(category_code, subcategory_code=None) -> int:
    # Прописываем условия для вывода (категория товара равняется выбранной категории)
    conditions = dict(category_code=category_code)

    # Если передали подкатегорию, то добавляем ее в условие
    if subcategory_code:
        conditions.update(subcategory_code=subcategory_code)
    return Item.objects.filter(**conditions).count()


# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
@sync_to_async
def get_items(category_code, subcategory_code) -> List[Item]:
    item = Item.objects.filter(
        category_code=category_code, subcategory_code=subcategory_code).all()
    return item


# Функция для получения объекта товара по его айди
@sync_to_async
def get_item(item_id) -> Item:
    item = Item.objects.filter(id=int(item_id)).first()
    return item
