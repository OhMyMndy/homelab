# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_detailed_one_of4 import RepositoryRuleDetailedOneOf4

class TestRepositoryRuleDetailedOneOf4(unittest.TestCase):
    """RepositoryRuleDetailedOneOf4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleDetailedOneOf4:
        """Test RepositoryRuleDetailedOneOf4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleDetailedOneOf4`
        """
        model = RepositoryRuleDetailedOneOf4()
        if include_optional:
            return RepositoryRuleDetailedOneOf4(
                type = 'merge_queue',
                parameters = github_openapi.models.repository_rule_merge_queue_parameters.repository_rule_merge_queue_parameters(
                    check_response_timeout_minutes = 1, 
                    grouping_strategy = 'ALLGREEN', 
                    max_entries_to_build = 0, 
                    max_entries_to_merge = 0, 
                    merge_method = 'MERGE', 
                    min_entries_to_merge = 0, 
                    min_entries_to_merge_wait_minutes = 0, ),
                ruleset_source_type = 'Repository',
                ruleset_source = '',
                ruleset_id = 56
            )
        else:
            return RepositoryRuleDetailedOneOf4(
                type = 'merge_queue',
        )
        """

    def testRepositoryRuleDetailedOneOf4(self):
        """Test RepositoryRuleDetailedOneOf4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
