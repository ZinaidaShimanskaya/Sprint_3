from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator
class TestRedirectToPersonalAcc:
    def test_redirect_to_personal_acc_by_click_user_redirected(self, driver): #переход по клику на "Личный кабинет"
        driver.find_element(*Locator.login_into_acc_button).click()
        driver.find_element(*Locator.email_login).send_keys("zinashimanskaya0801@yandex.ru")
        driver.find_element(*Locator.password_login).send_keys("123456789")
        driver.find_element(*Locator.login_button).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.place_order))
        driver.find_element(*Locator.personal_account_button).click()
        history_orders = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.history_orders_link)).text
        assert history_orders == 'История заказов'