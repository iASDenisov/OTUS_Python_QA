""" text """
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
    """ 1st fixture """
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    driver = None

    if browser_name == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'ff':
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == 'ya':
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(executable_path='C:/yandexdriver')
        driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    return driver
