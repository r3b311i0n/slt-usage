import pytesseract
import sys
import argparse

try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output


def resolve(img_path):
    print('Resampling the Image')
    # check_output(['convert', img_path, '-resample', '600', img_path])
    return pytesseract.image_to_string(Image.open(img_path), lang='eng')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('path', help='Captcha file path')
    args = argparser.parse_args()
    path = args.path
    print('Resolving Captcha')
    captcha_text = resolve(path)
    print('Extracted Text', captcha_text)
    with open('cap.txt', 'w+') as f:
        f.write(captcha_text)
