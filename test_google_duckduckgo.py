from selene import browser, have, be


def test_google_captcha_should_be_shown(log_test, open_google):
    browser.element('[name="q"]').should(be.visible).type('qa.guru')
    browser.element('[name="btnK"]').should(be.visible).should(be.clickable).click()
    browser.element('html').should(have.text('Об этой странице'))

def test_other_site_search_positive(log_test, open_duck):
    # browser.element('[placeholder="Поиск без отслеживания"]').should(have.attribute('placeholder').value('Поиск без отслеживания'))
    browser.element('[id="searchbox_input"]').should(be.visible).type('tutorials selene github')
    browser.element('[type="submit"]').should(be.visible).should(be.clickable).click()
    browser.element('[id="web_content_wrapper"]').should(have.text('GitHub - FunctionLab/selene: a framework for training '))

def test_other_site_search_negative(log_test, open_duck):
    #browser.element('[placeholder="Поиск без отслеживания"]').should(have.attribute('placeholder').value('Поиск без отслеживания'))
    browser.element('[id="searchbox_input"]').should(be.visible).type('%*(&*^%^$%$&%^(*^*(&%^#$%^*$(^&^&%^$^&*%^&*(^')
    browser.element('[type="submit"]').should(be.visible).should(be.clickable).click()
    browser.element('[id=react-layout]').should(have.text('По запросу «%*(&*^%^$%$&%^(*^*(&%^#$%^*$(^&^&%^$^&*%^&*(^» ничего не найдено.'))


