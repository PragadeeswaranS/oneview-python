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

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()


from hpOneView.resources.resource import Resource, ResourcePatchMixin, unavailable_method


class SasInterconnects(ResourcePatchMixin, Resource):
    """
    SAS Interconnects API client.

    Note:
        This resource is only available on HPE Synergy.

    """
    URI = '/rest/sas-interconnects'

    def __init__(self, connection, data=None):
        super(SasInterconnects, self).__init__(connection, data)

    def get_all(self, start=0, count=-1, fields='', filter='', query='', sort='', view=''):
        """
        Get list of SAS interconnects each with port details.

        Args:
            start:
                 The first item to return, using 0-based indexing. If not specified, the default is 0 - start with the
                 first available item.
            count:
                The number of resources to return. A count of -1 requests all items. The actual number of items in
                the response may differ from the requested count if the sum of start and count exceeds the total number
                of items.
            fields:
                 Specifies which fields should be returned in the result set.
            filter (list or str):
                 A general filter/query string to narrow the list of items returned. The default is no filter; all
                 resources are returned.
            query:
                 A general query string to narrow the list of resources returned. The default is no query (all
                 resources are returned).
            sort:
                The sort order of the returned data set. By default, the sort order is based on create time, with the
                oldest entry first.
            view:
                 Returns a specific subset of the attributes of the resource or collection, by specifying the name of a
                 predefined view. The default view is expand (show all attributes of the resource and all elements of
                 collections of resources).

        Returns:
            list: A list of SAS interconnects.
        """
        return self._helper.get_all(start=start, count=count, filter=filter, query=query, sort=sort, view=view,
                                    fields=fields)

    def refresh_state(self, configuration):
        """
        Refresh a SAS Interconnect.

        Args:
            configuration: Configuration

        Returns:
            dict: SAS Interconnect
        """
        uri = "{}/refreshState".format(self.data["uri"])
        return self._helper.update(uri=uri, resource=configuration)

    def create(self):
        """Create method is not available"""
        unavailable_method()

    def delete(self):
        """Delete method is not available"""
        unavailable_method()

    def update(self):
        """Update method is not available"""
        unavailable_method()
