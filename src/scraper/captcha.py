from halo import Halo
from subprocess import call
from threading import Thread
from xdg import BaseDirectory

_SLT_URL = 'https://www.internetvas.slt.lk/SLTVasPortal-war/application/index.nable'


class Captcha(Thread):
    def __init__(self, browser):
        super().__init__()
        self.browser = browser
        self.spinner = Halo(text='Loading', spinner='dots')
        self._show_captcha()

    def _show_captcha(self):
        xdg_captcha_cache = BaseDirectory.save_cache_path('slt-usage') + '/cap.png'
        self.spinner.start()
        self.browser.get(_SLT_URL)
        elem = self.browser.find_element_by_css_selector('tr > td > img')
        with open(xdg_captcha_cache, 'w+b') as f:
            f.write(elem.screenshot_as_png)

        self.spinner.stop()

        call(['termpix', xdg_captcha_cache, '--true-colour', '--width', '97', '--height', '19'])
