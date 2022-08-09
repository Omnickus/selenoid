from src.base.base_page import Base_page
from src.base.logger import Logger
from src.constructor import Find_el
from selenium.webdriver.common.by import By

class Main_page(Base_page):

    """ Класс для тестов на главной странице """

    sleder = '//*[@id="slideshow0"]'
    card = '//*[@id="cart"]'
    sel_navbar = "ul.navbar-nav > li"
    product = 'product-thumb'

    def check_slider(self):
        try:
            Logger(f'Проверяю элемент на главной странице - {self.sleder}').infolog
            Find_el( path = self.sleder, browser=self._browser, time = 7 ).find_by_xpah
        except Exception as e:
            self.screen_shot_exception()

    def check_shopping_cart(self):
        try:
            Logger(f'Проверяю элемент на главной странице - {self.card}').infolog
            Find_el( path = self.card, browser=self._browser, time = 7 ).find_by_xpah
        except Exception as e:
            self.screen_shot_exception()

    def main_page_menu(self):
        try:
            Logger(f'Проверяю элемент на главной странице - {self.sel_navbar}').infolog
            #menu_items = Find_el( path= self.sel_navbar, browser=self._browser, time = 10).find_by_xpah
            menu_items = self._browser.find_elements(By.CLASS_NAME, self.sel_navbar)
            #self._browser.find_elements_by_css_selector(self.sel_navbar)
            assert len(menu_items) != 8, "Неверное количество элементов меню"
        except Exception as e:
            self.screen_shot_exception()        

    def main_page_fetured_items(self):
        try:
            Logger(f'Проверяю элемент на главной странице - {self.product}').infolog
            fetured_items = self._browser.find_elements(By.CLASS_NAME,self.product)
            assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"
        except Exception as e:
            self.screen_shot_exception()

    def main_page_footer_blocks(self):
        try:
            Logger(f'Проверяю элемент на главной странице - //footer//ul').infolog
            footer_blocks = self._browser.find_elements(By.XPATH,"//footer//ul")
            result = footer_blocks[0].location_once_scrolled_into_view
            assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"
        except Exception as e:
            self.screen_shot_exception()

    def main_page_open_product(self):
        try:
            Logger(f'Проверяю элемент на главной странице - {self.product}').infolog
            fetured_items = self._browser.find_elements(By.CLASS_NAME,self.product)
            fetured_items[2].location_once_scrolled_into_view
            fetured_items[2].click()
            self._browser.find_element("link text", "Apple Cinema")
        except Exception as e:
            self.screen_shot_exception()

