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

from authentik_openapi.models.role_object_permission import RoleObjectPermission

class TestRoleObjectPermission(unittest.TestCase):
    """RoleObjectPermission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleObjectPermission:
        """Test RoleObjectPermission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleObjectPermission`
        """
        model = RoleObjectPermission()
        if include_optional:
            return RoleObjectPermission(
                id = 56,
                codename = '',
                model = '',
                app_label = '',
                object_pk = '',
                name = ''
            )
        else:
            return RoleObjectPermission(
                id = 56,
                codename = '',
                model = '',
                app_label = '',
                object_pk = '',
                name = '',
        )
        """

    def testRoleObjectPermission(self):
        """Test RoleObjectPermission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
