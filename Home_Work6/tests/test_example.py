""" text """
import time


def test_check_title_chrome(browser):
    """ text """
    browser.get('https://google.com/')

    assert "Google" in browser.title
    time.sleep(1)
    browser.quit()
