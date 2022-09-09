import logging

import pytest
from selene import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()

@pytest.fixture(scope="class")
def driver_init(request):
    # driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4444/wd/hub',
    #     desired_capabilities={'browserName': 'htmlunit',
    #                           'version': '2',
    #                           'javascriptEnabled': True})
    # browser.set_driver(driver)
    browser.set_driver(webdriver.Chrome(ChromeDriverManager().install()))
    yield
    browser.quit()

