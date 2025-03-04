# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_detailed_one_of16 import RepositoryRuleDetailedOneOf16

class TestRepositoryRuleDetailedOneOf16(unittest.TestCase):
    """RepositoryRuleDetailedOneOf16 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleDetailedOneOf16:
        """Test RepositoryRuleDetailedOneOf16
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleDetailedOneOf16`
        """
        model = RepositoryRuleDetailedOneOf16()
        if include_optional:
            return RepositoryRuleDetailedOneOf16(
                type = 'code_scanning',
                parameters = github_openapi.models.repository_rule_code_scanning_parameters.repository_rule_code_scanning_parameters(
                    code_scanning_tools = [
                        github_openapi.models.code_scanning_tool.CodeScanningTool(
                            alerts_threshold = 'none', 
                            security_alerts_threshold = 'none', 
                            tool = '', )
                        ], ),
                ruleset_source_type = 'Repository',
                ruleset_source = '',
                ruleset_id = 56
            )
        else:
            return RepositoryRuleDetailedOneOf16(
                type = 'code_scanning',
        )
        """

    def testRepositoryRuleDetailedOneOf16(self):
        """Test RepositoryRuleDetailedOneOf16"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
