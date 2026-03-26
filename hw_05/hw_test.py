from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver
    driver.quit()

def test_text_in_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)

    text_find = "semper posuere integer et senectus justo curabitur."

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))

    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), text_find))

    text_body = driver.find_element(By.TAG_NAME, "body").text

    assert text_find in text_body




def test_drag_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    driver.add_cookie({"name": "FCCDCF",
                        "value": "%5Bnull%2Cnull%2Cnull%2C%5B%22CQgpPoAQgpPoAEsACBRUCVFoAP_gAEPgABBoK1IB_C7EbCFCiDJ3IKMEMAhHABBAYsAwAAYBAwAADBIQIAQCgkEYBASAFCACCAAAKASBAAAgCAAAAUAAIAAFAABAAAwAIBAIIAAAgAAAAEAIAAAACIAAEQCAAAAEAEAAkAgAAAIASAAAAAAAAACBAAAAAAAAAAAAAAAABAEAAQAAQAAAAAAAiAAAAAAAABAIAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQWEQD-F2I2EKFEGCuQUYIYBCuACAAxYBgAAwCBgAAGCQgQAgFJIIkCAEAIEAAEAAAQAgCAABQEBAAAIAAAAAqAACAABgAQCAQAIABAAAAgIAAAAAAEQAAIgEAAAAIAIABABAAAAQAkAAAAAAAAAECAAAAAAAAAAAAAAAAAAIAAEABgAAAAAABEAAAAAAAACAQIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAA.ILCIB_C7EbCFCiDJ3IKMEMAhXABBAYsAwAAYBAwAADBIQIAQCkkEaBASAFCACCAAAKASBAAAoCAgAAUAAIAAVAABAAAwAIBAIIEAAgAAAQEAIAAAACIAAEQCAAAAEAEAAkAgAAAIASAAAAAAAAACBAAAAAAAAAAAAAAAABAEAASAAwAAAAAAAiAAAAAAAABAIEAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQAAAE%22%2C%222~61.89.122.161.184.196.230.314.442.445.494.550.576.827.1029.1033.1046.1047.1051.1097.1126.1166.1301.1342.1415.1725.1765.1942.1958.1987.2068.2072.2074.2107.2213.2219.2223.2224.2328.2331.2387.2416.2501.2567.2568.2575.2657.2686.2778.2869.2878.2908.2920.2963.3005.3023.3126.3234.3235.3253.3309.3731.6931.8931.13731.15731.33931~dv.%22%2C%223D52A15F-3860-4E03-8371-16A1AFFCD02E%22%5D%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22d160fac0-9d89-4127-ab06-a8405fa2da91%5C%22%2C%5B1772784498%2C468000000%5D%5D%22%5D%5D%5D",
                        "domain": ".globalsqa.com",
                        })
    driver.refresh()
    wait = WebDriverWait(driver, 10)

    actions = ActionChains(driver)

    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(iframe)

    all_images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))

    element_drop = all_images[0]
    element_drag = wait.until(EC.presence_of_element_located((By.ID, "trash")))

    actions.drag_and_drop(element_drop, element_drag).perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    # sleep(2)

    all_images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
    drag_images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#trash li")))

    assert len(all_images) == 3
    assert len(drag_images) == 1


    #
    # wait = WebDriverWait(driver, 10)
    #
    # drag_element = driver.find_element(By.CLASS_NAME, "ui-widget-content.ui-corner-tr.ui-draggable.ui-draggable-handle")
    # drop_area = driver.find_element(By.CLASS_NAME, "ui-widget-content.ui-state-default.ui-droppable")
    #
    # actions = ActionChains(driver)
    # actions.drag_and_drop(drag_element, drop_area).perform()
    #
    # sleep(5)
    # dropped_text = driver.find_element(By.CSS_SELECTOR, "#droppable > p")
    #
    # assert drop_area.text == "Dropped!", drop_area.text
