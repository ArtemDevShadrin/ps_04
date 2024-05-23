import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def initialize_browser():
    browser = webdriver.Firefox()
    browser.get(
        "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    assert "Википедия" in browser.title
    time.sleep(1)
    return browser


def requesting_articles_from_the_user(browser):
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


def numbering_and_dictionary_search(articles):
    for count, title in enumerate(articles, start=1):
        print(f"Статья № {count} - {title}")


def link_user_input(browser, articles, user_input):
    value = list(articles.values())[user_input - 1]
    return browser.get(value)


def linked_page(browser):
    hatnotes = []

    # Ищем ссылки в блоках с классами "hatnote", "mw-parser-output", и "div-col"
    for cls in ["hatnote", "mw-parser-output", "div-col"]:
        for element in browser.find_elements(By.CLASS_NAME, cls):
            links = element.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                if href and href.startswith("https://"):
                    hatnotes.append(href)

    if hatnotes:
        chosen_link = random.choice(hatnotes)
        print(f"Переход по ссылке: {chosen_link}")
        browser.get(chosen_link)
    else:
        print("Связанные страницы не найдены.")


def going_through_the_paragraphs_of_the_article(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input("Нажмите Enter для перехода к следующему параграфу.")


def close_program(browser):
    print("Выход из программы")
    browser.quit()
    exit()


def choosing_actions(browser):
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
            going_through_the_paragraphs_of_the_article(browser)
        elif choice == '2':
            linked_page(browser)
        elif choice == '3':
            close_program(browser)
        else:
            print("Неправильный выбор. Попробуйте снова.")
