import os
from setuptools import setup, find_packages

setup(
    name='trfind',
    version='0.0.5',
    author='Jason Curtis and Jaime McCandless',
    description='Finds trip reports from the Internet',
    url='http://github.com/thatneat/trfind',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'Flask',
        'Flask-Cors',
        'lxml',
        'petl',
        'python-dateutil',
        'requests',
    ],
    entry_points={
        'console_scripts': ['trfind = trfind.find:main']
    },
    include_package_data=True
)
