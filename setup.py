from distutils.core import setup

setup(
    name='slt-usage',
    packages=['slt-usage'],
    version='0.9.0',
    description='Unofficial usage checker for SLT Internet',
    author='Amal Karunarathna',
    author_email='nasashinega@gmail.com',
    url='https://github.com/r3b311i0n/slt-usage',
    download_url='https://github.com/r3b311i0n/slt-usage/archive/0.9.0.tar.xz',
    keywords=['lk', 'sri lanka', 'internet', 'isp', 'terminal', 'internet usage', 'slt', 'selenium'],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Sri Lankans',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6'],
    install_requires=['selenium', 'halo', 'colorama', 'pyxdg', 'Pillow'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'slt-usage=slt-usage:main',
        ],
    },
)