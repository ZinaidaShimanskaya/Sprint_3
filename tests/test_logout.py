from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator
class TestLogout:
    def test_logout_by_logout_button_user_logged_out(self, driver): #выход из аккаунта по кнопке "Выход" в личном кабинете
        driver.find_element(*Locator.login_into_acc_button).click()
        driver.find_element(*Locator.email_login).send_keys("zinashimanskaya0801@yandex.ru")
        driver.find_element(*Locator.password_login).send_keys("123456789")
        driver.find_element(*Locator.login_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locator.place_order))
        driver.find_element(*Locator.personal_account_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locator.logout_button)).click()
        check_logout = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locator.login_button)).text
        assert check_logout == 'Войти'