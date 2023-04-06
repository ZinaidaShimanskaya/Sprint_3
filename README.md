# Sprint_3
Проект автоматизации тестирования сервиса Stella Burgers.
Основа для написания автотестов — фреймворк pytest.
Команда для запуска — pytest -v.

Описание тестов:

Регистрация с корректным именем, емейлом и паролем
test_signup_with_name_email_password_successful

#регистрация с паролем меньше 6 символов
test_signup_with_password_less_than_6characters_error_appears

#логин по кнопке "Войти в аккаунт" на главной
test_login_with_login_to_acc_button_user_logged_in

#логин по кнопке "Личный кабинет"
test_login_by_personal_account_button_user_logged_in

#логин по ссылке в форме регистрации
test_login_by_sign_up_link_user_signed_in

#вход по ссылке в форме восстановления пароля
test_login_by_forgot_password_link_user_logged_in

#переход по клику на "Личный кабинет" 
test_redirect_to_personal_acc_by_click_user_redirected

#переход из "Личного кабинета" в "Конструктор" по клику
test_redirect_to_constructor_by_click_user_redirected

#переход из "Личного кабинета" на главную по клику на логотип
test_redirect_to_main_page_by_click_on_logo_user_redirected

#выход из аккаунта по кнопке "Выход" в личном кабинете
test_logout_by_logout_button_user_logged_out

#переход из раздела "Конструктор" в раздел "Булки"
test_redirect_to_buns_user_redirected

#переход из раздела "Конструктор" в раздел "Соусы"
test_redirect_to_sauces_user_redirected

#переход из раздела "Конструктор" в раздел "Начинки"
test_redirect_to_fillings_user_redirected