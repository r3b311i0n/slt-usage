import sys
import threading
from halo import Halo
from selenium import webdriver
from subprocess import call

_SLT_URL = 'https://www.internetvas.slt.lk/SLTVasPortal-war/application/index.nable'


# TODO: Handle lots of exceptions
class Scraper(threading.Thread):
    def __init__(self, user, password):
        super().__init__()
        self.spinner = Halo(text='Loading', spinner='dots')
        self.user = user
        self.password = password
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.binary_location = '/bin/firefox'
        self.firefox_options.set_headless(True)
        self.browser = webdriver.Firefox(firefox_options=self.firefox_options)
        self.show_captcha()
        self.submit_form()
        print(self.browser.current_url)

    @staticmethod
    def read_captcha_answer():
        print('Please enter captcha:')
        answer = sys.stdin.readline()
        return answer

    def submit_form(self):
        answer = self.read_captcha_answer()
        self.spinner.start()
        self.browser.find_element_by_xpath('//input[@placeholder="Portal Username eg: CEN2121212"]').\
            send_keys(self.user)
        self.browser.find_element_by_class_name('ui-password').send_keys(self.password)
        self.browser.find_element_by_xpath('//input[@placeholder="Enter Above Captcha"]').send_keys(answer)

        self.browser.find_element_by_xpath('//input[@value="Sign in"]').click()
        self.spinner.stop()

    def show_captcha(self):
        self.spinner.start()
        self.browser.get(_SLT_URL)
        elem = self.browser.find_element_by_css_selector('tr > td > img')
        with open('cap.png', 'w+b') as f:
            f.write(elem.screenshot_as_png)

        self.spinner.stop()

        call(['termpix', 'cap.png', '--true-colour', '--width', '97', '--height', '19'])

    def __del__(self):
        self.browser.quit()
