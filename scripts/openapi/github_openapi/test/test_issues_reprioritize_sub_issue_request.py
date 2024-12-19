# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.issues_reprioritize_sub_issue_request import IssuesReprioritizeSubIssueRequest

class TestIssuesReprioritizeSubIssueRequest(unittest.TestCase):
    """IssuesReprioritizeSubIssueRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IssuesReprioritizeSubIssueRequest:
        """Test IssuesReprioritizeSubIssueRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IssuesReprioritizeSubIssueRequest`
        """
        model = IssuesReprioritizeSubIssueRequest()
        if include_optional:
            return IssuesReprioritizeSubIssueRequest(
                sub_issue_id = 56,
                after_id = 56,
                before_id = 56
            )
        else:
            return IssuesReprioritizeSubIssueRequest(
                sub_issue_id = 56,
        )
        """

    def testIssuesReprioritizeSubIssueRequest(self):
        """Test IssuesReprioritizeSubIssueRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
