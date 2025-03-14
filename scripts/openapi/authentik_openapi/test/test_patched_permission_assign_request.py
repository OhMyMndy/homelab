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

from authentik_openapi.models.patched_permission_assign_request import PatchedPermissionAssignRequest

class TestPatchedPermissionAssignRequest(unittest.TestCase):
    """PatchedPermissionAssignRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedPermissionAssignRequest:
        """Test PatchedPermissionAssignRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedPermissionAssignRequest`
        """
        model = PatchedPermissionAssignRequest()
        if include_optional:
            return PatchedPermissionAssignRequest(
                permissions = [
                    '0'
                    ],
                model = 'authentik_tenants.domain',
                object_pk = '0'
            )
        else:
            return PatchedPermissionAssignRequest(
        )
        """

    def testPatchedPermissionAssignRequest(self):
        """Test PatchedPermissionAssignRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
