import pprint
import time
from selenium import webdriver
# ввод данных с клавиатуры
from selenium.webdriver import Keys
# Поиск различных элементов
from selenium.webdriver.common.by import By

# browser = webdriver.Firefox()
# browser.get(
#     "https://ru.wikipedia.org/w/index.php?fulltext=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&search=world&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1")

browser = webdriver.Firefox()
browser.get(
    "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")


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


def going_through_the_paragraphs_of_the_article():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    # Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


going_through_the_paragraphs_of_the_article()
