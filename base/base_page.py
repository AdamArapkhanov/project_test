import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver




    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url -" + get_url)


    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot("C:\\Users\\Адам\\PycharmProjects\\project_test\\screen\\" + name_screenshot)




    def assert_check_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("good assert word")

    def make_text(self, some):
        some = some.text
        return some







