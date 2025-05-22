import pytest
from selene import browser, have, Browser, be


def test_captcha_should_be_shown(log_test, open_google):
    #browser.open('https://google.com') # не обязательно, в open_google fixture прокинул
    browser.element('[name="q"]').type('qa.guru')
    browser.element('[name="btnK"]').should(be.visible)
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('Об этой странице'))


