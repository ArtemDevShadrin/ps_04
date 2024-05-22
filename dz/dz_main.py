import pprint

from selenium import webdriver

# ввод данных с клавиатуры
from selenium.webdriver import Keys

# Поиск различных элементов
from selenium.webdriver.common.by import By

import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(1)

# Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

# Ввод запроса от пользователя
# user_request = input("Введите ваш запрос - ")

# Прописываем ввод текста в поисковую строку.
# search_box.send_keys(user_request)
search_box.send_keys("world")
# Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# def paragraphs_of_the_article():
# paragraphs = browser.find_elements(By.TAG_NAME, "p")
#
# # Для перебора пишем цикл
# for paragraph in paragraphs:
#     print(paragraph.text)
#     input()
# hatnotes = []

# pprint.pprint(browser.find_element(By.TAG_NAME, "li").text)
for element in browser.find_elements(By.TAG_NAME, "li"):
    # Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "searchresult mw-search-result-ns-0 searchresult-with-quickview":
        pprint.pprint(element.text)


# print(hatnotes)
