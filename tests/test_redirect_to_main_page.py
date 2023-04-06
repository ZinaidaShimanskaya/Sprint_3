from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locator
class TestRedirectToMainPage:
    def test_redirect_to_constructor_by_click_user_redirected(self, driver): #переход из "Личного кабинета" в "Конструктор" по клику
        driver.find_element(*Locator.personal_account_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locator.login_button))
        driver.find_element(*Locator.constructor_page).click()
        check_header = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.header_make_burger)).text
        assert check_header == 'Соберите бургер'

    def test_redirect_to_main_page_by_click_on_logo_user_redirected(self, driver): #переход из "Личного кабинета" на главную по клику на логотип
        driver.find_element(*Locator.personal_account_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locator.login_button))
        driver.find_element(*Locator.logo_stella_burgers).click()
        check_header_text = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.header_make_burger)).text
        assert check_header_text == 'Соберите бургер'