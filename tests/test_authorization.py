from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator

class TestAuthorization:
    def test_login_with_login_to_acc_button_user_logged_in(self, driver): #логин по кнопке "Войти в аккаунт" на главной
        driver.find_element(*Locator.login_into_acc_button).click()
        driver.find_element(*Locator.email_login).send_keys("zinashimanskaya0801@yandex.ru")
        driver.find_element(*Locator.password_login).send_keys("123456789")
        driver.find_element(*Locator.login_button).click()
        order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.place_order)).text
        assert order_button_text == 'Оформить заказ'

    def test_login_by_personal_account_button_user_logged_in(self, driver): #логин по кнопке "Личный кабинет"
        driver.find_element(*Locator.personal_account_button).click()
        driver.find_element(*Locator.email_login).send_keys("zinashimanskaya0801@yandex.ru")
        driver.find_element(*Locator.password_login).send_keys("123456789")
        driver.find_element(*Locator.login_button).click()
        order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.place_order)).text
        assert order_button_text == 'Оформить заказ'

    def test_login_by_sign_up_link_user_signed_in(self, driver): #логин по ссылке в форме регистрации
        driver.find_element(*Locator.personal_account_button).click()
        driver.find_element(*Locator.sign_up_link).click()
        driver.find_element(*Locator.login_link).click()
        driver.find_element(*Locator.email_login).send_keys("zinashimanskaya0801@yandex.ru")
        driver.find_element(*Locator.password_login).send_keys("123456789")
        driver.find_element(*Locator.login_button).click()
        order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.place_order)).text
        assert order_button_text == 'Оформить заказ'

    def test_login_by_forgot_password_link_user_logged_in(self, driver): #вход по ссылке в форме восстановления пароля
        driver.find_element(*Locator.personal_account_button).click()
        driver.find_element(*Locator.forgot_password_link).click()
        driver.find_element(*Locator.login_link).click()
        driver.find_element(*Locator.email_login).send_keys("zinashimanskaya0801@yandex.ru")
        driver.find_element(*Locator.password_login).send_keys("123456789")
        driver.find_element(*Locator.login_button).click()
        order_button_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.place_order)).text
        assert order_button_text == 'Оформить заказ'

