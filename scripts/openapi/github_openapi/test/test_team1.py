# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.team1 import Team1

class TestTeam1(unittest.TestCase):
    """Team1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Team1:
        """Test Team1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Team1`
        """
        model = Team1()
        if include_optional:
            return Team1(
                deleted = True,
                description = '',
                html_url = '',
                id = 56,
                members_url = '',
                name = '',
                node_id = '',
                parent = github_openapi.models.team_parent.Team_parent(
                    description = '', 
                    html_url = '', 
                    id = 56, 
                    members_url = '', 
                    name = '', 
                    node_id = '', 
                    permission = '', 
                    privacy = 'open', 
                    repositories_url = '', 
                    slug = '', 
                    url = '', ),
                permission = '',
                privacy = 'open',
                repositories_url = '',
                slug = '',
                url = ''
            )
        else:
            return Team1(
                description = '',
                html_url = '',
                id = 56,
                members_url = '',
                name = '',
                node_id = '',
                permission = '',
                privacy = 'open',
                repositories_url = '',
                slug = '',
                url = '',
        )
        """

    def testTeam1(self):
        """Test Team1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
