# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_rule_required_status_checks import RepositoryRuleRequiredStatusChecks

class TestRepositoryRuleRequiredStatusChecks(unittest.TestCase):
    """RepositoryRuleRequiredStatusChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryRuleRequiredStatusChecks:
        """Test RepositoryRuleRequiredStatusChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryRuleRequiredStatusChecks`
        """
        model = RepositoryRuleRequiredStatusChecks()
        if include_optional:
            return RepositoryRuleRequiredStatusChecks(
                type = 'required_status_checks',
                parameters = github_openapi.models.repository_rule_required_status_checks_parameters.repository_rule_required_status_checks_parameters(
                    do_not_enforce_on_create = True, 
                    required_status_checks = [
                        github_openapi.models.status_check_configuration.StatusCheckConfiguration(
                            context = '', 
                            integration_id = 56, )
                        ], 
                    strict_required_status_checks_policy = True, )
            )
        else:
            return RepositoryRuleRequiredStatusChecks(
                type = 'required_status_checks',
        )
        """

    def testRepositoryRuleRequiredStatusChecks(self):
        """Test RepositoryRuleRequiredStatusChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
