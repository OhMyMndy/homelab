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

from authentik_openapi.models.group_member import GroupMember

class TestGroupMember(unittest.TestCase):
    """GroupMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupMember:
        """Test GroupMember
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupMember`
        """
        model = GroupMember()
        if include_optional:
            return GroupMember(
                pk = 56,
                username = 'A',
                name = '',
                is_active = True,
                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '',
                attributes = {
                    'key' : null
                    },
                uid = ''
            )
        else:
            return GroupMember(
                pk = 56,
                username = 'A',
                name = '',
                uid = '',
        )
        """

    def testGroupMember(self):
        """Test GroupMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
