# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest

class TestTeamsCreateDiscussionCommentInOrgRequest(unittest.TestCase):
    """TeamsCreateDiscussionCommentInOrgRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamsCreateDiscussionCommentInOrgRequest:
        """Test TeamsCreateDiscussionCommentInOrgRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamsCreateDiscussionCommentInOrgRequest`
        """
        model = TeamsCreateDiscussionCommentInOrgRequest()
        if include_optional:
            return TeamsCreateDiscussionCommentInOrgRequest(
                body = ''
            )
        else:
            return TeamsCreateDiscussionCommentInOrgRequest(
                body = '',
        )
        """

    def testTeamsCreateDiscussionCommentInOrgRequest(self):
        """Test TeamsCreateDiscussionCommentInOrgRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
