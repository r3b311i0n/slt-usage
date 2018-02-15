import json
import sys
from xdg import BaseDirectory

from .scraper import Scraper


def get_settings():
    conf_path = './conf.json' if (sys.platform == 'win32') \
        else BaseDirectory.save_config_path('slt-usage') + '/conf.json'
    try:
        conf = json.load(open(conf_path))
    except FileNotFoundError:
        conf = create_conf(conf_path)
    user = conf['user']
    password = conf['password']
    return [user, password]


def create_conf(conf_path):
    print('Please enter your SLT username:\n')
    username = sys.stdin.readline()
    print('Please enter your SLT password:\n')
    password = sys.stdin.readline()
    conf = json.dumps({'user': username, 'password': password})
    with open(conf_path, 'w+') as f:
        f.write(conf)

    return json.load(open(conf_path))


def main():
    settings = get_settings()
    Scraper(settings[0], settings[1])
