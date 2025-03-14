# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.copilot_seat_details_assigning_team import CopilotSeatDetailsAssigningTeam

class TestCopilotSeatDetailsAssigningTeam(unittest.TestCase):
    """CopilotSeatDetailsAssigningTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopilotSeatDetailsAssigningTeam:
        """Test CopilotSeatDetailsAssigningTeam
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopilotSeatDetailsAssigningTeam`
        """
        model = CopilotSeatDetailsAssigningTeam()
        if include_optional:
            return CopilotSeatDetailsAssigningTeam(
                id = 56,
                node_id = '',
                name = '',
                slug = '',
                description = '',
                privacy = '',
                notification_setting = '',
                permission = '',
                permissions = github_openapi.models.team_permissions.team_permissions(
                    pull = True, 
                    triage = True, 
                    push = True, 
                    maintain = True, 
                    admin = True, ),
                url = '',
                html_url = 'https://github.com/enterprises/dc/teams/justice-league',
                members_url = '',
                repositories_url = '',
                parent = github_openapi.models.team_simple.Team Simple(
                    id = 1, 
                    node_id = 'MDQ6VGVhbTE=', 
                    url = 'https://api.github.com/organizations/1/team/1', 
                    members_url = 'https://api.github.com/organizations/1/team/1/members{/member}', 
                    name = 'Justice League', 
                    description = 'A great team.', 
                    permission = 'admin', 
                    privacy = 'closed', 
                    notification_setting = 'notifications_enabled', 
                    html_url = 'https://github.com/orgs/rails/teams/core', 
                    repositories_url = 'https://api.github.com/organizations/1/team/1/repos', 
                    slug = 'justice-league', 
                    ldap_dn = 'uid=example,ou=users,dc=github,dc=com', ),
                sync_to_organizations = 'disabled | all',
                group_id = '62ab9291-fae2-468e-974b-7e45096d5021',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CopilotSeatDetailsAssigningTeam(
                id = 56,
                node_id = '',
                name = '',
                slug = '',
                description = '',
                permission = '',
                url = '',
                html_url = 'https://github.com/enterprises/dc/teams/justice-league',
                members_url = '',
                repositories_url = '',
                parent = github_openapi.models.team_simple.Team Simple(
                    id = 1, 
                    node_id = 'MDQ6VGVhbTE=', 
                    url = 'https://api.github.com/organizations/1/team/1', 
                    members_url = 'https://api.github.com/organizations/1/team/1/members{/member}', 
                    name = 'Justice League', 
                    description = 'A great team.', 
                    permission = 'admin', 
                    privacy = 'closed', 
                    notification_setting = 'notifications_enabled', 
                    html_url = 'https://github.com/orgs/rails/teams/core', 
                    repositories_url = 'https://api.github.com/organizations/1/team/1/repos', 
                    slug = 'justice-league', 
                    ldap_dn = 'uid=example,ou=users,dc=github,dc=com', ),
                sync_to_organizations = 'disabled | all',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCopilotSeatDetailsAssigningTeam(self):
        """Test CopilotSeatDetailsAssigningTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
