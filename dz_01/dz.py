import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from func import (
    initialize_browser,
    requesting_articles_from_the_user,
    numbering_and_dictionary_search,
    link_user_input,
    choosing_actions
)
###############################################################################
# Инициализация браузера и открытие страницы
browser = initialize_browser()
###############################################################################

###############################################################################
# Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

# Ввод запроса от пользователя
user_request = input("Введите ваш запрос - ")

# Прописываем ввод текста в поисковую строку
search_box.send_keys(user_request)

# Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)  # Небольшая пауза для загрузки результатов поиска
###############################################################################

###############################################################################
# Получение статей по запросу пользователя
list_articles = requesting_articles_from_the_user(browser)

# Нумерация и вывод статей
numbering_and_dictionary_search(list_articles)

# Получение выбора пользователя
user_input = int(input("Выберите номер интересующей вас статьи - "))

# Переход по ссылке выбранной пользователем
link_user_input(browser, list_articles, user_input)
time.sleep(5)  # Небольшая пауза для загрузки статьи

# Выбор действия пользователя
choosing_actions(browser)
###############################################################################
