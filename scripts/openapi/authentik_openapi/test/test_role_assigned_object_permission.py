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

from authentik_openapi.models.role_assigned_object_permission import RoleAssignedObjectPermission

class TestRoleAssignedObjectPermission(unittest.TestCase):
    """RoleAssignedObjectPermission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleAssignedObjectPermission:
        """Test RoleAssignedObjectPermission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleAssignedObjectPermission`
        """
        model = RoleAssignedObjectPermission()
        if include_optional:
            return RoleAssignedObjectPermission(
                role_pk = '',
                name = '',
                permissions = [
                    authentik_openapi.models.role_object_permission.RoleObjectPermission(
                        id = 56, 
                        codename = '', 
                        model = '', 
                        app_label = '', 
                        object_pk = '', 
                        name = '', )
                    ]
            )
        else:
            return RoleAssignedObjectPermission(
                role_pk = '',
                name = '',
                permissions = [
                    authentik_openapi.models.role_object_permission.RoleObjectPermission(
                        id = 56, 
                        codename = '', 
                        model = '', 
                        app_label = '', 
                        object_pk = '', 
                        name = '', )
                    ],
        )
        """

    def testRoleAssignedObjectPermission(self):
        """Test RoleAssignedObjectPermission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()