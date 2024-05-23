import pprint
import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get(
    "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(1)

# Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

# Ввод запроса от пользователя
user_request = input("Введите ваш запрос - ")

# Прописываем ввод текста в поисковую строку.
search_box.send_keys(user_request)

# Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)  # Небольшая пауза для загрузки результатов поиска


def requesting_articles_from_the_user():
    """
    Создает словарь из списка статей, по запросу пользователя
    Где ключ - Title, значение ссылка на статью
    :return: hatnotes
    """
    hatnotes = {}

    for elements in browser.find_elements(By.TAG_NAME, "li"):
        # Чтобы искать атрибут класса
        cl = elements.get_attribute("class")
        if cl == "mw-search-result mw-search-result-ns-0 searchresult-with-quickview":
            for element in elements.find_elements(By.TAG_NAME, "div"):
                cl = element.get_attribute("class")
                if cl == "mw-search-result-heading":
                    link = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                    title = element.text
                    hatnotes.setdefault(title, link)
    return hatnotes


list_articles = requesting_articles_from_the_user()


def numbering_and_dictionary_search(dict):
    """
    Номеруем наш словарь
    :param dict:
    :return:
    """
    count = 1
    for i in list_articles:
        print(f"Статья № {count} - {i}")
        count += 1


# Получаем словарь со статьями
numbering_and_dictionary_search(list_articles)

user_input = int(input("Выберите номер интересующей вас статьи - "))


def link_user_input(list_articles, user_input):
    """Переходим по ссылке которую выбирает пользователь"""
    value = list(list_articles.values())[user_input - 1]
    return browser.get(value)


paragraph_article = link_user_input(list_articles, user_input)
time.sleep(5)  # Небольшая пауза для загрузки результатов

# going_through_the_paragraphs_of_the_article()
time.sleep(5)  # Небольшая пауза для загрузки результатов


def linked_page():
    hatnotes = []

    for element in browser.find_elements(By.TAG_NAME, "div"):
        # Чтобы искать атрибут класса
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)

    hatnote = random.choice(hatnotes)

    # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)


def going_through_the_paragraphs_of_the_article():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    # Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


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

сhoosing_actions(going_through_the_paragraphs_of_the_article(), linked_page, None)
