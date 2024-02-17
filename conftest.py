import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    """ pytest hooks """
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    browser = None

    if browser_name == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'ff':
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        browser = webdriver.Firefox(options=options)
    elif browser_name == 'ya':
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(executable_path='C:/yandexdriver')
        browser = webdriver.Chrome(service=service)

    browser.maximize_window()
    return browser
