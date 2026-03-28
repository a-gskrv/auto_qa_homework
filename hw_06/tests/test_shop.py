from time import sleep

import pytest
from selenium import webdriver

from homework.hw_06.pages.login_page import LoginPage
from homework.hw_06.pages.cart_page import CartPage
from homework.hw_06.pages.inventory_page import InventoryPage
from homework.hw_06.pages.checkout_page import CheckoutPage


class TestShop():
    @pytest.fixture(scope='class')  ## вызов один раз на уровне класса
    def driver(self):
        #### победил вместе с ИИ всплывающее окно Chrome о пароле
        options = webdriver.ChromeOptions()
        # отключаем менеджер паролей
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        # отключаем проверку утечек паролей (ВАЖНО)
        options.add_argument("--disable-features=PasswordLeakDetection")
        options.add_argument("--disable-features=PasswordLeakDetection,PasswordCheck")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)

        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture(autouse=True)  ## вызов перед каждым тестом
    def setup_login_page(self, driver):
        self.login_page = LoginPage(driver)

    @pytest.fixture(autouse=True)  ## вызов перед каждым тестом
    def setup_cart_page(self, driver):
        self.cart_page = CartPage(driver)

    @pytest.fixture(autouse=True)  ## вызов перед каждым тестом
    def setup_inventory_page(self, driver):
        self.inventory_page = InventoryPage(driver)

    @pytest.fixture(autouse=True)  ## вызов перед каждым тестом
    def setup_checkout_page(self, driver):
        self.checkout_page = CheckoutPage(driver)

    def test_shop(self):
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")

        """
        Добавьте в корзину товары:
Sauce Labs Backpack
Sauce Labs Bolt T-Shirt
Sauce Labs Onesie
        """

        inventory_page = self.inventory_page
        inventory_page.add_item_by_name_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_by_name_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_by_name_to_cart("Sauce Labs Onesie")

        element_cart_item = inventory_page.get_cart()
        element_cart_item.click()

        self.cart_page.click_checkout()

        self.checkout_page.enter_first_name("Albert")
        self.checkout_page.enter_last_name("Gaskarov")
        self.checkout_page.enter_postal_code("09599")

        self.checkout_page.click_button_continue()

        label_total = self.checkout_page.get_label_total()
        total_sum = label_total.text.replace("Total: $", "")

        # sleep(2)

        assert float(total_sum) == 58.29, f"ERROR. Итоговая сумма = {total_sum}"
