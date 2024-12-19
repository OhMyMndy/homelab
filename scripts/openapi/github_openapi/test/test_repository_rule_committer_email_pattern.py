# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_committer_email_pattern import RepositoryRuleCommitterEmailPattern

class TestRepositoryRuleCommitterEmailPattern(unittest.TestCase):
    """RepositoryRuleCommitterEmailPattern unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleCommitterEmailPattern:
        """Test RepositoryRuleCommitterEmailPattern
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleCommitterEmailPattern`
        """
        model = RepositoryRuleCommitterEmailPattern()
        if include_optional:
            return RepositoryRuleCommitterEmailPattern(
                type = 'committer_email_pattern',
                parameters = github_openapi.models.repository_rule_commit_message_pattern_parameters.repository_rule_commit_message_pattern_parameters(
                    name = '', 
                    negate = True, 
                    operator = 'starts_with', 
                    pattern = '', )
            )
        else:
            return RepositoryRuleCommitterEmailPattern(
                type = 'committer_email_pattern',
        )
        """

    def testRepositoryRuleCommitterEmailPattern(self):
        """Test RepositoryRuleCommitterEmailPattern"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()