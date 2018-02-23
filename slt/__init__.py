import json
import sys
from .scraper import Scraper
from xdg import BaseDirectory


# TODO: Handle network errors.
# TODO: Use a gif in README.md.

def get_settings(platform_conf):
    conf_path = './conf.json' if (platform_conf == 'win32') \
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
    platform = sys.platform
    settings = get_settings(platform)
    Scraper(settings[0], settings[1], platform)
