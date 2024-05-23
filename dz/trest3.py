import pprint
import time
from selenium import webdriver
# ввод данных с клавиатуры
from selenium.webdriver import Keys
# Поиск различных элементов
from selenium.webdriver.common.by import By


# browser = webdriver.Firefox()
# browser.get(
#     "https://ru.wikipedia.org/wiki/World_Class")


# Предлагать пользователю три варианта действий:
#
#     листать параграфы текущей статьи;
#     перейти на одну из связанных страниц — и снова выбор из двух пунктов:
#
# - листать параграфы статьи;
#
# - перейти на одну из внутренних статей.
#
#     выйти из программы.


def aa():
    return "Привет"


def bb():
    return "Не Привет"


def cc():
    return "Пока"


# def сhoosing_actions(a, b, c):
#     variant = {
#         a(): "листать параграфы текущей статьи;",
#         b(): "перейти на одну из связанных страниц;",
#         c(): "Выход из программы"
#     }
#     count = 1
#     for i in variant:
#         print(f"действия № {count} - {variant[i]}")
#         count += 1
#
#     user_input = int(input("Выберите номер интересующего вас действия - "))
#
#     print(list(variant.keys())[user_input - 1])


# сhoosing_actions(aa, bb, cc)

def сhoosing_actions(aa, bb, cc):
    list = ["листать параграфы текущей статьи;", "перейти на одну из связанных страниц;", "Выход из программы"]
    for i, item in enumerate(list):
        print(i + 1, item)

    user_unput = int(input("Выберите номер интересующего вас действия - "))

    if user_unput == 1:
        return aa

    elif user_unput == 2:
        return bb

    else:
        return cc


print(сhoosing_actions(aa, bb, cc))
