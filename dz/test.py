import pprint

from selenium import webdriver

# ввод данных с клавиатуры
from selenium.webdriver import Keys

# Поиск различных элементов
from selenium.webdriver.common.by import By

import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/w/index.php?fulltext=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&search=world&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1")

# for elements in browser.find_elements(By.TAG_NAME, "li"):
#     # Чтобы искать атрибут класса
#     cl = elements.get_attribute("class")
#     if cl == "mw-search-result mw-search-result-ns-0 searchresult-with-quickview":
#         for element in elements.find_elements(By.TAG_NAME, "div"):
#             cl = elements.get_attribute("class")
#             if cl == "searchResultImage-text":
#                 pprint.pprint(element)
        # pprint.pprint(element.text)
element = browser.find_element(By.TAG_NAME, "li")
cl = element.get_attribute("class")
if cl == "mw-search-result mw-search-result-ns-0 searchresult-with-quickview":
    pprint.pprint(element.text)

# pprint.pprint(browser.find_element(By.TAG_NAME, "li").get_attribute("mw-search-result mw-search-result-ns-0 searchresult-with-quickview"))

