# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.api_overview_ssh_key_fingerprints import ApiOverviewSshKeyFingerprints

class TestApiOverviewSshKeyFingerprints(unittest.TestCase):
    """ApiOverviewSshKeyFingerprints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiOverviewSshKeyFingerprints:
        """Test ApiOverviewSshKeyFingerprints
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiOverviewSshKeyFingerprints`
        """
        model = ApiOverviewSshKeyFingerprints()
        if include_optional:
            return ApiOverviewSshKeyFingerprints(
                sha256_rsa = '',
                sha256_dsa = '',
                sha256_ecdsa = '',
                sha256_ed25519 = ''
            )
        else:
            return ApiOverviewSshKeyFingerprints(
        )
        """

    def testApiOverviewSshKeyFingerprints(self):
        """Test ApiOverviewSshKeyFingerprints"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
