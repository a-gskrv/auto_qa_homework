from time import sleep

import pytest
from selenium import webdriver

from homework.hw_06.pages.login_page import LoginPage
from homework.hw_06.pages.cart_page import CartPage
from homework.hw_06.pages.inventory_page import InventoryPage


class TestShop():
    @pytest.fixture(scope='class') ## вызов один раз на уровне класса
    def driver(self):
        driver = webdriver.Chrome()
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







    def test_shop(self):
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")

        """
        Добавьте в корзину товары:
Sauce Labs Backpack
Sauce Labs Bolt T-Shirt
Sauce Labs Onesie
        """




        sleep(2)
