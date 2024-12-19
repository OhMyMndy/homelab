# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_openapi.models.patched_scim_source_user_request import PatchedSCIMSourceUserRequest

class TestPatchedSCIMSourceUserRequest(unittest.TestCase):
    """PatchedSCIMSourceUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedSCIMSourceUserRequest:
        """Test PatchedSCIMSourceUserRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedSCIMSourceUserRequest`
        """
        model = PatchedSCIMSourceUserRequest()
        if include_optional:
            return PatchedSCIMSourceUserRequest(
                id = '0',
                user = 56,
                source = '',
                attributes = None
            )
        else:
            return PatchedSCIMSourceUserRequest(
        )
        """

    def testPatchedSCIMSourceUserRequest(self):
        """Test PatchedSCIMSourceUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
