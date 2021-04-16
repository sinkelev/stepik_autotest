from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_find_button_add(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_add = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
    )
    assert button_add.is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
