from time import sleep
from tkinter import Image
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

def test_input_text(driver):
    driver.get("http://uitestingplayground.com/textinput")
    text_input = "ITCH"

    element_input = driver.find_element(By.CLASS_NAME, "form-control")
    element_input.send_keys(text_input)
    # sleep(2)

    blue_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
    blue_button.click()
    # sleep(2)

    text_button = blue_button.text

    assert text_input == text_button


def test_img(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "lead"),
        "Done!")
    )

    # images = driver.find_elements(By.TAG_NAME, "img")

    image_container = driver.find_element(By.ID, "image-container")
    images = image_container.find_elements(By.TAG_NAME, "img")

    image_3_alt = images[2].get_attribute("alt")

    assert image_3_alt == "award"



    #
    #
    # img = Image.open("test.jpg")
    # img.show()
    #
    # image_container = driver.find_element(By.ID, "image-container")
    # images = image_container.find_elements(By.TAG_NAME, "img")
    # image_3 = images[2]
    #
    # alt_value = image_3.get_attribute("alt")