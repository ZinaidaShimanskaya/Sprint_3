from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator
class TestRedirectToTabs:
    def test_redirect_to_buns_user_redirected(self, driver): #переход из раздела "Конструктор" в раздел "Булки"
        driver.find_element(*Locator.constructor_page).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.buns_tab))
        check_buns_header = driver.find_element(*Locator.buns_header).text
        assert check_buns_header == 'Булки'

    def test_redirect_to_sauces_user_redirected(self, driver): #переход из раздела "Конструктор" в раздел "Соусы"
        driver.find_element(*Locator.constructor_page).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.sauces_tab)).click()
        check_sauces_header = driver.find_element(*Locator.sauces_header).text
        assert check_sauces_header == 'Соусы'

    def test_redirect_to_fillings_user_redirected(self, driver): #переход из раздела "Конструктор" в раздел "Начинки"
        driver.find_element(*Locator.constructor_page).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locator.fillings_tab)).click()
        check_fillings_header = driver.find_element(*Locator.fillings_header).text
        assert check_fillings_header == 'Начинки'