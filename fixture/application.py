from selenium import webdriver
from fixture.session import SessionHelper
from fixture.filebrowser import FilebrowserHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.maximize_window()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
            self.wd.maximize_window()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.filebrowser = FilebrowserHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/filebrowser/"):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()