import pytest
from selene import browser

@pytest.fixture
def log_test():

    print("\nStart TEST ...")
    yield
    print("End TEST")


@pytest.fixture(scope="function")
def window_browser_mode():

    browser.config.window_width = 2000
    browser.config.window_height = 1200
    print("OPEN - Window size mode")
    yield
    browser.quit()
    print("CLOSE")

@pytest.fixture
def open_google(window_browser_mode):

    browser.open('https://google.com')
    print("Open main Google")
    yield
