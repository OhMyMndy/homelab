# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.node_info_usage_users import NodeInfoUsageUsers

class TestNodeInfoUsageUsers(unittest.TestCase):
    """NodeInfoUsageUsers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeInfoUsageUsers:
        """Test NodeInfoUsageUsers
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeInfoUsageUsers`
        """
        model = NodeInfoUsageUsers()
        if include_optional:
            return NodeInfoUsageUsers(
                active_halfyear = 56,
                active_month = 56,
                total = 56
            )
        else:
            return NodeInfoUsageUsers(
        )
        """

    def testNodeInfoUsageUsers(self):
        """Test NodeInfoUsageUsers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
