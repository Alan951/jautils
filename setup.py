from setuptools import setup, find_packages

NAME = 'jautils-library'
VERSION = '0.1'

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(include=['jautils']),
    #packages=find_packages(where='src'),
    setup_requires=['wheel'],
    include_package_data=True
)