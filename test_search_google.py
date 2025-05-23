from selene import browser, have, be


def test_captcha_should_be_shown(log_test, open_google):
    browser.element('[name="q"]').should(be.visible)
    browser.element('[name="q"]').type('qa.guru')
    browser.element('[name="btnK"]').should(be.visible).should(be.clickable)
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('Об этой странице'))



def test_other_site_show(log_test, open_other_browser):
    browser.should(have.script_returned(True, 'return document.readyState === "complete"'))
    browser.element('[placeholder="Поиск без отслеживания"]').should(have.attribute('placeholder').value('Поиск без отслеживания'))
    browser.element('[data-testid="hero"]').should(have.text('Подробнее'))
    browser.element('[id="searchbox_input"]').type('%*(&*^%^$%$&%^(*^*(&%^#$%^*$(^&^&%^$^&*%^&*(^')
    browser.element('[type="submit"]').should(be.visible).should(be.clickable)
    browser.element('[type="submit"]').click()
    browser.element('[id=react-layout]').should(have.text('По запросу «%*(&*^%^$%$&%^(*^*(&%^#$%^*$(^&^&%^$^&*%^&*(^» ничего не найдено.'))


