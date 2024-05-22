from selenium import webdriver
import time

browser = webdriver.Firefox()

# В кавычках указываем URL сайта, на который нам нужно зайти
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("dom.png")

# Задержка
time.sleep(5)

browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")

# Задержка
time.sleep(3)

# Перезагрузка страницы
browser.refresh()

# # Закрываем браузер
# browser.quit()
