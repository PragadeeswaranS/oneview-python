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

import os
from pprint import pprint
from hpOneView.oneview_client import OneViewClient

EXAMPLE_CONFIG_FILE = os.path.join(os.path.dirname(__file__), '../config.json')

oneview_client = OneViewClient.from_json_file(EXAMPLE_CONFIG_FILE)

image_streamer_client = oneview_client.create_image_streamer_client()

artifact_bundles_to_be_created = {
    "name": "Artifact Bundles Test",
    "description": "Description of Artifact Bundles Test",
    "buildPlans": [
        {
            "resourceUri": "/rest/build-plans/3ec91dd2-0ebb-4484-8b2d-90d065114315",
            "readOnly": "false"
        }
    ]
}

artifact_bundles_deployment_group = {
    "deploymentGroupURI": "/rest/deployment-groups/c5a727ef-71e9-4154-a512-6655b168c2e3"
}

artifact_bundle_file_path = {
    "download": "~/artifact_bundle.zip",
    "download_archive": "~/archive.zip",
    "name_upload": "artifact_bundle",
    "upload": "~/artifact_bundle.zip",
    "upload_backup": "~/backup.zip"
}

artifact_bundle_new_name = "Artifact Bundles Test Updated"

# Create an Artifact Bundle
print("\nCreate an Artifact Bundle")
response = image_streamer_client.artifact_bundles.create(artifact_bundles_to_be_created)
pprint(response)


# Get all Artifacts Bundle
print("\nGet all Artifact Bundles")
artifact_bundles = image_streamer_client.artifact_bundles.get_all()
for artifacts_bundle in artifact_bundles:
    pprint(artifacts_bundle)


# Get the Artifacts Bundle by Name
print("\nGet Artifact Bundles by Name")
artifact_bundle = image_streamer_client.artifact_bundles.get_by_name(artifact_bundles_to_be_created['name'])
pprint(artifact_bundle)


# Get the Artifacts Bundle
print("\nGet the Artifact Bundle")
response = image_streamer_client.artifact_bundles.get(artifact_bundle['uri'])
pprint(response)


# Download the Artifact Bundle
print("\nDownload the Artifact Bundle")
response = image_streamer_client.artifact_bundles.download_artifact_bundle(
    artifact_bundle['uri'], artifact_bundle_file_path['download'])
pprint(response)


# Download the Archive of the Artifact Bundle
print("\nDownload the Archive of the Artifact Bundle")
response = image_streamer_client.artifact_bundles\
    .download_archive_artifact_bundle(artifact_bundle['uri'], artifact_bundle_file_path['download_archive'])
pprint(response)


# Extract an Artifact Bundle
print("\nExtract an Artifact Bundle")
response = image_streamer_client.artifact_bundles.extract_bundle(artifact_bundle)
pprint(response)


# Update an Artifact Bundle
print("\nUpdate an Artifact Bundle")
artifact_bundle = image_streamer_client.artifact_bundles.get_by_name(artifact_bundles_to_be_created['name'])
artifact_bundle['name'] = artifact_bundle_new_name
response = image_streamer_client.artifact_bundles.update(artifact_bundle)
pprint(response)


# Delete an Artifact Bundle
print("\nDelete an Artifact Bundle")
artifact_bundle = image_streamer_client.artifact_bundles.get_by_name(artifact_bundle_new_name)
image_streamer_client.artifact_bundles.delete(artifact_bundle)


# Create a Backup for the Artifact Bundle
print("\nCreate a Backup for Artifact Bundle")
response = image_streamer_client.artifact_bundles.create_backup(artifact_bundles_deployment_group)
pprint(response)


# Get all Backups Bundles
print("\nGet all Backups Bundles")
backups_artifacts_bundle = image_streamer_client.artifact_bundles.get_all_backups()
pprint(backups_artifacts_bundle)


# Get Backup Bundle
print("\nGet Backup Bundle")
artifacts_bundle = image_streamer_client.artifact_bundles.get_backup(backups_artifacts_bundle[0]['uri'])
pprint(artifacts_bundle)


# Upload an Artifact Bundle from file
print("\nUpload an Artifact Bundle from file")
response = image_streamer_client.artifact_bundles.upload_bundle_from_file(artifact_bundle_file_path['upload'])
pprint(response)


# Upload a Backup of Artifact Bundle from file
print("\nUpload a Backup of Artifact Bundle from file")
response = image_streamer_client.artifact_bundles\
    .upload_backup_bundle_from_file(artifact_bundle_file_path['upload_backup'],
                                    artifact_bundles_deployment_group['deploymentGroupURI'])
pprint(response)


# Extract an Artifact Bundle
print("\nExtract an Artifact Bundle from Backup")
response = image_streamer_client.artifact_bundles.extract_backup_bundle(artifact_bundles_deployment_group)
pprint(response)


# Delete the Artifact Bundle created from file
print("\nDelete the Artifact Bundle created from file")
artifact_bundle = image_streamer_client.artifact_bundles.get_by_name(artifact_bundle_file_path['name_upload'])
image_streamer_client.artifact_bundles.delete(artifact_bundle)
