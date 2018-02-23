from setuptools import setup, find_packages

setup(
    name='slt',
    packages=find_packages(),
    version='0.10.3',
    description='Unofficial usage checker for SLT Internet',
    author='Amal Karunarathna',
    author_email='nasashinega@gmail.com',
    url='https://github.com/r3b311i0n/slt-usage',
    download_url='https://github.com/r3b311i0n/slt-usage/archive/0.9.0.tar.gz',
    keywords=['lk', 'sri lanka', 'internet', 'isp', 'terminal', 'internet usage', 'slt', 'selenium'],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: End Users/Desktop',
                 'Intended Audience :: Telecommunications Industry',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6'],
    install_requires=['selenium', 'halo', 'colorama', 'pyxdg', 'Pillow'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'slt=slt:main',
        ],
    },
)
