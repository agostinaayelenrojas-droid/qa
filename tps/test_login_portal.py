import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPortal:

    def test_login_correcto(self):
        driver = webdriver.Chrome()
        driver.get('https://automationtesting.co.uk/loginPortal.html')

        driver.find_element(By.ID, 'login_text').send_keys('test')
        driver.find_element(By.ID, 'login_password').send_keys('test123')
        driver.find_element(By.ID, 'login_btn').click()

        alerta = driver.switch_to.alert
        assert alerta.text == 'validation succeeded'
        alerta.accept()

        driver.quit()


    def test_login_vacio(self):
        driver = webdriver.Chrome()
        driver.get('https://automationtesting.co.uk/loginPortal.html')

        driver.find_element(By.ID, 'login_btn').click()

        alerta = driver.switch_to.alert
        assert alerta.text == 'validation failed'
        alerta.accept()

        driver.quit()


    def test_login_incorrecto(self):
        driver = webdriver.Chrome()
        driver.get('https://automationtesting.co.uk/loginPortal.html')

        driver.find_element(By.ID, 'login_text').send_keys('usuario')
        driver.find_element(By.ID, 'login_password').send_keys('clave')
        driver.find_element(By.ID, 'login_btn').click()

        alerta = driver.switch_to.alert
        assert alerta.text == 'validation failed'
        alerta.accept()

        driver.quit()

#python -m pytest -v tps/test_login_portal.py