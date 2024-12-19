# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.team_parent import TeamParent

class TestTeamParent(unittest.TestCase):
    """TeamParent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamParent:
        """Test TeamParent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamParent`
        """
        model = TeamParent()
        if include_optional:
            return TeamParent(
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
                url = ''
            )
        else:
            return TeamParent(
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

    def testTeamParent(self):
        """Test TeamParent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
