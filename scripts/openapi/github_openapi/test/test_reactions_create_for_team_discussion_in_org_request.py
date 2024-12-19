# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.reactions_create_for_team_discussion_in_org_request import ReactionsCreateForTeamDiscussionInOrgRequest

class TestReactionsCreateForTeamDiscussionInOrgRequest(unittest.TestCase):
    """ReactionsCreateForTeamDiscussionInOrgRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReactionsCreateForTeamDiscussionInOrgRequest:
        """Test ReactionsCreateForTeamDiscussionInOrgRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReactionsCreateForTeamDiscussionInOrgRequest`
        """
        model = ReactionsCreateForTeamDiscussionInOrgRequest()
        if include_optional:
            return ReactionsCreateForTeamDiscussionInOrgRequest(
                content = '+1'
            )
        else:
            return ReactionsCreateForTeamDiscussionInOrgRequest(
                content = '+1',
        )
        """

    def testReactionsCreateForTeamDiscussionInOrgRequest(self):
        """Test ReactionsCreateForTeamDiscussionInOrgRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()