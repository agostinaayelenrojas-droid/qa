import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCoffeeCart:

    # TEST 1: Agregar un café y validar carrito y precio
    def test_agregar_espresso(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('https://coffee-cart.app/')

        driver.find_element(By.CSS_SELECTOR, '[data-test="Espresso"]').click()

        carrito = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Cart page"]')
        assert carrito.text == 'cart (1)'

        total = driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]')
        assert total.text == 'Total: $10.00'

        driver.quit()

    # TEST 2: Intentar pagar dejando los campos vacíos
    def test_pago_vacio(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('https://coffee-cart.app/')

        driver.find_element(By.CSS_SELECTOR, '[data-test="Espresso"]').click()
        driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]').click()

        driver.find_element(By.ID, 'submit-payment').click()

        titulo = driver.find_element(By.TAG_NAME, 'h1')
        assert titulo.text == 'Payment details'

        driver.quit()

    # TEST 3: Completar los datos y hacer la compra exitosa
    def test_compra_exitosa(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('https://coffee-cart.app/')

        driver.find_element(By.CSS_SELECTOR, '[data-test="Espresso"]').click()
        driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]').click()

        driver.find_element(By.ID, 'name').send_keys('Agostina')
        driver.find_element(By.ID, 'email').send_keys('agostina@mail.com')
        driver.find_element(By.ID, 'promotion').click()
        driver.find_element(By.ID, 'submit-payment').click()

        carrito = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Cart page"]')
        assert carrito.text == 'cart (0)'

        driver.quit()

#python -m pytest -v tps/test_coffee_cart.py