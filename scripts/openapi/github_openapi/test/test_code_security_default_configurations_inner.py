# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.code_security_default_configurations_inner import CodeSecurityDefaultConfigurationsInner

class TestCodeSecurityDefaultConfigurationsInner(unittest.TestCase):
    """CodeSecurityDefaultConfigurationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeSecurityDefaultConfigurationsInner:
        """Test CodeSecurityDefaultConfigurationsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeSecurityDefaultConfigurationsInner`
        """
        model = CodeSecurityDefaultConfigurationsInner()
        if include_optional:
            return CodeSecurityDefaultConfigurationsInner(
                default_for_new_repos = 'public',
                configuration = github_openapi.models.code_security_configuration.code-security-configuration(
                    id = 56, 
                    name = '', 
                    target_type = 'global', 
                    description = '', 
                    advanced_security = 'enabled', 
                    dependency_graph = 'enabled', 
                    dependency_graph_autosubmit_action = 'enabled', 
                    dependency_graph_autosubmit_action_options = github_openapi.models.code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options.code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options(
                        labeled_runners = True, ), 
                    dependabot_alerts = 'enabled', 
                    dependabot_security_updates = 'enabled', 
                    code_scanning_default_setup = 'enabled', 
                    code_scanning_default_setup_options = github_openapi.models.code_security_configuration_code_scanning_default_setup_options.code_security_configuration_code_scanning_default_setup_options(
                        runner_type = 'standard', 
                        runner_label = '', ), 
                    secret_scanning = 'enabled', 
                    secret_scanning_push_protection = 'enabled', 
                    secret_scanning_delegated_bypass = 'enabled', 
                    secret_scanning_delegated_bypass_options = github_openapi.models.code_security_create_configuration_request_secret_scanning_delegated_bypass_options.code_security_create_configuration_request_secret_scanning_delegated_bypass_options(
                        reviewers = [
                            github_openapi.models.code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner.code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner(
                                reviewer_id = 56, 
                                reviewer_type = 'TEAM', )
                            ], ), 
                    secret_scanning_validity_checks = 'enabled', 
                    secret_scanning_non_provider_patterns = 'enabled', 
                    private_vulnerability_reporting = 'enabled', 
                    enforcement = 'enforced', 
                    url = '', 
                    html_url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return CodeSecurityDefaultConfigurationsInner(
        )
        """

    def testCodeSecurityDefaultConfigurationsInner(self):
        """Test CodeSecurityDefaultConfigurationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
