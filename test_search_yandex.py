import pytest
from selene import browser, have, be



@pytest.fixture
def open_yandex():
    print("\nTEST YANDEX_start")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://ya.ru'
    browser.open('/')  # теперь просто слеш
    yield
    browser.quit()
    print("\nTEST YANDEX_end")

def test_ya_search(open_yandex):
    search_input = browser.element('#text')
    search_input.should(be.visible).should(be.clickable)
    search_input.should(have.attribute('placeholder').value('Найдётся всё'))
    search_input.send_keys('fixture python pytest')
    suggestions = browser.all('[role="listbox"]') # элементы выпадающего списка
    suggestions.should(have.size_greater_than(0))
    suggestions.element_by(have.text('fixture python pytest')).should(be.visible).should(be.clickable)
    browser.element('[aria-label="Найти"]').should(be.visible).should(be.clickable).click()
    browser.should(have.script_returned(True, 'return document.readyState === "complete"'))
    browser.should(have.url_containing('/search'))
    browser.element('.main__content').should(be.visible)
    browser.element('.Distribution-SplashScreenModalContent').should(be.visible)
    browser.element('.Distribution-Actions > button').should(be.visible).click()










