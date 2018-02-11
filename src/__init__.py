import json
from scraper import Scraper


def get_settings():
    conf = json.load(open('./tmp/conf.json'))
    user = conf['user']
    password = conf['password']
    return [user, password]


if __name__ == '__main__':
    settings = get_settings()
    Scraper(settings[0], settings[1])
