from time import sleep

from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
    driver.quit()


def is_visible_link_by_text(driver, find_text):
    driver.get("https://itcareerhub.de/ru")
    sleep(0.5)

    all_buttons = driver.find_elements(By.CLASS_NAME, "tn-atom__button-content")
    for btn in all_buttons:
        if btn.text == find_text:
            return btn.is_displayed()

    return False

def test_01_logo(driver):
    driver.get("https://itcareerhub.de/ru")
    # sleep(0.5)

    logo = driver.find_element(By.CLASS_NAME, "tn-atom__img.t-img.loaded")
    assert logo.is_displayed()

def test_02_link_programm(driver):
    find_text = "Программы"
    assert is_visible_link_by_text(driver, find_text)

def test_03_link_payments(driver):
    find_text = "Способы оплаты"
    assert is_visible_link_by_text(driver, find_text)

def test_04_link_news(driver):
    # нет такого на сайте
    find_text = "Новости"
    # assert is_visible_link_by_text(driver, find_text)

def test_05_link_about(driver):
    find_text = "О нас"
    assert is_visible_link_by_text(driver, find_text)

def test_06_link_reviews(driver):
    find_text = "Отзывы"
    assert is_visible_link_by_text(driver, find_text)

def test_07_link_selector_language(driver):
    # find_text = "ru"
    # assert is_visible_link_by_text(driver, find_text)

    driver.get("https://itcareerhub.de/ru")

    selector_ru = driver.find_element(By.CSS_SELECTOR, "[data-elem-id='1710152827519']")
    assert selector_ru.is_displayed()

    selector_de = driver.find_element(By.CSS_SELECTOR, "[data-elem-id='1710152941400']")  # tn-atom
    assert selector_de.is_displayed()
