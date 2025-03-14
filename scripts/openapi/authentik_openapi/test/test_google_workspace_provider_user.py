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

from authentik_openapi.models.google_workspace_provider_user import GoogleWorkspaceProviderUser

class TestGoogleWorkspaceProviderUser(unittest.TestCase):
    """GoogleWorkspaceProviderUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleWorkspaceProviderUser:
        """Test GoogleWorkspaceProviderUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleWorkspaceProviderUser`
        """
        model = GoogleWorkspaceProviderUser()
        if include_optional:
            return GoogleWorkspaceProviderUser(
                id = '',
                google_id = '',
                user = 56,
                user_obj = authentik_openapi.models.group_member.GroupMember(
                    pk = 56, 
                    username = 'A', 
                    name = '', 
                    is_active = True, 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    attributes = {
                        'key' : null
                        }, 
                    uid = '', ),
                provider = 56,
                attributes = None
            )
        else:
            return GoogleWorkspaceProviderUser(
                id = '',
                google_id = '',
                user = 56,
                user_obj = authentik_openapi.models.group_member.GroupMember(
                    pk = 56, 
                    username = 'A', 
                    name = '', 
                    is_active = True, 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    attributes = {
                        'key' : null
                        }, 
                    uid = '', ),
                provider = 56,
                attributes = None,
        )
        """

    def testGoogleWorkspaceProviderUser(self):
        """Test GoogleWorkspaceProviderUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
