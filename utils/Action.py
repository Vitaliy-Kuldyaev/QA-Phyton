import time
import logging
import allure

import pytest
from selene.elements import SeleneElement
from selene.support.conditions import be
from page.mainPage import userNameLocator, loginBtnLocator, userPasswordLocator
from utils.Utils import getWebBrowser
from utils.steps import StepBase

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


class Action(object):
    @allure.step("Открытие страницы: {site}")
    def open(self, site):
        self.headerLog()
        LOG.info("Открытие страницы: " + site)
        getWebBrowser().get(site)
        self.footerLog()
        return self

    @allure.step("Логин под пользователем {user}")
    def login(self, user):
        LOG.info("-------------------------------------")
        LOG.info("------- Start  Работа алгритма логина")
        self.send(userNameLocator, user.a, "Логин установка пользователя")
        self.send(userPasswordLocator, user.b, "Логин установка пароля")
        self.click(loginBtnLocator, "кнопка LOGIN")
        LOG.info("------- END  Работа алгритма логина")
        LOG.info("-------------------------------------")
        return self

    @allure.step("Нажатие на элемент: {message}")
    def click(self, el: SeleneElement, message: str):
        LOG.info("-------------------------------------")
        LOG.info("------- Нажатие: " + message)
        el.should_be(be.visible, 10).click()
        LOG.info("-------------------------------------")
        return self

    def sleep(self, sec):
        time.sleep(sec)
        return self

    @allure.step("Заполнить элемент: {message}")
    def send(self, el: SeleneElement, value: str, message: str):
        LOG.info("Отправка значения:" + value + "  в элемент: " + el.tag_name + "  Описание: " + message)
        for i in range(5):
            self.headerLog()
            LOG.info("--- проверка на наличие элемента, установка значения")
            el.should(be.visible).should_be(be.enabled)
            LOG.info("--- очистка элемента")
            el.clear()
            LOG.info("--- установка значения: " + value)
            el.set(value)
            LOG.info("--- --- значениe text: " + el.text)
            LOG.info("--- --- значениe value: " + el.get_attribute('value'))
            if el.text == value or el.get_attribute('value') == value:
                logging.info("--- Значение установлено")
                break
            else:
                logging.info("--- ERROR значение не установлено, повтор: " + str(i))
            self.footerLog()
        return self

    @allure.step("Выполнить действия: {message}")
    def step(self, step: StepBase, message: str):
        LOG.info("")
        LOG.info("-------------------------------------")
        LOG.info("Выполнено действие: " + message)
        LOG.info("-------------------------------------")
        return self

    @allure.step("Проверка: {message}")
    def check(self, action: bool, message: str):
        self.headerLog()
        LOG.info("Проверка: " + message)
        assert action == True
        self.footerLog()
        return self

    def headerLog(self):
        LOG.info("")
        LOG.info("")
        LOG.info("____________________________________")
        LOG.info("-------------Start Step-------------")

    def footerLog(self):
        LOG.info("-------------End Step---------------")
        LOG.info("____________________________________")
