import allure

from utils.base.BaseTest import BaseTest
from utils.enums.UsersEnum import UsersEnum
from page.inventiryPage import productSortCmb, compareProductOption
from utils.Action import Action
from utils.steps.baseStep.BaseStep import BaseStep


class TestClass(BaseTest):

    @allure.feature('Login')
    @allure.story('Проверка логина (Positive)')
    def test_52145(self):
        Action() \
            .open('https://www.saucedemo.com/') \
            .step(BaseStep.printMethod(), "промежуточный шаг")\
            .login(UsersEnum.STANDARTUSER) \
            .click(productSortCmb, "Сортировка продуктов (Комбобокс)")\
            .check(compareProductOption(), "список видимый и соответсвует ожидаемому")

