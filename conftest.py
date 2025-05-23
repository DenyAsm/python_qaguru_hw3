import pytest
from selene import browser, have

@pytest.fixture
def log_test():
    print("\nTEST_start")
    yield
    print("TEST_end")


@pytest.fixture(scope="function")
def window_browser_mode():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    print("OPEN - Window size mode")
    yield
    browser.quit()
    print("\nCLOSE")

@pytest.fixture
def open_google(window_browser_mode):
    browser.open('https://google.com')
    browser.should(have.script_returned(True, 'return document.readyState === "complete"'))
    print("Open main Google")
    yield

@pytest.fixture
def open_other_browser(window_browser_mode):
    browser.open('https://duckduckgo.com/')
    browser.should(have.script_returned(True, 'return document.readyState === "complete"'))
    print('Open other site - Duck')
    yield