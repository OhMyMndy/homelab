# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_update_release_asset_request import ReposUpdateReleaseAssetRequest

class TestReposUpdateReleaseAssetRequest(unittest.TestCase):
    """ReposUpdateReleaseAssetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposUpdateReleaseAssetRequest:
        """Test ReposUpdateReleaseAssetRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposUpdateReleaseAssetRequest`
        """
        model = ReposUpdateReleaseAssetRequest()
        if include_optional:
            return ReposUpdateReleaseAssetRequest(
                name = '',
                label = '',
                state = '"uploaded"'
            )
        else:
            return ReposUpdateReleaseAssetRequest(
        )
        """

    def testReposUpdateReleaseAssetRequest(self):
        """Test ReposUpdateReleaseAssetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
