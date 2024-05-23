import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Настройки браузера и открытие страницы
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


def numbering_and_dictionary_search(articles):
    """
    Нумеруем наш словарь
    :param articles:
    """
    for count, title in enumerate(articles, start=1):
        print(f"Статья № {count} - {title}")


# Получаем словарь со статьями
numbering_and_dictionary_search(list_articles)

user_input = int(input("Выберите номер интересующей вас статьи - "))


def link_user_input(articles, user_input):
    """Переходим по ссылке которую выбирает пользователь"""
    value = list(articles.values())[user_input - 1]
    return browser.get(value)


paragraph_article = link_user_input(list_articles, user_input)
time.sleep(5)  # Небольшая пауза для загрузки статьи


def linked_page():
    hatnotes = []

    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if "hatnote" in cl:
            links = element.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                hatnotes.append(href)

    if hatnotes:
        chosen_link = random.choice(hatnotes)
        browser.get(chosen_link)
    else:
        print("Связанные страницы не найдены.")


def going_through_the_paragraphs_of_the_article():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    for paragraph in paragraphs:
        print(paragraph.text)
        input("Нажмите Enter для перехода к следующему параграфу.")


def close_program():
    print("Выход из программы")
    browser.quit()
    exit()


def choosing_actions():
    options = [
        "листать параграфы текущей статьи",
        "перейти на одну из связанных страниц",
        "Выход из программы"
    ]

    while True:
        print("\nВыберите опцию:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Введите номер опции: ")

        if choice == '1':
            going_through_the_paragraphs_of_the_article()
        elif choice == '2':
            linked_page()
        elif choice == '3':
            close_program()
        else:
            print("Неправильный выбор. Попробуйте снова.")


choosing_actions()