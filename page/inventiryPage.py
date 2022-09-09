import collections

from selene.support import by
from selene.support.jquery_style_selectors import ss, s

from utils.Utils import LOG, headerPrecondicion

productOptionExpected = ["Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"]

pageAdress = 'https://www.saucedemo.com/inventory.html'

productSortCmb = s(by.xpath("//select[@class=\"product_sort_container\"]"))
userPasswordLocator = s(by.name('password'))
loginBtnLocator = s(by.name('login-button'))

productOptionSortCmb = s(by.xpath("//select[@class='product_sort_container']"))
productOptionList = ss(by.xpath("//select[@class='product_sort_container']//option"))


def compareProductOption():
    headerPrecondicion()
    LOG("--- --- ожидаемые значения: " + str(productOptionExpected))
    listEl = [i.text for i in productOptionList]
    LOG("--- --- актуальные значения: " + str(listEl))
    if collections.Counter(productOptionExpected) == collections.Counter(listEl):
        LOG("--- --- данные совпадают : ")
        return True
    else:
        LOG("--- --- ERROR данные не совпадают : ")
        return False

