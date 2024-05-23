import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Открываем браузер и переходим на главную страницу Википедии
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
time.sleep(2)  # Небольшая пауза для загрузки результатов поиска


def requesting_articles_from_the_user():
    """
    Создает словарь из списка статей, по запросу пользователя
    Где ключ - Title, значение ссылка на статью
    :return: hatnotes
    """
    hatnotes = {}

    search_results = browser.find_elements(By.CLASS_NAME, "mw-search-result")
    for result in search_results:
        heading = result.find_element(By.CLASS_NAME, "mw-search-result-heading")
        link = heading.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = heading.text
        hatnotes[title] = link

    return hatnotes


list_articles = requesting_articles_from_the_user()


def numbering_and_dictionary_search(articles_dict):
    """
    Номеруем наш словарь
    :param articles_dict: словарь со статьями
    :return:
    """
    count = 1
    for title in articles_dict:
        print(f"Статья № {count} - {title}")
        count += 1


# Получаем словарь со статьями
numbering_and_dictionary_search(list_articles)