# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.artifact import Artifact

class TestArtifact(unittest.TestCase):
    """Artifact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Artifact:
        """Test Artifact
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Artifact`
        """
        model = Artifact()
        if include_optional:
            return Artifact(
                id = 5,
                node_id = 'MDEwOkNoZWNrU3VpdGU1',
                name = 'AdventureWorks.Framework',
                size_in_bytes = 12345,
                url = 'https://api.github.com/repos/github/hello-world/actions/artifacts/5',
                archive_download_url = 'https://api.github.com/repos/github/hello-world/actions/artifacts/5/zip',
                expired = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                workflow_run = github_openapi.models.artifact_workflow_run.artifact_workflow_run(
                    id = 10, 
                    repository_id = 42, 
                    head_repository_id = 42, 
                    head_branch = 'main', 
                    head_sha = '009b8a3a9ccbb128af87f9b1c0f4c62e8a304f6d', )
            )
        else:
            return Artifact(
                id = 5,
                node_id = 'MDEwOkNoZWNrU3VpdGU1',
                name = 'AdventureWorks.Framework',
                size_in_bytes = 12345,
                url = 'https://api.github.com/repos/github/hello-world/actions/artifacts/5',
                archive_download_url = 'https://api.github.com/repos/github/hello-world/actions/artifacts/5/zip',
                expired = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testArtifact(self):
        """Test Artifact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
