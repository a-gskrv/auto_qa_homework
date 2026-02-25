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


def test_itcareerhub(driver):
    driver.get("https://itcareerhub.de/ru")

    find_payment_method = False
    all_buttons = driver.find_elements(By.CLASS_NAME, "tn-atom__button-content")
    for btn in all_buttons:
        if btn.text == "Способы оплаты":
            btn.click()
            find_payment_method = True
            break

    sleep(2)
    driver.save_screenshot("homework/hw_02/itcareerhub.png")
    sleep(2)

    assert find_payment_method
