# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2017) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from pprint import pprint

from config_loader import try_load_from_file
from hpOneView.oneview_client import OneViewClient

config = {
    "ip": "",
    "credentials": {
        "userName": "",
        "password": ""
    }
}

# Try load config from a file (if there is a config file)
config = try_load_from_file(config)

oneview_client = OneViewClient(config)

# Retrieve Internal CA Certificate
print('Get the internal Certificate Authority:')
certificate = oneview_client.certificate_authority.get()
pprint(certificate)

# Retrieve Certificate Revocation List
print("Getting the Certificate Revocation List")
certificate_visual_content = oneview_client.certificate_authority.get_crl()
pprint(certificate_visual_content)

# Revoke Internal CA Signed Certificate
print("Revoking Internal CA Signed Certificate")
success = oneview_client.certificate_authority.delete("default")
print(success)

# Regenerate Certificates
print("Regenerating Certificates")
success = oneview_client.certificate_authority.delete("rabbitmq_readonly")
print(success)
