# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_status_branches_inner import WebhookStatusBranchesInner

class TestWebhookStatusBranchesInner(unittest.TestCase):
    """WebhookStatusBranchesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookStatusBranchesInner:
        """Test WebhookStatusBranchesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookStatusBranchesInner`
        """
        model = WebhookStatusBranchesInner()
        if include_optional:
            return WebhookStatusBranchesInner(
                commit = github_openapi.models.webhook_status_branches_inner_commit.webhook_status_branches_inner_commit(
                    sha = '', 
                    url = '', ),
                name = '',
                protected = True
            )
        else:
            return WebhookStatusBranchesInner(
                commit = github_openapi.models.webhook_status_branches_inner_commit.webhook_status_branches_inner_commit(
                    sha = '', 
                    url = '', ),
                name = '',
                protected = True,
        )
        """

    def testWebhookStatusBranchesInner(self):
        """Test WebhookStatusBranchesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
