import pprint

from selenium import webdriver

# ввод данных с клавиатуры
from selenium.webdriver import Keys

# Поиск различных элементов
from selenium.webdriver.common.by import By

import time

browser = webdriver.Firefox()
browser.get(
    "https://ru.wikipedia.org/w/index.php?fulltext=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&search=world&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1")

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

count = 1
for i in hatnotes:
    print(f"Статья № {count} - {i}")
    count += 1

user_input = int(input("Ввыберите номер интересующей вас стать"))


value = list(hatnotes.values())[user_input - 1]
print(value)
browser.get(value)
