# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_detailed_one_of9 import RepositoryRuleDetailedOneOf9

class TestRepositoryRuleDetailedOneOf9(unittest.TestCase):
    """RepositoryRuleDetailedOneOf9 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleDetailedOneOf9:
        """Test RepositoryRuleDetailedOneOf9
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleDetailedOneOf9`
        """
        model = RepositoryRuleDetailedOneOf9()
        if include_optional:
            return RepositoryRuleDetailedOneOf9(
                type = 'non_fast_forward',
                ruleset_source_type = 'Repository',
                ruleset_source = '',
                ruleset_id = 56
            )
        else:
            return RepositoryRuleDetailedOneOf9(
                type = 'non_fast_forward',
        )
        """

    def testRepositoryRuleDetailedOneOf9(self):
        """Test RepositoryRuleDetailedOneOf9"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
