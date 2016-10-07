# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-30 14:01:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-06 20:14:28


from distutils.core import setup
from setuptools import Extension,find_packages
from os import path

setup(
    name = 'digAgeDateExtractor',
    version = '0.1.0',
    description = 'digAgeDateExtractor',
    author = 'Lingzhe Teng',
    author_email = 'zwein27@gmail.com',
    url = 'https://github.com/usc-isi-i2/dig-age-extractor',
    download_url = 'https://github.com/usc-isi-i2/dig-age-extractor',
    packages = find_packages(),
    keywords = ['age', 'extractor'],
    install_requires=['digAgeDateExtractor']
    )