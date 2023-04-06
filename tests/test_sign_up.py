from locator import Locator
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

faker = Faker()

class TestSignUp:
    def test_signup_with_name_email_password_successful(self, driver):  # регистрация с корректным именем, емейлом и паролем
        email = faker.email()
        driver.find_element(*Locator.login_into_acc_button).click()
        driver.find_element(*Locator.sign_up_link).click()
        driver.find_element(*Locator.name_input).send_keys("zina")
        driver.find_element(*Locator.email_input).send_keys(email)
        driver.find_element(*Locator.password_input).send_keys("123456")
        driver.find_element(*Locator.sign_up_button).click()
        login = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locator.login_button)).text
        assert login == 'Войти'

    def test_signup_with_password_less_than_6characters_error_appears(self, driver): # регистрация с паролем меньше 6 символов
        email = faker.email()
        driver.find_element(*Locator.login_into_acc_button).click()
        driver.find_element(*Locator.sign_up_link).click()
        driver.find_element(*Locator.name_input).send_keys("zina")
        driver.find_element(*Locator.email_input).send_keys(email)
        driver.find_element(*Locator.password_input).send_keys("123")
        driver.find_element(*Locator.sign_up_button).click()
        error_message = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locator.incorrect_password_error)).text
        assert error_message == 'Некорректный пароль'