from selenium.webdriver.common.by import By
class Locator:

    # Главная:
    # кнопка "Войти в аккаунт"
    login_into_acc_button = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    # кнопка "Личный кабинет"
    personal_account_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
    # логотип "Stellar Burgers"
    logo_stella_burgers = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    # раздел "Конструктор"
    constructor_page = (By.XPATH, ".//p[text()='Конструктор']")
    # вкладка "Булки"
    buns_tab = (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    # раздел  "Булки"
    buns_header = (By.XPATH, ".//h2[text()='Булки']")
    # вкладка "Соусы"
    sauces_tab = (By.XPATH, ".//span[text()='Соусы']")
    # раздел  "Соусы"
    sauces_header = (By.XPATH, ".//h2[text()='Соусы']")
    # вкладка "Начинки"
    fillings_tab = (By.XPATH, ".//span[text()='Начинки']")
    # раздел  "Начинки"
    fillings_header = (By.XPATH, ".//h2[text()='Начинки']")
    # заголовок Соберите бургер
    header_make_burger = (By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")

    # Вход:
    # поле "Email"
    email_login = (By.XPATH, ".//fieldset[1]//input[@name='name']")
    # поле "Пароль"
    password_login = (By.XPATH, ".//fieldset[2]//input[@name='Пароль']")
    # кнопка "Войти"
    login_button = (By.XPATH, ".//button[text()='Войти']")
    # кликабельная ссылка "Восстановить пароль"
    forgot_password_link = (By.XPATH, ".//a[@href='/forgot-password']")
    # кликабельная ссылка "Зарегистрироваться"
    sign_up_link = (By.XPATH, ".//a[@href='/register']")


    # Регистрация:
    # поле "Имя"
    name_input = (By.XPATH, ".//fieldset[1]//input[@name='name']")
    # поле "Email"
    email_input = (By.XPATH, ".//fieldset[2]//input[@name='name']")
    # поле "Пароль"
    password_input = (By.XPATH, ".//fieldset//input[@name='Пароль']")
    # кнопка "Зарегистрироваться"
    sign_up_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # кликабельная ссылка "Войти"
    login_link = (By.XPATH, ".//a[@href='/login']")
    # некорректный пароль
    incorrect_password_error = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # Личный кабинет:
    # кнопка "Выход"
    logout_button = (By.XPATH, ".//button[text()= 'Выход']")
    # кнопка "Оформить заказ"
    place_order = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # раздел "История заказов"
    history_orders_link = (By.XPATH, ".//a[@href='/account/order-history']")