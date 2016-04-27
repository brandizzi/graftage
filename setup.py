#!/usr/bin/env python
#
# Copyright 2016 Adam Victor Brandizzi
#
# This file is part of Graftage.
#
# Graftage is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Graftage is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Graftage. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name="graftage",
    version="0.0.1.dev1",
    author='Adam Victor Brandizzi',
    author_email='adam@brandizzi.com.br',
    description='graftage',
    license='LGPLv3',
    url='http://bitbucket.com/brandizzi/graftage',

    packages=find_packages(),
    test_suite='graftage.tests',
    test_loader='unittest:TestLoader',
)
