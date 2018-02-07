import argparse
import codecs
import sys
import os, os.path
import errno

from captcha import resolve


# Taken from https://stackoverflow.com/a/600612/119527 and modified
def mkdir_p(dir_path):
    try:
        os.makedirs(dir_path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(dir_path):
            pass
        else:
            raise


def safe_open_w(safe_path, mode):
    """ Open "path" for writing, creating any parent directories as needed.
    """
    mkdir_p(os.path.dirname(safe_path))
    return open(safe_path, mode)


if __name__ == '__main__':
    capPath = './tmp/cap.png'
    argparser = argparse.ArgumentParser()
    argparser.add_argument('path', help='Captcha file path')
    args = argparser.parse_args()
    path = args.path
    with open(path, 'rb') as f:
        contents = f.read()
        b64 = contents.partition(b',')[2]
        pad = len(b64) % 4
        b64 += b'=' * pad
        print('Decoding image...')
        png = codecs.decode(b64.strip(), 'base64')
        print(b64)
        with safe_open_w(capPath, 'w+b') as w:
            print('Writing image to disk...')
            w.write(png)
    # capPath = './tmp/captcha.png'
    broken = resolve(capPath)
    with safe_open_w('./tmp/cap.txt', 'w+') as f:
        f.write(broken)
