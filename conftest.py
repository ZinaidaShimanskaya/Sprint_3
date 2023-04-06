import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()
