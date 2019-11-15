import os
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.1'

setup(
    name='nse_python_ipo',
    version=VERSION,

    packages=find_packages(),

    url='https://github.com/shriharishastry/nse-ipo-python',

    author='Shrihari Shastry',
    author_email='shriharishastrysmg@gmail.com',

    description='Python client library for NSE IPO API :'
                ' https://www.nseindia.com/technology/content/nnf/WEB_CBRICS_PROTOCOL_1.1.pdf',
    long_description=read('README.md'),
    license='MIT',

    keywords=['nse', 'ipo', 'api', 'client'],
)