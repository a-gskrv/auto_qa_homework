from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

    def get_cart(self):
        return self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "a.shopping_cart_link"
            ))
        )

    def add_item_by_name_to_cart(self, item_name):

        items = self.get_items()

        for item in items:
            i_name = item.find_element(By.CLASS_NAME, "inventory_item_name ").text
            if item_name == i_name:
                button_add = item.find_element(By.CLASS_NAME, "btn_inventory ")
                button_add.click()
                break
