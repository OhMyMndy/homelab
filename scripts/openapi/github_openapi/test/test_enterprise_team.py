# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.enterprise_team import EnterpriseTeam

class TestEnterpriseTeam(unittest.TestCase):
    """EnterpriseTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnterpriseTeam:
        """Test EnterpriseTeam
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnterpriseTeam`
        """
        model = EnterpriseTeam()
        if include_optional:
            return EnterpriseTeam(
                id = 56,
                name = '',
                slug = '',
                url = '',
                sync_to_organizations = 'disabled | all',
                group_id = '62ab9291-fae2-468e-974b-7e45096d5021',
                html_url = 'https://github.com/enterprises/dc/teams/justice-league',
                members_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return EnterpriseTeam(
                id = 56,
                name = '',
                slug = '',
                url = '',
                sync_to_organizations = 'disabled | all',
                html_url = 'https://github.com/enterprises/dc/teams/justice-league',
                members_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testEnterpriseTeam(self):
        """Test EnterpriseTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
