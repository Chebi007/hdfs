
from selenium.webdriver.common.action_chains import ActionChains
import os.path
import time


class FilebrowserHelper:

    def __init__(self, app):
        self.app = app

    def open_filebrowser(self):
        wd = self.app.wd
        wd.find_element_by_link_text("File Browser").click()

    def add_directory(self, directory):
        wd = self.app.wd
        self.open_filebrowser()
        wd.find_element_by_link_text("New").click()
        wd.find_element_by_xpath("//a[@title='Directory']").click()
        button = wd.find_element_by_id("newDirectoryNameInput")
        time.sleep(1)
        ActionChains(wd).send_keys_to_element(button, directory.name).perform()
        wd.find_element_by_xpath("//input[@value='Create']").click()

    def get_file_list(self):
        wd =self.app.wd
        self.open_filebrowser()
        l =[]
        for row in wd.find_elements_by_id("files"):
            cells = row.find_elements_by_tag_name("strong")
            for i in cells:
                l.append(i.text)
        return l

    def add_file(self, file):
        wd = self.app.wd
        wd.find_element_by_link_text("File Browser").click()
        wd.find_element_by_name("file").send_keys(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ('data\\files\\' + str(file))))


    def delete_dir_and_files(self):
        wd = self.app.wd
        self.open_filebrowser()
        wd.find_element_by_xpath("//th/div").click()
        wd.find_element_by_xpath("//tbody[@id='files']/tr[3]/td/div").click()
        wd.find_element_by_id("trash-btn").click()
        time.sleep(2)
        wd.find_element_by_xpath("//input[@value='Да']").click()


    def restore_from_trash(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//tbody[@id='files']/tr[4]/td/div").click()
        wd.find_element_by_id("trash-btn").click()
        wd.find_element_by_xpath("//input[@value='Да']").click()
        wd.find_element_by_link_text("Trash").click()
        wd.find_element_by_xpath("//tr[3]/td/div").click()
        wd.find_element_by_xpath("//button[@title='Restore from trash']").click()
        button = wd.find_element_by_xpath("//form[@id='restoreTrashForm']/input[2]")
        time.sleep(2)
        ActionChains(wd).click(button).perform()
        time.sleep(2)

