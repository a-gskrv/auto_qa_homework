from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_input_first_name(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    def get_input_last_name(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "last-name")))

    def get_input_postal_code(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "postal-code")))

    def get_button_continue(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "continue")))

    def enter_first_name(self, first_name):
        input_first_name = self.get_input_first_name()
        input_first_name.clear()
        input_first_name.send_keys(first_name)

    def enter_last_name(self, first_name):
        input_first_name = self.get_input_last_name()
        input_first_name.clear()
        input_first_name.send_keys(first_name)

    def enter_postal_code(self, first_name):
        input_first_name = self.get_input_postal_code()
        input_first_name.clear()
        input_first_name.send_keys(first_name)

    def click_button_continue(self):
        self.get_button_continue().click()

    def get_label_total(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
