# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.secret_scanning_location_commit import SecretScanningLocationCommit

class TestSecretScanningLocationCommit(unittest.TestCase):
    """SecretScanningLocationCommit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecretScanningLocationCommit:
        """Test SecretScanningLocationCommit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecretScanningLocationCommit`
        """
        model = SecretScanningLocationCommit()
        if include_optional:
            return SecretScanningLocationCommit(
                path = '/example/secrets.txt',
                start_line = 1.337,
                end_line = 1.337,
                start_column = 1.337,
                end_column = 1.337,
                blob_sha = 'af5626b4a114abcb82d63db7c8082c3c4756e51b',
                blob_url = '',
                commit_sha = 'af5626b4a114abcb82d63db7c8082c3c4756e51b',
                commit_url = ''
            )
        else:
            return SecretScanningLocationCommit(
                path = '/example/secrets.txt',
                start_line = 1.337,
                end_line = 1.337,
                start_column = 1.337,
                end_column = 1.337,
                blob_sha = 'af5626b4a114abcb82d63db7c8082c3c4756e51b',
                blob_url = '',
                commit_sha = 'af5626b4a114abcb82d63db7c8082c3c4756e51b',
                commit_url = '',
        )
        """

    def testSecretScanningLocationCommit(self):
        """Test SecretScanningLocationCommit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
