import time


def test_check_title_chrome(browser):
    browser.get('https://google.com/')

    assert "Google" in browser.title
    time.sleep(1)
    browser.quit()
# def test_check_title_firefox(browser):
#     browser = webdriver.Firefox()
#     browser.get('https://google.com/')
#
#     assert "Google" in browser.title
#     time.sleep(1)
#     browser.quit()
