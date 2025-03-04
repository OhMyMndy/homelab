# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.snapshot import Snapshot

class TestSnapshot(unittest.TestCase):
    """Snapshot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Snapshot:
        """Test Snapshot
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Snapshot`
        """
        model = Snapshot()
        if include_optional:
            return Snapshot(
                version = 56,
                job = github_openapi.models.snapshot_job.snapshot_job(
                    id = '5622a2b0-63f6-4732-8c34-a1ab27e102a11', 
                    correlator = 'yourworkflowname_yourjobname', 
                    html_url = 'http://example.com/build', ),
                sha = 'ddc951f4b1293222421f2c8df679786153acf689',
                ref = 'refs/heads/main',
                detector = github_openapi.models.snapshot_detector.snapshot_detector(
                    name = 'docker buildtime detector', 
                    version = '1.0.0', 
                    url = 'http://example.com/docker-buildtimer-detector', ),
                metadata = {
                    'key' : null
                    },
                manifests = {
                    'key' : github_openapi.models.manifest.manifest(
                        name = 'package-lock.json', 
                        file = github_openapi.models.manifest_file.manifest_file(
                            source_location = '/src/build/package-lock.json', ), 
                        metadata = {
                            'key' : null
                            }, 
                        resolved = {
                            'key' : github_openapi.models.dependency.dependency(
                                package_url = 'pkg:/npm/%40actions/http-client@1.0.11', 
                                relationship = 'direct', 
                                scope = 'runtime', 
                                dependencies = @actions/http-client, )
                            }, )
                    },
                scanned = '2020-06-13T14:52:50-05:00'
            )
        else:
            return Snapshot(
                version = 56,
                job = github_openapi.models.snapshot_job.snapshot_job(
                    id = '5622a2b0-63f6-4732-8c34-a1ab27e102a11', 
                    correlator = 'yourworkflowname_yourjobname', 
                    html_url = 'http://example.com/build', ),
                sha = 'ddc951f4b1293222421f2c8df679786153acf689',
                ref = 'refs/heads/main',
                detector = github_openapi.models.snapshot_detector.snapshot_detector(
                    name = 'docker buildtime detector', 
                    version = '1.0.0', 
                    url = 'http://example.com/docker-buildtimer-detector', ),
                scanned = '2020-06-13T14:52:50-05:00',
        )
        """

    def testSnapshot(self):
        """Test Snapshot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
