# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.review_comment_links import ReviewCommentLinks

class TestReviewCommentLinks(unittest.TestCase):
    """ReviewCommentLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReviewCommentLinks:
        """Test ReviewCommentLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReviewCommentLinks`
        """
        model = ReviewCommentLinks()
        if include_optional:
            return ReviewCommentLinks(
                var_self = github_openapi.models.link.Link(
                    href = '', ),
                html = github_openapi.models.link.Link(
                    href = '', ),
                pull_request = github_openapi.models.link.Link(
                    href = '', )
            )
        else:
            return ReviewCommentLinks(
                var_self = github_openapi.models.link.Link(
                    href = '', ),
                html = github_openapi.models.link.Link(
                    href = '', ),
                pull_request = github_openapi.models.link.Link(
                    href = '', ),
        )
        """

    def testReviewCommentLinks(self):
        """Test ReviewCommentLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
