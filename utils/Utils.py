import logging

import selene.api
import selenium.webdriver

logging.basicConfig(level=logging.INFO)
LOGING = logging.getLogger()


def getWebBrowser() -> selenium.webdriver.Chrome:
    return selene.api.browser.driver()


def LOG(message: str):
    LOGING.info(message)


def headerPrecondicion():
    LOG("")
    LOG("")
    LOG("")
    LOG("--- подготовка к проверке")
