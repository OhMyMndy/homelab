# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_detailed_one_of7 import RepositoryRuleDetailedOneOf7

class TestRepositoryRuleDetailedOneOf7(unittest.TestCase):
    """RepositoryRuleDetailedOneOf7 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleDetailedOneOf7:
        """Test RepositoryRuleDetailedOneOf7
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleDetailedOneOf7`
        """
        model = RepositoryRuleDetailedOneOf7()
        if include_optional:
            return RepositoryRuleDetailedOneOf7(
                type = 'pull_request',
                parameters = github_openapi.models.repository_rule_pull_request_parameters.repository_rule_pull_request_parameters(
                    allowed_merge_methods = [
                        ''
                        ], 
                    dismiss_stale_reviews_on_push = True, 
                    require_code_owner_review = True, 
                    require_last_push_approval = True, 
                    required_approving_review_count = 0, 
                    required_review_thread_resolution = True, ),
                ruleset_source_type = 'Repository',
                ruleset_source = '',
                ruleset_id = 56
            )
        else:
            return RepositoryRuleDetailedOneOf7(
                type = 'pull_request',
        )
        """

    def testRepositoryRuleDetailedOneOf7(self):
        """Test RepositoryRuleDetailedOneOf7"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
