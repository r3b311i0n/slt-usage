import json
from scraper import Scraper


# Taken from https://stackoverflow.com/a/600612/119527 and modified


# def _mkdir_p(dir_path):
#     try:
#         os.makedirs(dir_path)
#     except OSError as exc:  # Python >2.5
#         if exc.errno == errno.EEXIST and os.path.isdir(dir_path):
#             pass
#         else:
#             raise
#
#
# def _safe_open_w(safe_path, mode):
#     """ Open "path" for writing, creating any parent directories as needed.
#     """
#     _mkdir_p(os.path.dirname(safe_path))
#     return open(safe_path, mode)


# Convert image from base64 to PNG.
# def _convert_img(img_path):
#     with open(img_path, 'rb') as f:
#         contents = f.read()
#         b64 = contents.partition(b',')[2]
#         pad = len(b64) % 4
#         b64 += b'=' * pad
#         print('Decoding image...')
#         png = codecs.decode(b64.strip(), 'base64')
#         # print(b64)
#         with _safe_open_w(capPath, 'w+b') as w:
#             print('Writing image to disk...')
#             w.write(png)

def get_settings():
    conf = json.load(open('./tmp/conf.json'))
    user = conf['user']
    password = conf['password']
    return [user, password]


if __name__ == '__main__':
    # capPath = './tmp/cap.png'
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument('path', help='Captcha file path')
    # args = argparser.parse_args()
    # path = args.path
    # _convert_img(path)
    settings = get_settings()
    Scraper(settings[0], settings[1])
