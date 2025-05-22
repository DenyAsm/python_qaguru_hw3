import pytest
from selene import browser, have, Browser, be


def test_captcha_should_be_shown(window_browser_mode):
    browser.open('https://google.com')
    browser.element('[name="q"]').type('qa.guru')
    browser.element('[name="btnK"]').should(be.visible)
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('Об этой странице'))
