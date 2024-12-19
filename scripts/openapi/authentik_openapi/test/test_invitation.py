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

from authentik_openapi.models.invitation import Invitation

class TestInvitation(unittest.TestCase):
    """Invitation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Invitation:
        """Test Invitation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Invitation`
        """
        model = Invitation()
        if include_optional:
            return Invitation(
                pk = '',
                name = 'z',
                expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fixed_data = {
                    'key' : null
                    },
                created_by = authentik_openapi.models.group_member.GroupMember(
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
                single_use = True,
                flow = '',
                flow_obj = authentik_openapi.models.flow.Flow(
                    pk = '', 
                    policybindingmodel_ptr_id = '', 
                    name = '', 
                    slug = 'z', 
                    title = '', 
                    designation = null, 
                    background = '', 
                    stages = [
                        ''
                        ], 
                    policies = [
                        ''
                        ], 
                    cache_count = 56, 
                    policy_engine_mode = 'all', 
                    compatibility_mode = True, 
                    export_url = '', 
                    layout = 'stacked', 
                    denied_action = null, 
                    authentication = null, )
            )
        else:
            return Invitation(
                pk = '',
                name = 'z',
                created_by = authentik_openapi.models.group_member.GroupMember(
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
                flow_obj = authentik_openapi.models.flow.Flow(
                    pk = '', 
                    policybindingmodel_ptr_id = '', 
                    name = '', 
                    slug = 'z', 
                    title = '', 
                    designation = null, 
                    background = '', 
                    stages = [
                        ''
                        ], 
                    policies = [
                        ''
                        ], 
                    cache_count = 56, 
                    policy_engine_mode = 'all', 
                    compatibility_mode = True, 
                    export_url = '', 
                    layout = 'stacked', 
                    denied_action = null, 
                    authentication = null, ),
        )
        """

    def testInvitation(self):
        """Test Invitation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
