# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.copilot_dotcom_pull_requests_repositories_inner_models_inner import CopilotDotcomPullRequestsRepositoriesInnerModelsInner

class TestCopilotDotcomPullRequestsRepositoriesInnerModelsInner(unittest.TestCase):
    """CopilotDotcomPullRequestsRepositoriesInnerModelsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopilotDotcomPullRequestsRepositoriesInnerModelsInner:
        """Test CopilotDotcomPullRequestsRepositoriesInnerModelsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopilotDotcomPullRequestsRepositoriesInnerModelsInner`
        """
        model = CopilotDotcomPullRequestsRepositoriesInnerModelsInner()
        if include_optional:
            return CopilotDotcomPullRequestsRepositoriesInnerModelsInner(
                name = '',
                is_custom_model = True,
                custom_model_training_date = '',
                total_pr_summaries_created = 56,
                total_engaged_users = 56
            )
        else:
            return CopilotDotcomPullRequestsRepositoriesInnerModelsInner(
        )
        """

    def testCopilotDotcomPullRequestsRepositoriesInnerModelsInner(self):
        """Test CopilotDotcomPullRequestsRepositoriesInnerModelsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()