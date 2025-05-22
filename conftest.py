import pytest


@pytest.fixture(scope="session")
def window_mode():
    print ("Браузер!")
    yield
    print("Закрываем браузер!")


import pytest
from selene import browser

@pytest.fixture(scope="function")
def window_browser_mode():

    # Настройка браузера перед тестом

    browser.config.window_width = 1900
    browser.config.window_height = 1000
    print("   Открываем браузер - размеры окна описаны в фикстуре!")
    yield
    # Очистка после теста
    browser.quit()
    print("   Закрываем браузер")