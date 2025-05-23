
import pytest
from selene import browser, have

@pytest.fixture # по дефолту scope = "function"
def log_test():
    print("\nTEST_start")
    yield
    print("TEST_end")


@pytest.fixture(scope="function") # опционально, по дефолту in
def window_browser_mode():
    browser.config.window_width = 2560
    browser.config.window_height = 1440
    print("OPEN - size mode")
    yield
    browser.quit()
    print("\nCLOSE")

@pytest.fixture
def open_google(window_browser_mode):
    browser.open('https://google.com')
    browser.should(have.script_returned(True, 'return document.readyState === "complete"'))

    print("Open main - Google")
    yield

@pytest.fixture
def open_duck(window_browser_mode):
    browser.open('https://duckduckgo.com/')
    browser.should(have.script_returned(True, 'return document.readyState === "complete"'))

    print('Open other site - Duck')
    yield