from halo import Halo
from subprocess import call
from threading import Thread

_SLT_URL = 'https://www.internetvas.slt.lk/SLTVasPortal-war/application/index.nable'


class Captcha(Thread):
    def __init__(self, browser):
        super().__init__()
        self.browser = browser
        self.spinner = Halo(text='Loading', spinner='dots')
        self._show_captcha()

    def _show_captcha(self):
        self.spinner.start()
        self.browser.get(_SLT_URL)
        elem = self.browser.find_element_by_css_selector('tr > td > img')
        with open('cap.png', 'w+b') as f:
            f.write(elem.screenshot_as_png)

        self.spinner.stop()

        call(['termpix', 'cap.png', '--true-colour', '--width', '97', '--height', '19'])
