# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_set_team_access_restrictions_request_one_of import ReposSetTeamAccessRestrictionsRequestOneOf

class TestReposSetTeamAccessRestrictionsRequestOneOf(unittest.TestCase):
    """ReposSetTeamAccessRestrictionsRequestOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposSetTeamAccessRestrictionsRequestOneOf:
        """Test ReposSetTeamAccessRestrictionsRequestOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposSetTeamAccessRestrictionsRequestOneOf`
        """
        model = ReposSetTeamAccessRestrictionsRequestOneOf()
        if include_optional:
            return ReposSetTeamAccessRestrictionsRequestOneOf(
                teams = [
                    ''
                    ]
            )
        else:
            return ReposSetTeamAccessRestrictionsRequestOneOf(
                teams = [
                    ''
                    ],
        )
        """

    def testReposSetTeamAccessRestrictionsRequestOneOf(self):
        """Test ReposSetTeamAccessRestrictionsRequestOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
