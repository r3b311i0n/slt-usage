from colorama import init, Fore, Style
from halo import Halo
from PIL import Image
from selenium import webdriver
from subprocess import call
from threading import Thread
from xdg import BaseDirectory

_SLT_URL = 'https://www.internetvas.slt.lk/SLTVasPortal-war/application/index.nable'


class Captcha(Thread):
    def __init__(self, browser: webdriver, platform: str):
        super().__init__()
        self.browser = browser
        self.platform = platform
        self.spinner = Halo(text='Loading...', spinner='dots')
        self._show_captcha()

    def _show_captcha(self):
        xdg_captcha_cache = './cap.png' if (self.platform == 'win32') \
            else BaseDirectory.save_cache_path('slt-usage') + '/cap.png'
        if self.platform != 'win32':
            self.spinner.start()
        self.browser.get(_SLT_URL)
        elem = self.browser.find_element_by_css_selector('tr > td > img')
        with open(xdg_captcha_cache, 'w+b') as f:
            f.write(elem.screenshot_as_png)

        if self.platform != 'win32':
            self.spinner.stop()

        try:
            call(['termpix', xdg_captcha_cache, '--true-colour', '--width', '97', '--height', '19'])
        except FileNotFoundError:
            init()
            print(Fore.RED + Style.BRIGHT +
                  '\nInstall termpix (https://github.com/hopey-dishwasher/termpix)'
                  ' to view captcha inline on the terminal!')
            Image.open(xdg_captcha_cache).show()
