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
    
    def get_cart_item(self):
        return self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "a.shopping-cart-link"
            ))
        )












    def get_cart_item_price(self, index):
        return self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    f"[data-test='inventory-item']:nth-child({index}) [data-test='inventory-item-price']",
                    
                )
            )
        ).text





    def get_item_price_button(self, index):
        return self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    f"[data-test='inventory-item']:nth-child({index}) [class='btn btn_primary btn_small btn_inventory ']",
                )
            )
        )

    def get_items_amount(self):
        return len(self.get_items())

    def all_items_are_displayed(self):
        return all(item.is_displayed() for item in self.get_items())

    def get_item_names(self):
        return [
            item.text
            for item in self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "inventory_item_name")
                )
            )
        ]

    def all_items_names_are_displayed(self):
        return all(name.strip() != "" for name in self.get_item_names())

    def all_item_names_are_not_empty(self):
        return all(bool(name.strip()) for name in self.get_item_names())

    def all_item_names_contains_sauce_labs(self):
        return all(name.startswith("Sauce Labs") for name in self.get_item_names())

    def get_one_price(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']"
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, item_xpath))
        ).text

    # def get_items(self):
    #     items = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'data-test="inventory-item"')))
    #     return items
