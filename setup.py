# -*- coding: utf-8 -*-
###
# (C) Copyright [2019] Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###


from setuptools import find_packages
from setuptools import setup

setup(name='hpOneView',
      version='5.0.0-beta',
      description='HPE OneView Python Library',
      url='https://github.com/HewlettPackard/python-hpOneView',
      download_url="https://github.com/HewlettPackard/python-hpOneView/tarball/v5.0.0-beta",
      author='Hewlett Packard Enterprise Development LP',
      author_email='oneview-pythonsdk@hpe.com',
      license='MIT',
      packages=find_packages(exclude=['examples*', 'tests*']),
      keywords=['oneview', 'hpe'],
      install_requires=['future>=0.15.2'])