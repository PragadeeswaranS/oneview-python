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
import mock
import unittest

from hpOneView.connection import connection
from hpOneView.resources.resource import ResourceClient
from hpOneView.resources.servers.id_pools import IdPools


class TestIdPools(unittest.TestCase):
    resource_info = {'type': 'Range',
                     'name': 'No name'}
    example_uri = "/rest/id-pools/ipv4"

    def setUp(self):
        self.host = '127.0.0.1'
        self.connection = connection(self.host)
        self.client = IdPools(self.connection)

    @mock.patch.object(ResourceClient, 'get')
    def test_get_called_once_by_id(self, mock_get):
        id_pools_range_id = "f0a0a113-ec97-41b4-83ce-d7c92b900e7c"
        self.client.get(id_pools_range_id)
        mock_get.assert_called_once_with(id_pools_range_id)

    @mock.patch.object(ResourceClient, 'get')
    def test_get_called_once_by_uri(self, mock_get):
        self.client.get(self.example_uri)
        mock_get.assert_called_once_with(self.example_uri)

    @mock.patch.object(ResourceClient, 'get')
    def test_generate_called_once(self, mock_get):
        self.client.generate(self.example_uri)
        mock_get.assert_called_once_with(self.example_uri + '/generate')

    @mock.patch.object(ResourceClient, 'get')
    def test_validate_id_pool_called_once(self, mock_get):
        self.client.validate_id_pool(self.example_uri, ['VCGYOAA023',
                                                        'VCGYOAA024'])
        mock_get.assert_called_once_with(self.example_uri + "/validate?idList=VCGYOAA023&idList=VCGYOAA024")

    @mock.patch.object(ResourceClient, 'update')
    def test_validate_called_once(self, update):
        self.client.validate(self.resource_info.copy(), self.example_uri)
        update.assert_called_once_with(self.resource_info.copy(), self.example_uri + "/validate", timeout=-1)

    @mock.patch.object(ResourceClient, 'update')
    def test_enable_called_once(self, update):
        self.client.enable(self.resource_info.copy(), self.example_uri)
        update.assert_called_once_with(self.resource_info.copy(), self.example_uri, timeout=-1)

    @mock.patch.object(ResourceClient, 'get')
    def test_get_check_range_availability_called_once_with_defaults(self, mock_get):
        self.client.get_check_range_availability(self.example_uri, ['VCGYOAA023',
                                                                    'VCGYOAA024'])
        mock_get.assert_called_once_with(
            self.example_uri + "/checkrangeavailability?idList=VCGYOAA023&idList=VCGYOAA024")

    @mock.patch.object(ResourceClient, 'update')
    def test_allocate_called_once(self, mock_update):
        self.client.allocate(self.resource_info.copy(), self.example_uri)
        mock_update.assert_called_once_with(self.resource_info.copy(), self.example_uri + "/allocator", timeout=-1)

    @mock.patch.object(ResourceClient, 'update')
    def test_collect_called_once(self, update):
        self.client.collect(self.resource_info.copy(), self.example_uri)
        update.assert_called_once_with(self.resource_info.copy(), self.example_uri + "/collector", timeout=-1)
