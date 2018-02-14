import sys
from colorama import init, Fore, Style
from halo import Halo
from selenium import webdriver
from scraper.captcha import Captcha


# TODO: Handle lots of exceptions (gecko-driver not found).

class Scraper:
    def __init__(self, user, password):
        init()
        self.spinner = Halo(text='Loading', spinner='dots')
        self.user = user
        self.password = password
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.binary_location = '/bin/firefox'
        self.firefox_options.set_headless(True)
        self.browser = webdriver.Firefox(firefox_options=self.firefox_options)
        Captcha(self.browser).start()
        self._submit_form()
        self._print_stats()

    @staticmethod
    def _read_captcha_answer():
        print('Please enter captcha:\n')
        answer = sys.stdin.readline()
        return answer

    def _print_stats(self):
        remainder = self.browser.find_elements_by_class_name('progress-label')
        try:
            print(Fore.CYAN +
                  f'\nTotal Volume:\n\n' +
                  Fore.MAGENTA +
                  f'{remainder[0].text}\n'
                  + Style.BRIGHT + Fore.RED + f'{remainder[1].text}\n'
                  + Style.NORMAL + Fore.MAGENTA + f'{remainder[2].text}' +
                  Fore.CYAN +
                  f'\n\n\nPeak Volume:\n\n' +
                  Fore.MAGENTA +
                  f'{remainder[3].text}\n'
                  + Style.BRIGHT + Fore.RED + f'{remainder[4].text}\n'
                  + Style.NORMAL + Fore.MAGENTA + f'{remainder[5].text}')
        except IndexError:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + 'Invalid Captcha!')
            self.browser.quit()
            Scraper(self.user, self.password)

    def _submit_form(self):
        answer = self._read_captcha_answer()
        if sys.platform != 'win32':
            self.spinner.start()
        self.browser.find_element_by_xpath('//input[@placeholder="Portal Username eg: CEN2121212"]'). \
            send_keys(self.user)
        self.browser.find_element_by_class_name('ui-password').send_keys(self.password)
        self.browser.find_element_by_xpath('//input[@placeholder="Enter Above Captcha"]').send_keys(answer)

        self.browser.find_element_by_xpath('//input[@value="Sign in"]').click()
        if sys.platform != 'win32':
            self.spinner.stop()

    def __del__(self):
        self.browser.quit()
